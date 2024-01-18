# Configuration Data ----------------------------------------------------------------------------------------------------------
# Author: Cole Barach
# Date Created: 22.09.28
# Date Updated: 23.01.30
#   This module contains all configurable data for the execution of the app. Values stored in this file
#   may be referenced as needed throughout the program. These values should not change during runtime.

USE_GPIO = False

# GUI -------------------------------------------------------------------------------------------------------------------------
GUI_WIDTH                        = 800
GUI_HEIGHT                       = 480

GUI_FRAMERATE                    = 32

GUI_DASH_STYLE                   = "style_Dash.json"
GUI_DEBUG_STYLE                  = "style_Debug.json"

# Icons -----------------------------------------------------------------------------------------------------------------------
ICON_SPEED                       = "icons/Speed.png"
ICON_ENDURANCE                   = "icons/Endurance.png"
ICON_TESTING                     = "icons/Testing.png"
ICON_BMS                         = "icons/Bms.png"
ICON_CALIBRATION                 = "icons/Calibration.png"
ICON_DATABASE                    = "icons/Database.png"

ICON_SCALING                     = 0.33

# System ----------------------------------------------------------------------------------------------------------------------
TERMINAL_ID                      = "lxterminal"

# GPIO ------------------------------------------------------------------------------------------------------------------------
GPIO_TIME_PERIOD                 = 0.1

GPIO_BUTTON_WHEEL_L              = 3
GPIO_BUTTON_WHEEL_R              = 2
GPIO_BUTTON_REGEN                = 27

GPIO_ROT_TORQUE_PIN_A            = 17
GPIO_ROT_TORQUE_PIN_B            = 18
GPIO_ROT_REGEN_PIN_A             = 22
GPIO_ROT_REGEN_PIN_B             = 23

GPIO_RGB_PIN_R                   = 24
GPIO_RGB_PIN_G                   = 10
GPIO_RGB_PIN_B                   = 15

GPIO_ROT_TORQUE_SENSITIVITY      = 5
GPIO_ROT_REGEN_SENSITIVITY       = 1

# CAN Interface ---------------------------------------------------------------------------------------------------------------
CAN_CANLIB                       = "CANLIB"
CAN_INNOMAKER                    = "INNOMAKER"
CAN_EMULATE                      = "EMULATER"

CAN_LIBRARY_TYPE                 = CAN_INNOMAKER

# CAN Bus ---------------------------------------------------------------------------------------------------------------------
CAN_BITRATE                      = 1000000                     # CAN Bitrate of 1 Megabit per Second

CAN_DATABASE_PATH                = "database/Main_2023.dbc"
CAN_BMS_DATABASE_PATH            = "database/BMS_2023.dbc"

CAN_ID_COMMAND_DRIVE_START       = 0x004                       # ID of Command_Drive_Start
CAN_ID_INPUT_PEDALS              = 0x005                       # ID of Input_Pedals
CAN_ID_COMMAND_TORQUE_LIMIT      = 0x010                       # ID of Command_Torque_Limit
CAN_ID_DATA_TEMP_1               = 0x0A0                       # ID of Data_Temperature_1
CAN_ID_DATA_TEMP_2               = 0x0A1                       # ID of Data_Temperature_2
CAN_ID_DATA_TEMP_3               = 0x0A2                       # ID of Data_Temperature_3_Torque
CAN_ID_DATA_MOTOR                = 0x0A5                       # ID of Data_Motor
CAN_ID_CELL_VOLTAGES_START       = 0x401                       # ID of Cell_Voltages_01_04
CAN_ID_CELL_VOLTAGES_END         = 0x417                       # ID of Cell_Voltages_88_89
CAN_ID_PACK_TEMPERATURES_START   = 0x41B                       # ID of Pack_Temperatures_00_03
CAN_ID_PACK_TEMPERATURES_END     = 0x426                       # ID of Pack_Temperatures_44
CAN_ID_CELL_BALANCINGS_START     = 0x418                       # ID of Cell_Balancings_00_35
CAN_ID_CELL_BALANCINGS_END       = 0x41A                       # ID of Cell_Balancings_72_89
CAN_ID_STATUS_BMS                = 0x440                       # ID of Status_BMS
CAN_ID_DATA_PEDALS               = 0x701                       # ID of Data_Pedals
CAN_ID_STATUS_ECU                = 0x703                       # ID of Status_ECU

CAN_ID_CALIBRATE_APPS_RANGE      = 0x533                       # ID of Calibrate_APPS_Range
CAN_ID_CALIBRATE_BRAKE_RANGE     = 0x534                       # ID of Calibrate_Brake_Range

CAN_MESSAGE_TIMEOUT              = 1                           # Length of Time for CAN Activity to Expire
CAN_TIME_PERIOD                  = 0.01                        # Period of Time Thread Update

# CAN Data Interpretation -----------------------------------------------------------------------------------------------------
RPM_MAX                          = 5500                        # Maximum RPM Value
INVERTER_RPM_SCALE               = 1                           # Inverter RPM Scale Factor
INVERTER_TEMP_SCALE              = 0.1                         # Inverter Temperature Scale Factor

APPS_1_PERCENT_SCALE             = 0.1                         # APPS-1 Percent Scale Factor
APPS_2_PERCENT_SCALE             = 0.1                         # APPS-2 Percent Scale Factor
BRAKE_1_PERCENT_SCALE            = 0.1                         # Brake-1 Percent Scale Factor
BRAKE_2_PERCENT_SCALE            = 0.1                         # Brake-2 Percent Scale Factor

LV_BATTERY_VOLTAGE_SCALE         = 0.0196888                   # Low-Voltage Battery Voltage Scale Factor
CELL_VOLTAGE_SCALE               = 0.0001                      # Cell Voltage Scale Factor
PACK_TEMPERATURE_SCALE           = -0.0021933                  # Pack Temperature Scale Factor
PACK_TEMPERATURE_OFFSET          = 81.297                      # Pack Temperature Offset Factor
STATE_OF_CHARGE_SCALE            = 0.1                         # State of Charge Scale Factor
PACK_CURRENT_LO_SCALE            = 0.01                        # Pack Current Lo Byte Scale Factor

# Logging ---------------------------------------------------------------------------------------------------------------------
LOG_FILE                         = "stdout.log"

# Vehicle Configuration Defaults ------------------------------------------------------------------------------------------------------
TORQUE_LIMIT                     = 230
REGEN_LIMIT                      = 30

RADIANS_PER_ROTATION             = 6.283185307                 # Number of Radians per Rotation (2 * PI)
TIRE_RADIUS_INCHES               = 9                           # Radius of the Vehicle Rear Tire
SPROCKET_TEETH_COUNT             = 40                          # Number of Teeth on Axle Sprocket
MOTOR_TEETH_COUNT                = 13                          # Number of Teeth on Motor Sprocket
MINUTES_PER_HOUR                 = 60                          # Number of Minutes per Hour
INCHES_PER_FOOT                  = 12                          # Number of Inches per Foot
FEET_PER_MILE                    = 5280                        # Number of Feet per Mile