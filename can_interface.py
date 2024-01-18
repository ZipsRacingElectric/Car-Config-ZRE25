# CAN Interface ---------------------------------------------------------------------------------------------------------------
# Author: Cole Barach
# Date Created: 22.09.28
# Date Updated: 23.01.30
#   This module acts as the manager for anything relating to the CAN communications protocol.

# Libraries
import logging

import time
import sys

import threading
from threading import Thread

# Includes
import config

# Objects ---------------------------------------------------------------------------------------------------------------------
# CAN Interface
# - Interface Object for CAN Libraries
# - Objects inheriting from this may be used a CAN interface by the application
class CanInterface():
    def __init__(self, database, messageHandler=None, timingFunction=None, timingPeriod=None):
        logging.debug("CAN - Initializing...")
        self.database = database
        self.channels = []
        self.messageHandler = messageHandler
        self.timingFunction = timingFunction
        self.timingPeriod   = timingPeriod
        self.InitializeTimeThread()
    
    # Main Loop
    def Begin(self):
        logging.debug("CAN - Beginning...")
        self.online = True
        self.BeginTimeThread()

    def Kill(self):
        logging.debug("CAN - Terminating...")
        self.online = False

    # Messages
    def Transmit(self, id, data, channel):
        self.Receive(id, data)

    def Receive(self, id, data):
        self.messageHandler(self.database, id, data)

    # Timing
    def InitializeTimeThread(self):
        if(self.timingFunction == None):
            self.timeThread = None
            return
        self.timeThread = Thread(target=self.TimeThread)

    def BeginTimeThread(self):
        if(self.timeThread == None): return
        self.timeThreadOnline = True
        self.timeThread.start()

    def TimeThread(self):
        if(self.timeThread == None): return
        while(self.online):
            self.timingFunction(self.database)
            time.sleep(self.timingPeriod)

# Functions -------------------------------------------------------------------------------------------------------------------
# - Call this function to get an initialized CAN Interface Object
def Setup(database):
    try:
        database["Time"] = None
        database["ECU_CAN_Timeout"]      = None
        database["ACAN_CAN_Timeout"]     = None
        database["Inverter_CAN_Timeout"] = None
        database["BMS_CAN_Timeout"]      = None
        database["ECU_CAN_Active"]       = None
        database["ACAN_CAN_Active"]      = None
        database["Inverter_CAN_Active"]  = None
        database["BMS_CAN_Active"]       = None
        SetTimeouts(database)

        if(config.CAN_LIBRARY_TYPE == config.CAN_EMULATE):
            try:
                logging.debug("CAN - Using CAN Emulation.")
                return CanInterface(database, messageHandler=HandleMessage, timingFunction=None, timingPeriod=config.CAN_TIME_PERIOD)
            except Exception as e:
                logging.error("Failed to Initialize Emulated CAN: " + str(e))

        if(config.CAN_LIBRARY_TYPE == config.CAN_CANLIB):
            try:
                import lib_canlib
                library = lib_canlib.Main(database, messageHandler=HandleMessage, timingFunction=SetTimeouts, timingPeriod=config.CAN_TIME_PERIOD)
                library.OpenChannel(config.CAN_BITRATE, 0)
                # library.OpenChannel(config.CAN_BITRATE, 1)
                return library
            except Exception as e:
                logging.error("Failed to Initialize CANLIB Library: " + str(e))
        
        if(config.CAN_LIBRARY_TYPE == config.CAN_INNOMAKER):
            try:
                if(sys.platform == "win32"):
                    import lib_innomaker_win
                    library = lib_innomaker_win.Main(database, messageHandler=HandleMessage, timingFunction=SetTimeouts, timingPeriod=config.CAN_TIME_PERIOD)
                    library.OpenChannel(config.CAN_BITRATE, 0)
                    # library.OpenChannel(config.CAN_BITRATE, 1)
                    return library

                if(sys.platform == "linux"):
                    import lib_innomaker_linux
                    library = lib_innomaker_linux.Main(database, messageHandler=HandleMessage, timingFunction=SetTimeouts, timingPeriod=config.CAN_TIME_PERIOD)
                    library.OpenChannel(config.CAN_BITRATE, 0)
                    # library.OpenChannel(config.CAN_BITRATE, 1)
                    return library
            except Exception as e:
                logging.error("Failed to Initialize INNOMAKER Library: " + str(e))
        
        logging.error("Exception: No CAN Library Type configured.")
        raise
    except Exception as e:
        logging.error("Failed to Setup CAN Interface: " + str(e))
        raise

# Message Handling ------------------------------------------------------------------------------------------------------------

# Handle Message
# - Call to Interpret a CAN Message
# - Updates car_data with Appropriate Values  
def HandleMessage(database, id, data):
    if(id == config.CAN_ID_INPUT_PEDALS):
        ClearTimeoutEcu(database)
        database.decode_message(id, data)
        return

    if(id == config.CAN_ID_DATA_TEMP_1): 
        ClearTimeoutInverter(database)
        database.decode_message(id, data)
        return

    if(id == config.CAN_ID_DATA_TEMP_2):
        ClearTimeoutInverter(database)
        database.decode_message(id, data)
        return

    if(id == config.CAN_ID_DATA_TEMP_3):
        ClearTimeoutInverter(database)
        database.decode_message(id, data)
        return

    if(id == config.CAN_ID_DATA_MOTOR):
        ClearTimeoutInverter(database)
        CalculateMotorStats(database)
        database.decode_message(id, data)
        return

    if(id == config.CAN_ID_DATA_PEDALS):
        ClearTimeoutEcu(database)
        database.decode_message(id, data)
        return

    if(id == config.CAN_ID_STATUS_ECU):
        ClearTimeoutEcu(database)
        database.decode_message(id, data)
        return

    if(id == config.CAN_ID_STATUS_BMS):
        ClearTimeoutBms(database)
        database.decode_message(id, data)
        return
    
    for index in range(config.CAN_ID_CELL_VOLTAGES_END - config.CAN_ID_CELL_VOLTAGES_START + 1):
        idIndex = config.CAN_ID_CELL_VOLTAGES_START + index
        if(id == idIndex):
            ClearTimeoutBms(database)
            database.decode_message(id, data)
            CalculateBmsStats(database)
            return
    
    for index in range(config.CAN_ID_CELL_BALANCINGS_END - config.CAN_ID_CELL_BALANCINGS_START + 1):
        idIndex = config.CAN_ID_CELL_BALANCINGS_START + index
        if(id == idIndex):
            ClearTimeoutBms(database)
            database.decode_message(id, data)
            CalculateBmsStats(database)
            return

    for index in range(config.CAN_ID_PACK_TEMPERATURES_END - config.CAN_ID_PACK_TEMPERATURES_START + 1):
        idIndex = config.CAN_ID_PACK_TEMPERATURES_START + index
        if(id == idIndex):
            ClearTimeoutBms(database)
            database.decode_message(id, data)
            CalculateBmsStats(database)
            return

    database.decode_message(id, data)

# DEPRICATED ------------------------------------------------------------------------------------------------------------------

# # Message 0x005 - Pedal Data from ECU
# def HandleInputPedals(database, data):
#     # Bytes 0 & 1
#     database.apps1  = data[0] | (data[1] << 8)
#     # Bytes 2 & 3
#     database.apps2  = data[2] | (data[3] << 8)
#     # Bytes 4 & 5
#     database.brake1 = data[4] | (data[5] << 8)
#     # Bytes 6 & 7
#     database.brake2 = data[6] | (data[7] << 8)
#     # Timeout
#     ClearTimeoutAcan(database)

# # Message 0x0A0 - Temperature Data from Inverter 
# def HandleDataTemperature1(database, data):
#     # Bytes 0 & 1
#     database.inverterTempModuleA = (data[1] >> 8 | data[0]) * config.INVERTER_TEMP_SCALE
#     # Bytes 2 & 3
#     database.inverterTempModuleB = (data[3] >> 8 | data[2]) * config.INVERTER_TEMP_SCALE
#     # Bytes 4 & 5
#     database.inverterTempModuleC = (data[5] >> 8 | data[4]) * config.INVERTER_TEMP_SCALE
#     # Bytes 6 & 7
#     database.inverterTempGdb     = (data[7] >> 8 | data[6]) * config.INVERTER_TEMP_SCALE
#     # Timeout & Calculations
#     CalculateInverterStats(database)
#     ClearTimeoutInverter(database)

# # Message 0x0A1 - Temperature Data from Inverter
# def HandleDataTemperature2(database, data):
#     # Bytes 0 & 1
#     database.inverterTempCb = (data[1] >> 8 | data[0]) * config.INVERTER_TEMP_SCALE
#     # Timeout
#     ClearTimeoutInverter(database)

# # Message 0x0A2 - Temperature Data from Inverter
# def HandleDataTemperature3Torque(database, data):
#     # Bytes 4 & 5
#     database.motorTemperature = (data[5] >> 8 | data[4]) * config.INVERTER_TEMP_SCALE
#     # Timeout
#     ClearTimeoutInverter(database)

# # Message 0x0A5 - Motor Data from Inverter
# def HandleDataMotor(database, data):
#     # Bytes 2 & 3
#     database.motorRpm      = InterpretSignedNBitInt(data[2] | (data[3] << 8)) * config.INVERTER_RPM_SCALE
#     database.motorSpeedMph = int(abs(RpmToMph(database.motorRpm)))
#     # Timeout
#     ClearTimeoutInverter(database)

# # Message 0x701 - Pedal Data from ECU
# def HandleDataPedals(database, data):
#     # Byte 0
#     database.apps1Percent  = InterpretSignedNBitInt((data[0] | (data[1] << 8))) * config.APPS_1_PERCENT_SCALE
#     # Byte 1
#     database.apps2Percent  = InterpretSignedNBitInt((data[2] | (data[3] << 8))) * config.APPS_2_PERCENT_SCALE
#     # Byte 2
#     database.brake1Percent = InterpretSignedNBitInt((data[4] | (data[5] << 8))) * config.BRAKE_1_PERCENT_SCALE
#     # Byte 3
#     database.brake2Percent = InterpretSignedNBitInt((data[6] | (data[7] << 8))) * config.BRAKE_2_PERCENT_SCALE
#     # Timeout
#     ClearTimeoutEcu(database)

# # Message 0x703 - Status Message from ECU
# def HandleStatusEcu(database, data):
#     # Byte 0
#     database.readyToDrive           = bool((data[0] & 0b00000001) >> 0)
#     database.highVoltageEnabled     = bool((data[0] & 0b00000010) >> 1)
#     database.regenEnabled           = bool((data[0] & 0b00000100) >> 2)
#     # Byte 1
#     database.torquePlausible        = bool((data[1] & 0b00000001) >> 0)
#     database.pedal100msPlausible    = bool((data[1] & 0b00000010) >> 1)
#     database.pedalsPlausible        = bool((data[1] & 0b00000100) >> 2)
#     database.appsPlausible          = bool((data[1] & 0b00001000) >> 3)
#     database.appsCalibPlausible     = bool((data[1] & 0b00010000) >> 4)
#     database.brakePlausible         = bool((data[1] & 0b00100000) >> 5)
#     database.brakeCalibPlausible    = bool((data[1] & 0b01000000) >> 6)
#     database.apps25_5Plausible      = bool((data[1] & 0b10000000) >> 7)
#     # Byte 2
#     database.stateAccelerating      = bool((data[2] & 0b00000001) >> 0)
#     database.stateBraking           = bool((data[2] & 0b00000010) >> 1)

#     # Timeout
#     ClearTimeoutEcu(database)

# # Messages 0x401 - 0x417 - Cell Voltages from BMS
# def HandleCellVoltages(database, data, id):
#     cellOffset = (id - config.CAN_ID_CELL_VOLTAGES_START) * 4
#     # Bytes 0 & 1
#     # BMS uses Motorola Byte Order, Lo Byte is 1, Hi Byte is 0
#     database.cellVoltages[cellOffset]   = (data[1] | (data[0] << 8)) * config.CELL_VOLTAGE_SCALE
#     # Bytes 2 & 3
#     database.cellVoltages[cellOffset+1] = (data[3] | (data[2] << 8)) * config.CELL_VOLTAGE_SCALE
    
#     # Last message only contains 4 bytes
#     if(id == config.CAN_ID_CELL_VOLTAGES_END): return
    
#     # Bytes 4 & 5
#     database.cellVoltages[cellOffset+2] = (data[5] | (data[4] << 8)) * config.CELL_VOLTAGE_SCALE
#     # Bytes 6 & 7
#     database.cellVoltages[cellOffset+3] = (data[7] | (data[6] << 8)) * config.CELL_VOLTAGE_SCALE
    
#     # Timeout
#     ClearTimeoutBms(database)

# # Messages 0x418 - 0x41A - Cell Balancings from BMS
# def HandleCellBalancings(database, data, id):
#     cellOffset = (id - config.CAN_ID_CELL_BALANCINGS_START) * 36
#     # Byte 0
#     database.cellBalancings[cellOffset]    = bool((data[0] >> 0) & 0b1)
#     database.cellBalancings[cellOffset+1]  = bool((data[0] >> 1) & 0b1)
#     database.cellBalancings[cellOffset+2]  = bool((data[0] >> 2) & 0b1)
#     database.cellBalancings[cellOffset+3]  = bool((data[0] >> 3) & 0b1)
#     database.cellBalancings[cellOffset+4]  = bool((data[0] >> 4) & 0b1)
#     database.cellBalancings[cellOffset+5]  = bool((data[0] >> 5) & 0b1)
#     database.cellBalancings[cellOffset+6]  = bool((data[0] >> 6) & 0b1)
#     database.cellBalancings[cellOffset+7]  = bool((data[0] >> 7) & 0b1)
#     # Byte 1
#     database.cellBalancings[cellOffset+8]  = bool((data[1] >> 0) & 0b1)
#     database.cellBalancings[cellOffset+9]  = bool((data[1] >> 1) & 0b1)
#     database.cellBalancings[cellOffset+10] = bool((data[1] >> 2) & 0b1)
#     database.cellBalancings[cellOffset+11] = bool((data[1] >> 3) & 0b1)
#     database.cellBalancings[cellOffset+12] = bool((data[1] >> 4) & 0b1)
#     database.cellBalancings[cellOffset+13] = bool((data[1] >> 5) & 0b1)
#     database.cellBalancings[cellOffset+14] = bool((data[1] >> 6) & 0b1)
#     database.cellBalancings[cellOffset+15] = bool((data[1] >> 7) & 0b1)
#     # Byte 2
#     database.cellBalancings[cellOffset+16] = bool((data[2] >> 0) & 0b1)
#     database.cellBalancings[cellOffset+17] = bool((data[2] >> 1) & 0b1)

#     # Last message only contains 3 bytes
#     if(id == config.CAN_ID_CELL_BALANCINGS_END): return
    
#     # Byte 3
#     database.cellBalancings[cellOffset+18] = bool((data[3] >> 0) & 0b1)
#     database.cellBalancings[cellOffset+19] = bool((data[3] >> 1) & 0b1)
#     database.cellBalancings[cellOffset+20] = bool((data[3] >> 2) & 0b1)
#     database.cellBalancings[cellOffset+21] = bool((data[3] >> 3) & 0b1)
#     database.cellBalancings[cellOffset+22] = bool((data[3] >> 4) & 0b1)
#     database.cellBalancings[cellOffset+23] = bool((data[3] >> 5) & 0b1)
#     database.cellBalancings[cellOffset+24] = bool((data[3] >> 6) & 0b1)
#     database.cellBalancings[cellOffset+25] = bool((data[3] >> 7) & 0b1)
#     # Byte 4
#     database.cellBalancings[cellOffset+26] = bool((data[4] >> 0) & 0b1)
#     database.cellBalancings[cellOffset+27] = bool((data[4] >> 1) & 0b1)
#     database.cellBalancings[cellOffset+28] = bool((data[4] >> 2) & 0b1)
#     database.cellBalancings[cellOffset+29] = bool((data[4] >> 3) & 0b1)
#     database.cellBalancings[cellOffset+30] = bool((data[4] >> 4) & 0b1)
#     database.cellBalancings[cellOffset+31] = bool((data[4] >> 5) & 0b1)
#     database.cellBalancings[cellOffset+32] = bool((data[4] >> 6) & 0b1)
#     database.cellBalancings[cellOffset+33] = bool((data[4] >> 7) & 0b1)
#     # Byte 5
#     database.cellBalancings[cellOffset+34] = bool((data[5] >> 0) & 0b1)
#     database.cellBalancings[cellOffset+35] = bool((data[5] >> 1) & 0b1)
    
#     # Timeout
#     ClearTimeoutBms(database)

# # Messages 0x41B - 0x426 - Pack Temperatures from BMS
# def HandlePackTemperatures(database, data, id):
#     packOffset = (id - config.CAN_ID_PACK_TEMPERATURES_START) * 4
    
#     # Bytes 0 & 1
#     # BMS uses Motorola Byte Order, Lo Byte is 1, Hi Byte is 0
#     database.packTemperatures[packOffset]   = (data[1] | (data[0] << 8)) * config.PACK_TEMPERATURE_SCALE + config.PACK_TEMPERATURE_OFFSET
    
#     # Last message only contains 2 bytes
#     if(id == config.CAN_ID_PACK_TEMPERATURES_END): return
    
#     # Bytes 2 & 3
#     database.packTemperatures[packOffset+1] = (data[3] | (data[2] << 8)) * config.PACK_TEMPERATURE_SCALE + config.PACK_TEMPERATURE_OFFSET
#     # Bytes 4 & 5
#     database.packTemperatures[packOffset+2] = (data[5] | (data[4] << 8)) * config.PACK_TEMPERATURE_SCALE + config.PACK_TEMPERATURE_OFFSET
#     # Bytes 6 & 7
#     database.packTemperatures[packOffset+3] = (data[7] | (data[6] << 8)) * config.PACK_TEMPERATURE_SCALE + config.PACK_TEMPERATURE_OFFSET
    
#     # Timeout
#     ClearTimeoutBms(database)

# # Message 0x440 - Status Message from BMS
# def HandleStatusBms(database, data):
#     # Bytes 0 & 1
#     database.stateOfCharge          = (data[0] | (data[1] << 8)) * config.STATE_OF_CHARGE_SCALE
#     # Bytes 4 & 5
#     database.packCurrent            = InterpretSignedNBitInt(data[4] | (data[5] << 8), 16) * config.PACK_CURRENT_LO_SCALE
#     # Byte 6
#     database.errorBmsTempFault      = bool((data[6] >> 0) & 0b1)
#     database.errorBmsVoltageFault   = bool((data[6] >> 1) & 0b1)
#     database.errorBmsSelfTestFault  = bool((data[6] >> 2) & 0b1)
#     database.errorBmsSenseLineFault = bool((data[6] >> 4) & 0b1)
#     # Timeout
#     CalculateBmsStats(database) 

# Data Extrapolation ----------------------------------------------------------------------------------------------------------
def CalculateInverterStats(database):
    try:
        database["Temperature_Inverter_Mean"] = None
        database["Temperature_Inverter_Max"]  = None

        tempCount = 0
        for i in range(4):
            temp = None
            if(i == 0):
                temp = database["Temperature_Inverter_Module_A"]
            elif(i == 1):
                temp = database["Temperature_Inverter_Module_B"]
            elif(i == 2):
                temp = database["Temperature_Inverter_Module_C"]
            elif(i == 3):
                temp = database["Temperature_Inverter_GDB"]

            if(temp == None): continue
            if(database["Temperature_Inverter_Max"]  == None): database["Temperature_Inverter_Max"]  = temp
            if(database["Temperature_Inverter_Mean"] == None): database["Temperature_Inverter_Mean"] = 0
            database["Temperature_Inverter_Mean"] += temp
            tempCount += 1

        if(tempCount != 0): database["Temperature_Inverter_Mean"] /= tempCount
    except Exception as e:
        logging.error("Failed to Calculate Inverter Stats: " + str(e))

def CalculateMotorStats(database):
    try:
        database["Motor_Speed_MPH"] = None
        if(database["Motor_Speed"] != None): database["Motor_Speed_MPH"] = int(abs(RpmToMph(database["Motor_Speed"])))
    except Exception as e:
        logging.error("Failed to Calculate Motor Stats: " + str(e))

def CalculateBmsStats(database):
    try:
        # Voltages
        database["Pack_Voltage"]    = None
        database["Cell_Voltage_Min"] = None
        database["Cell_Voltage_Max"] = None

        for index in range(54):
            strIndex = str(index).zfill(2)
            voltage = database[f"Voltage_Cell_{strIndex}"]

            if(voltage == None): continue

            if(database["Pack_Voltage"] == None): database["Pack_Voltage"] = 0
            
            database["Pack_Voltage"] += voltage
            
            if(database["Cell_Voltage_Min"] == None or voltage < database["Cell_Voltage_Min"]):
                database["Cell_Voltage_Min"] = voltage
            if(database["Cell_Voltage_Max"] == None or voltage > database["Cell_Voltage_Max"]):
                database["Cell_Voltage_Max"] = voltage

        # Deltas
        database["Cell_Delta_Max"]  = None
        database["Cell_Delta_Mean"] = None
        deltaCount = 0
        for index in range(54):
            strIndex = str(index).zfill(2)
            voltage = database[f"Voltage_Cell_{strIndex}"]

            if(voltage == None): continue

            delta = voltage - database["Cell_Voltage_Min"]
            if(database["Cell_Delta_Mean"] == None): database["Cell_Delta_Mean"] = 0
            if(database["Cell_Delta_Max"]  == None or delta > database["Cell_Delta_Max"]):
                database["Cell_Delta_Max"] = delta
            database["Cell_Delta_Mean"] += delta
            deltaCount += 1
        if(deltaCount != 0): database["Cell_Delta_Mean"] /= deltaCount

        # Temperatures
        database["Pack_Temperature_Max"]  = None
        database["Pack_Temperature_Mean"] = None
        tempCount = 0
        for index in range(27):
            if(index == 3): continue

            strIndex = str(index).zfill(2)
            temperature = database[f"Temperature_Sensor_{strIndex}"]

            if(temperature == None): continue
            
            if(database["Pack_Temperature_Mean"] == None): database["Pack_Temperature_Mean"] = 0
            if(database["Pack_Temperature_Max"]  == None or temperature > database["Pack_Temperature_Max"]):
                database["Pack_Temperature_Max"] = temperature
            database["Pack_Temperature_Mean"] += temperature
            tempCount += 1
        if(tempCount != 0): database["Pack_Temperature_Mean"] /= tempCount
    except Exception as e:
        logging.error("Failed to Calculate BMS Stats: " + str(e))

# Message Timeouts ------------------------------------------------------------------------------------------------------------
def SetTimeouts(database):
    database["Time"] = time.time()
    if(database["ECU_CAN_Timeout"]      == None or database["Time"] > database["ECU_CAN_Timeout"]      + config.CAN_MESSAGE_TIMEOUT): database["ECU_CAN_Active"]      = False
    if(database["ACAN_CAN_Timeout"]     == None or database["Time"] > database["ACAN_CAN_Timeout"]     + config.CAN_MESSAGE_TIMEOUT): database["ACAN_CAN_Active"]     = False
    if(database["Inverter_CAN_Timeout"] == None or database["Time"] > database["Inverter_CAN_Timeout"] + config.CAN_MESSAGE_TIMEOUT): database["Inverter_CAN_Active"] = False
    if(database["BMS_CAN_Timeout"]      == None or database["Time"] > database["BMS_CAN_Timeout"]      + config.CAN_MESSAGE_TIMEOUT): database["BMS_CAN_Active"]      = False

def ClearTimeoutEcu(database):
    database["ECU_CAN_Timeout"] = time.time()
    database["ECU_CAN_Active"] = True

def ClearTimeoutAcan(database):
    database["ACAN_CAN_Timeout"] = time.time()
    database["ACAN_CAN_Active"] = True

def ClearTimeoutInverter(database):
    database["Inverter_CAN_Timeout"] = time.time()
    database["Inverter_CAN_Active"] = True

def ClearTimeoutBms(database):
    database["BMS_CAN_Timeout"] = time.time()
    database["BMS_CAN_Active"] = True

# Data Interpretation ---------------------------------------------------------------------------------------------------------
def InterpretSignedNBitInt(value, bitCount=16):
    if(value > 2 ** (bitCount-1)): value -= 2 ** bitCount
    return value

def RpmToMph(rotationsPerMinute):
    radiansPerMinute = rotationsPerMinute * config.RADIANS_PER_ROTATION * config.MOTOR_TEETH_COUNT / config.SPROCKET_TEETH_COUNT
    speedMph = radiansPerMinute * config.TIRE_RADIUS_INCHES * config.MINUTES_PER_HOUR / (config.INCHES_PER_FOOT * config.FEET_PER_MILE)
    return speedMph

# Message Transmitting --------------------------------------------------------------------------------------------------------
def SendMessage(transmitter, id, data, channel=0):
    logging.debug(f"CAN - Sending Message ID: {hex(id)} [{hex(data[0])}, {hex(data[1])}, {hex(data[2])}, {hex(data[3])}, {hex(data[4])}, {hex(data[5])}, {hex(data[6])}, {hex(data[7])}]")
    transmitter.Transmit(id, data, 0)
    transmitter.Transmit(id, data, 1)

# Message 0x004
def SendCommandDriveStart(transmitter, commandEnterDrive):
    message = [0,0,0,0,0,0,0,0]
    
    message[0] = commandEnterDrive & 0b1
    
    SendMessage(transmitter, config.CAN_ID_COMMAND_DRIVE_START, message)

# Message 0x010
def SendCommandDriveConfiguration(transmitter, database):
    message = [0,0,0,0,0,0,0,0]

    message[0] = (int(database["Torque_Config_Limit"]        * 10))      & 0xFF
    message[1] = (int(database["Torque_Config_Limit"]        * 10) >> 8) & 0xFF
    message[2] = (int(database["Torque_Config_Limit_Regen"]  * 10))      & 0xFF
    message[3] = (int(database["Torque_Config_Limit_Regen"]  * 10) >> 8) & 0xFF
    message[4] = database["State_Regen_Config_Enabled"] & 0b1

    SendMessage(transmitter, config.CAN_ID_COMMAND_TORQUE_LIMIT, message)

# Message 0x533
def SendCalibrateAppsRange(transmitter, apps1MinValue, apps1MaxValue, apps2MinValue, apps2MaxValue):
    message = [0,0,0,0,0,0,0,0]

    message[0] = (apps1MinValue)      & 0xFF
    message[1] = (apps1MinValue >> 8) & 0xFF
    message[2] = (apps1MaxValue)      & 0xFF
    message[3] = (apps1MaxValue >> 8) & 0xFF
    message[4] = (apps2MinValue)      & 0xFF
    message[5] = (apps2MinValue >> 8) & 0xFF
    message[6] = (apps2MaxValue)      & 0xFF
    message[7] = (apps2MaxValue >> 8) & 0xFF
    
    SendMessage(transmitter, config.CAN_ID_CALIBRATE_APPS_RANGE, message)

# Message 0x534
def SendCalibrateBrakeRange(transmitter, brake1MinValue, brake1MaxValue, brake2MinValue, brake2MaxValue):
    message = [0,0,0,0,0,0,0,0]

    message[0] = (brake1MinValue)      & 0xFF
    message[1] = (brake1MinValue >> 8) & 0xFF
    message[2] = (brake1MaxValue)      & 0xFF
    message[3] = (brake1MaxValue >> 8) & 0xFF
    message[4] = (brake2MinValue)      & 0xFF
    message[5] = (brake2MinValue >> 8) & 0xFF
    message[6] = (brake2MaxValue)      & 0xFF
    message[7] = (brake2MaxValue >> 8) & 0xFF
    
    SendMessage(transmitter, config.CAN_ID_CALIBRATE_BRAKE_RANGE, message)

# Message 0x005
def SendInputPedals(transmitter, apps1, apps2, brake1, brake2):
    message = [0,0,0,0,0,0,0,0]
    
    message[0] = (apps1)       & 0xFF
    message[1] = (apps1 >> 8)  & 0xFF
    message[2] = (apps2)       & 0xFF
    message[3] = (apps2 >> 8)  & 0xFF
    message[4] = (brake1)      & 0xFF
    message[5] = (brake1 >> 8) & 0xFF
    message[6] = (brake2)      & 0xFF
    message[7] = (brake2 >> 8) & 0xFF
    
    SendMessage(transmitter, config.CAN_ID_INPUT_PEDALS, message)

# Message 0x0A5
def SendDataMotor(transmitter, motorAngle, motorRpm, motorFrequency, motorDeltaResolver):
    message = [0,0,0,0,0,0,0,0]
    
    message[0] =  (motorAngle * 10)           & 0xFF
    message[1] = ((motorAngle * 10) >> 8)     & 0xFF
    message[2] =  (motorRpm)                  & 0xFF
    message[3] =  (motorRpm >> 8)             & 0xFF
    message[4] =  (motorFrequency * 10)       & 0xFF
    message[5] = ((motorFrequency * 10) >> 8) & 0xFF
    message[6] =  (motorDeltaResolver)        & 0xFF
    message[7] =  (motorDeltaResolver >> 8)   & 0xFF
    
    SendMessage(transmitter, config.CAN_ID_DATA_MOTOR, message)

# Message 0x701
def SendDataPedals(transmitter, apps1Percent, apps2Percent, brake1Percent, brake2Percent):
    message = [0,0,0,0,0,0,0,0]
    
    message[0] = int(apps1Percent / config.APPS_1_PERCENT_SCALE)        & 0xFF
    message[1] = int(apps1Percent / config.APPS_1_PERCENT_SCALE) >> 8   & 0xFF
    message[2] = int(apps2Percent / config.APPS_2_PERCENT_SCALE)        & 0xFF
    message[3] = int(apps2Percent / config.APPS_2_PERCENT_SCALE) >> 8   & 0xFF
    message[4] = int(brake1Percent / config.BRAKE_1_PERCENT_SCALE)      & 0xFF
    message[5] = int(brake1Percent / config.BRAKE_1_PERCENT_SCALE) >> 8 & 0xFF
    message[6] = int(brake2Percent / config.BRAKE_2_PERCENT_SCALE)      & 0xFF
    message[7] = int(brake2Percent / config.BRAKE_2_PERCENT_SCALE) >> 8 & 0xFF
    
    SendMessage(transmitter, config.CAN_ID_DATA_PEDALS, message)

# Message 0x703
def SendStatusEcu(transmitter, driveStateInput, acceleratingInput, brakingInput, drsInput, regenInput, is25_5Input, inverterInput,
                  acanInput, is100msInput, torquePercentInput, regenPercentInput, voltageLvInput, resistanceImdInput):
    message = [0,0,0,0,0,0,0,0]
    
    # Byte 0
    message[0] |= (driveStateInput)        & 0b00000011
    message[0] |= (acceleratingInput << 2) & 0b00000100
    message[0] |= (brakingInput      << 3) & 0b00001000
    message[0] |= (drsInput          << 4) & 0b00010000
    message[0] |= (regenInput        << 5) & 0b00100000
    # Byte 1
    message[1] |= (is25_5Input)            & 0b00000001
    message[1] |= (inverterInput     << 1) & 0b00000010
    message[1] |= (acanInput         << 2) & 0b00000100
    message[1] |= (is100msInput      << 3) & 0b00001000
    # Bytes 2 & 3
    message[2] = int(torquePercentInput) & 0xFF
    message[3] = int(regenPercentInput)  & 0xFF
    # Bytes 4 & 5
    message[4] = (int(voltageLvInput / config.LV_BATTERY_VOLTAGE_SCALE))      & 0xFF
    message[5] = (int(voltageLvInput / config.LV_BATTERY_VOLTAGE_SCALE) >> 8) & 0xFF
    # Bytes 6 & 7
    message[6] = (int(resistanceImdInput))      & 0xFF
    message[7] = (int(resistanceImdInput) >> 8) & 0xFF
    
    SendMessage(transmitter, config.CAN_ID_STATUS_ECU, message)
