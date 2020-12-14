from enum import IntEnum, auto


class EnableableDevice(IntEnum):
    RECEIVER = 0
    CAMERA = auto()
    KEYBOARD = auto()
    BATTERY_SENSOR = auto()
    GPS = auto()
    COMPASS = auto()
    INERTIAL_UNIT = auto()
    GYRO = auto()


class NonEnableableDevice(IntEnum):
    LED = 100
    EMITTER = auto()


class MotorDevice(IntEnum):
    CAMERA = 200
    PROPELLER = auto()


class AircraftAxis(IntEnum):
    ROLL = 300
    PITCH = auto()
    YAW = auto()


class Relative2DPosition:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        x = 'front' if self.x == 1 else 'rear'
        y = 'left' if self.y == 1 else 'right'
        return f"{x} {y}"