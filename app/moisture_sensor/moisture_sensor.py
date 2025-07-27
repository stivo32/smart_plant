
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

from app.storage.action_logger import log_action
from app.storage.models import MoistureSensorData
from app.db import session_factory


class MoistureSensor:
    def __init__(self):
        self.gpio = digitalio.DigitalInOut(board.D21)
        self.gpio.direction = digitalio.Direction.OUTPUT
        self.gpio.value = False  # Начальное состояние - выключено

        # Настройка MCP3008
        spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        cs = digitalio.DigitalInOut(board.D5)
        mcp = MCP.MCP3008(spi, cs)
        self.channel = AnalogIn(mcp, MCP.P0)

    @log_action
    def read_moisture(self):
        self.gpio.value = True  # Включить питание датчика
        time.sleep(0.1)    # Ждем стабилизации (100 мс)
        value = self.channel.value
        self.gpio.value = False  # Выключить питание
        percent = self.convert_to_percentage(value)
        with session_factory() as session:
            moisture_data = MoistureSensorData(
                moisture_level=value,
                moisture_percentage=percent
            )
            session.add(moisture_data)
            session.commit()
        return percent


    def convert_to_percentage(self, value: int) -> float:
        DRY = 65535
        WATER = 40000
        if value < WATER:
            return 100.0
        
        if value > DRY:
            return 0.0
        return ((DRY - value) / (DRY - WATER)) * 100



def read_moisture() -> None:
    moisture_sensor = MoistureSensor()
    print("Reading moisture level...")
    moisture_sensor.read_moisture()
    

if __name__ == "__main__":
    sensor = MoistureSensor()
    while True:
        moisture = sensor.read_moisture()
        print(f"Влажность: {moisture:.2f} %")
        time.sleep(5)