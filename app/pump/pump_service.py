
import RPi.GPIO as GPIO
import time


class PumpService:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.OUT)
        
    def do_watering(self, duration: int) -> None:
        self.start_pump()
        time.sleep(duration)
        self.stop_pump()

    def start_pump(self) -> None:
        GPIO.output(23, GPIO.LOW)
        # Logic to start the pump
        print("Pump started.")

    def stop_pump(self) -> None:
        GPIO.output(23, GPIO.HIGH)
        # Logic to stop the pump
        print("Pump stopped.")


if __name__ == "__main__":
    pump_service = PumpService()
    try:
        pump_service.do_watering(1)  # Start the pump for 10 seconds
    except KeyboardInterrupt:
        print("Pump service interrupted.")
        pump_service.stop_pump()
    finally:
        GPIO.cleanup()  # Clean up GPIO settings