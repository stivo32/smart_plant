
import RPi.GPIO as GPIO
import time
import datetime

from app.storage.action_logger import log_action
from app.storage.models import MoistureSensorData, Pump
from app.db import session_factory


class PumpService:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.OUT)

    def do_watering(self, duration: int) -> None:
        start = datetime.datetime.now(datetime.timezone.utc)
        self.start_pump()
        time.sleep(duration)
        self.stop_pump()
        stop = datetime.datetime.now(datetime.timezone.utc)
        with session_factory() as session:
            pump_action = Pump(
                start=start, 
                stop=stop,
                duration=duration
            )
            session.add(pump_action)
            session.commit()

    @log_action
    def start_pump(self) -> None:
        GPIO.output(23, GPIO.LOW)
        # Logic to start the pump
        print("Pump started.")

    @log_action
    def stop_pump(self) -> None:
        GPIO.output(23, GPIO.HIGH)
        # Logic to stop the pump
        print("Pump stopped.")

    def __del__(self):
        GPIO.cleanup()


def do_watering() -> None:
    pump_service = PumpService()
    print("Starting watering process...")

    six_hours_ago = datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=6)

    with session_factory() as session:
        moisture = (
            session.query(MoistureSensorData)
            .filter(MoistureSensorData.timestamp >= six_hours_ago)
            .order_by(MoistureSensorData.id.desc())
            .first()
        )
        if not moisture:
            print("No moisture data found, cannot determine watering need.")
            raise ValueError("No moisture data available.")
        if moisture.moisture_percentage < 30:
            duration = 3
            pump_service.do_watering(duration)
        else:
            print("Moisture level is sufficient, no need to water.")


if __name__ == "__main__":
    do_watering()