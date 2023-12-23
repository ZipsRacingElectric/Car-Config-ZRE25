# GPIO Interface --------------------------------------------------------------------------------------------------------------
# Author: Cole Barach
# Date Created: 23.04.05
# Date Updated: 23.04.29

# Libraries -------------------------------------------------------------------------------------------------------------------
# import gpiozero

import os
import sys
import threading
import time

import logging

# Imports ---------------------------------------------------------------------------------------------------------------------
import config

import can_interface

# Functions -------------------------------------------------------------------------------------------------------------------
def Setup(db, canT):
    try:
        if(config.USE_GPIO != True): return None

        global database
        global can_transmitter
        global interface

        database = db
        can_transmitter = canT

        interface = None

        if(sys.platform == "win32"): return None

        interface = Main()

        database["Torque_Config_Limit"] = config.TORQUE_LIMIT / 10
        database["Torque_Config_Limit_Regen"] = 0
        database["State_Regen_Config_Enabled"] = False

        # interface.InsertDigital(config.GPIO_BUTTON_START, StartButtonPress)
        interface.InsertDigital(config.GPIO_BUTTON_REGEN, RegenButtonPress)
        interface.InsertDigital(config.GPIO_BUTTON_WHEEL_L, LeftButtonPress)
        interface.InsertDigital(config.GPIO_BUTTON_WHEEL_R, RightButtonPress)
        
        interface.InsertRotary(config.GPIO_ROT_TORQUE_PIN_A, config.GPIO_ROT_TORQUE_PIN_B, TorqueEncoderInterrupt)
        interface.InsertRotary(config.GPIO_ROT_REGEN_PIN_A,  config.GPIO_ROT_REGEN_PIN_B,  RegenEncoderInterrupt)

        interface.InsertRgb(config.GPIO_RGB_PIN_R, config.GPIO_RGB_PIN_G, config.GPIO_RGB_PIN_B)

        # interface.InsertService(CanSendService)

        return interface
        # return None
    except Exception as e:
        logging.error("GPIO Setup failure: " + str(e))
        raise

def StartButtonPress():
    pass
    # global can_transmitter
    # can_interface.SendCommandDriveStart(can_transmitter, True)

def RegenButtonPress():
    pass
    # global database
    # database["State_Regen_Config_Enabled"] = not database["State_Regen_Config_Enabled"]

    # global can_transmitter
    # can_interface.SendCommandDriveConfiguration(can_transmitter, database)

def LeftButtonPress():
    if(database["Torque_Config_Limit"] == None): pass
    if(database["Torque_Config_Limit"] >= 30): pass
    database["Torque_Config_Limit"] += 11

    can_transmitter.SendCommandDriveConfiguration()

def RightButtonPress():
    if(database["Torque_Config_Limit"] == None): pass
    if(database["Torque_Config_Limit"] <= 0): pass
    database["Torque_Config_Limit"] -= 11

    can_transmitter.SendCommandDriveConfiguration()

def TorqueEncoderInterrupt(direction):
    pass
    # global database
    # database["Torque_Config_Limit"] += direction * config.GPIO_ROT_TORQUE_SENSITIVITY

    # if(database["Torque_Config_Limit"] > config.TORQUE_LIMIT): database["Torque_Config_Limit"] = config.TORQUE_LIMIT
    # if(database["Torque_Config_Limit"] < 0): database["Torque_Config_Limit"] = 0

    # global can_transmitter
    # can_interface.SendCommandDriveConfiguration(can_transmitter, database)

def RegenEncoderInterrupt(direction):
    pass
    # global database
    # database["Torque_Config_Limit_Regen"] += direction * config.GPIO_ROT_REGEN_SENSITIVITY

    # if(database["Torque_Config_Limit_Regen"] > config.REGEN_LIMIT): database["Torque_Config_Limit_Regen"] = config.REGEN_LIMIT
    # if(database["Torque_Config_Limit_Regen"] < 0): database["Torque_Config_Limit_Regen"] = 0

    # global can_transmitter
    # can_interface.SendCommandDriveConfiguration(can_transmitter, database)

def SetRgb(pinR, colorR, colorG, colorB, period):
    pass
    # global interface
    # if(interface == None): return

    # interface.SetRgb(pinR, colorR, colorG, colorB, period)

# GUI Object ------------------------------------------------------------------------------------------------------------------
class Main():
    def __init__(self):
        try:
            logging.debug("GPIO - Initializing...")
        
            self.digitalInputs     = dict()
            self.rotaryInputs      = dict()
            self.rotaryInterrupts  = dict()
            self.rgbOutputs        = dict()
            self.rgbColors         = dict()
            self.rgbTimers         = dict()
            self.rgbPeriods        = dict()
            self.rgbStates         = dict()
            self.services          = []

            self.online = True

            logging.debug("GPIO - Initialized.")
        except Exception as e:
            logging.error("GPIO Initialization failed: " + str(e))

    def Begin(self):
        self.scanningThread = threading.Thread(target=self.ScanInterrupts)
        self.scanningThread.start()

    def InsertDigital(self, pin, handler):
        try:
            logging.debug(f"GPIO - Inserting Digital Interrupt for Pin: {pin}...")
            self.digitalInputs[pin] = gpiozero.Button(pin)
            self.digitalInputs[pin].when_pressed = handler
        except Exception as e:
            logging.error("GPIO Digital Interrupt Insertion Failed: " + str(e))
            pass

    def InsertRotary(self, pinA, pinB, handler):
        try:
            logging.debug(f"GPIO - Inserting Rotary Interrupt for Pins: {pinA}, {pinB}...")
            self.rotaryInputs[pinA] = (gpiozero.Button(pinA), gpiozero.Button(pinB))
            self.rotaryInputs[pinA][0].when_released = lambda x = pinA: self.RotaryInterrupt(x)
            self.rotaryInterrupts[pinA] = handler
        except Exception as e:
            logging.error("GPIO Rotary Interrupt Insertion Failed: " + str(e))
            pass

    def InsertRgb(self, pinR, pinG, pinB):
        try:
            logging.debug(f"GPIO - Inserting RGB LED with pins {pinR} {pinG} {pinB}...")
            self.rgbOutputs[pinR] = (gpiozero.LED(pinR), gpiozero.LED(pinG), gpiozero.LED(pinB))
            self.rgbColors[pinR]  = (False,False,False)
            self.rgbPeriods[pinR] = -1
            self.rgbTimers[pinR]  = 0
            self.rgbStates[pinR]  = False
        except Exception as e:
            logging.error("GPIO RGB Insertion Failed: " + str(e))

    def InsertService(self, service):
        self.services.append(service)
        
    def RotaryInterrupt(self, pinA):
        try:
            if(self.rotaryInputs[pinA][1].value == 1):
                # A is Rising while B is High (Forwards)
                self.rotaryInterrupts[pinA](1)
            if(self.rotaryInputs[pinA][1].value == 0):
                # A is Rising while B is Low (Backwards)
                self.rotaryInterrupts[pinA](-1)
        except Exception as e:
            logging.error("Rotary Interrupt Scan Error: " + str(e))

    def SetRgb(self, pin, colorR, colorG, colorB, period):
        self.rgbColors[pin] = (colorR, colorG, colorB)

        if(period <= 0):
            period = -1
            self.rgbStates[pin] = True
            for i in range(3):
                if(self.rgbColors[pin][i] == True):
                    self.rgbOutputs[pin][i].off()
                else:
                    self.rgbOutputs[pin][i].on()

        self.rgbPeriods[pin] = period

    def ToggleRgb(self, pin):
        if(self.rgbStates[pin] == True):
            self.rgbStates[pin] = False

            for i in range(3):
                self.rgbOutputs[pin][i].on()
        else:
            self.rgbStates[pin] = True

            for i in range(3):
                if(self.rgbColors[pin][i] == True):
                    self.rgbOutputs[pin][i].off()
                else:
                    self.rgbOutputs[pin][i].on()

    def ScanInterrupts(self):
        try:
            while(self.online):
                # LED Outputs
                for pin, led in self.rgbOutputs.items():
                    if(self.rgbPeriods[pin] == -1): continue
                    if(self.rgbTimers[pin] >= self.rgbPeriods[pin]):
                        self.ToggleRgb(pin)
                        self.rgbTimers[pin] = 0
                    else:
                        self.rgbTimers[pin] += config.GPIO_TIME_PERIOD

                for service in self.services:
                    service()

                time.sleep(config.GPIO_TIME_PERIOD)
        except Exception as e:
            logging.error("Interrupt scan error: " + str(e))
            pass

    def Kill(self):
        self.online = False