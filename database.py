import cantools
import os

import logging

import enum
from enum import Enum

import config

import can_interface

# Enumerables -----------------------------------------------------------------------------------------------------------------
class InputTypes(Enum):                              # Input Type Enumerable
    BUTTON_WHEEL_LEFT  = 0,                          # - Left Button of Steering Wheel
    BUTTON_WHEEL_RIGHT = 1,                          # - Right Button of Steering Wheel
    BUTTON_DASH_LEFT   = 2,                          # - Left Button of Dashboard
    BUTTON_DASH_RIGHT  = 3                           # - Right Button of Dashboard

def Setup():
    try:
        parentPath = os.path.dirname(__file__)
        databasePath    = os.path.join(parentPath, config.CAN_DATABASE_PATH)
        databaseBmsPath = os.path.join(parentPath, config.CAN_BMS_DATABASE_PATH)

        db = Database(databasePath)
        db.add_dbc_file(databaseBmsPath)

        db.populateDictionary()

        can_interface.CalculateInverterStats(db)
        can_interface.CalculateBmsStats(db)
        can_interface.CalculateMotorStats(db)

        return db
    except Exception as e:
        logging.error("Database Setup Failure: " + str(e))
        raise

class Database(dict):
    def __init__(self, path):
        super().__init__()
        self.__dict__ = self
        self.overrides = dict()

        self.db = cantools.db.load_file(path)

    def populateDictionary(self):
        messages = self.db.messages
        for message in messages:
            signals = message.signals
            for signal in signals:
                self[signal.name] = None

    def decode_message(self, id, data):
        try:
            messageData = self.db.decode_message(id, data)
        
            for signal in messageData:
                self[signal] = messageData[signal]
        except Exception as e:
            logging.error("Database Message Decoding Error. " + str(e))

    def add_dbc_file(self, filepath):
        try:
            self.db.add_dbc_file(filepath)
        except Exception as e:
            logging.error("Database Appending Error. " + str(e))

# # Database --------------------------------------------------------------------------------------------------------------------
# # Author: Cole Barach
# # Date Created: 22.09.28
# # Date Updated: 23.01.30
# #   This module is used for interfacing elements of the application. Any data that must be shared between different objects
# #   may be stored in here as to simplify references.

# # Libraries -------------------------------------------------------------------------------------------------------------------
# import enum
# from enum import Enum

# # Functions -------------------------------------------------------------------------------------------------------------------
# def Setup():
#     return CarData()

# # Objects ---------------------------------------------------------------------------------------------------------------------
# class CarData():
#     # Communications ----------------------------------------------------------------------------------------------------------
#     ecuCanActive           = False                       # Activity of the ECU CAN
#     acanCanActive          = False                       # Activity of the ACAN CAN
#     bmsCanActive           = False                       # Activity of the BMS CAN
#     inverterCanActive      = False                       # Activity of the Inverter CAN

#     ecuCanTimeout          = None                        # Time of last ECU CAN message received 
#     acanCanTimeout         = None                        # Time of last ACAN CAN message received
#     bmsCanTimeout          = None                        # Time of last BMS CAN message received
#     inverterCanTimeout     = None                        # Time of last Inverter CAN message received

#     time                   = 0

#     # Pedal Info --------------------------------------------------------------------------------------------------------------
#     apps1                  = None                        # Real APPS-1 Value from ACAN
#     apps2                  = None                        # Real APPS-2 Value from ACAN
#     brake1                 = None                        # Real Brake-1 Value from ACAN
#     brake2                 = None                        # Real Brake-2 Value from ACAN

#     apps1Percent           = None                        # APPS-1 Percentage from ECU
#     apps2Percent           = None                        # APPS-2 Percentage from ECU
#     brake1Percent          = None                        # Brake-1 Percentage from ECU
#     brake2Percent          = None                        # Brake-2 Percentage from ECU

#     apps1Min               = None                        # APPS-1 Calibration Minimum from Dash
#     apps1Max               = None                        # APPS-1 Calibration Maximum from Dash
#     apps2Min               = None                        # APPS-2 Calibration Minimum from Dash
#     apps2Max               = None                        # APPS-2 Calibration Maximum from Dash

#     brake1Min              = None                        # Brake-1 Calibration Minimum from Dash
#     brake1Max              = None                        # Brake-1 Calibration Maximum from Dash
#     brake2RawMin           = None                        # Brake-2 Calibration Minimum from Dash
#     brake2RawMax           = None                        # Brake-2 Calibration Maximum from Dash

#     accelerating           = None                        # Acceleration State (True => Accelerating)
#     braking                = None                        # Braking State (True => Braking)

#     # ECU Info ----------------------------------------------------------------------------------------------------------------
#     readyToDrive           = None                        # Car is Ready to Drive
#     highVoltageEnabled     = None                        # High Voltage is Enabled
#     regenEnabled           = None                        # Regen Braking Enabled
#     torquePlausible        = None                        # ECU is Requesting Torque
#     pedal100msPlausible    = None                        # Pedal Input is 100ms Plausible
#     pedalsPlausible        = None                        # Pedal Input is Plausible
#     appsPlausible          = None                        # APPS Input is Plausible
#     appsCalibPlausible     = None                        # APPS Calibration is Plausible
#     brakePlausible         = None                        # Brake Input is Plausible
#     brakeCalibPlausible    = None                        # Brake Calibration is Plausible
#     apps25_5Plausible      = None                        # APPS 25/5 Rule is Plausible
#     stateAccelerating      = None                        # Car is Accelerating
#     stateBraking           = None                        # Car is Braking
    
#     # Acumulator Data ---------------------------------------------------------------------------------------------------------
#     stateOfCharge          = None                        # State of Charge
#     packVoltage            = None                        # Total Voltage of the Accumulator
#     packCurrent            = None                        # Current of the Accumulator
#     cellVoltages           = [None]*90                   # Accumulator Cell Voltages
#     cellBalancings         = [None]*90                   # Accumulator Cell Balancings
#     cellVoltageMax         = None                        # Accumulator Highest Cell Voltage
#     cellVoltageMin         = None                        # Accumulator Lowest Cell Voltage
#     cellDeltaMax           = None                        # Accumulator Max Delta Voltage
#     cellDeltaMean          = None                        # Accumulator Average Delta Voltage
#     packTemperatures       = [None]*45                   # Accumulator Pack Temperatures
#     packTemperatureMax     = None                        # Highest Pack Temperature
#     packTemperatureMean    = None                        # Average Pack Temperature
#     segmentSenseLines      = [None]*5                    # Accumulator Segment Sense Line Statuses

#     # Inverter Data -----------------------------------------------------------------------------------------------------------
#     inverterTempGdb        = None                        # Temperature of the Inverter GDB
#     inverterTempModuleA    = None                        # Temperature of the Inverter Module A
#     inverterTempModuleB    = None                        # Temperature of the Inverter Module B
#     inverterTempModuleC    = None                        # Temperature of the Inverter Module C
#     inverterTempCb         = None                        # Temperature of the Inverter CB
#     inverterTempMean       = None                        # Average Temperature of the Inverter
#     inverterTempMax        = None                        # Maximum Temperature of the Inverter

#     # Motor Data --------------------------------------------------------------------------------------------------------------
#     motorRpm               = None                        # RPM of the Motor
#     motorSpeedMph          = None                        # Speed of the Vehicle
#     torquePercentageMax    = None                        # Maximum Torque Percentage from ECU
#     torquePercentageRegen  = None                        # Maximum Regen Percentage from ECU
#     motorTemperature       = None                        # Temperature of the Motor

#     # Errors ------------------------------------------------------------------------------------------------------------------
#     error25_5Implausible   = None                        # 25/5 APPS Implausibility
#     errorInverterFault     = None                        # Inverter Fault Detected
#     errorAcanImplausible   = None                        # ACAN Value Implausibility
#     error100MsImplausible  = None                        # 100ms APPS Implausibility
#     errorBmsTempFault      = None                        # BMS Temperature Fault
#     errorBmsVoltageFault   = None                        # BMS Voltage Fault
#     errorBmsSelfTestFault  = None                        # BMS Self Test Fault
#     errorBmsSenseLineFault = None                        # BMS Sense Line Fault