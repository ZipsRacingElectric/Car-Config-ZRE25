# Table of Contents
- [Table of Contents](#table-of-contents)
- [ZRE Car Config](#zre-car-config)
- [Connecting to the Vehicle](#connecting-to-the-vehicle)
- [Software Documentation](#software-documentation)
  - [Data View (IN PROGRESS)](#data-view-in-progress)
  - [CAN View (IN PROGRESS)](#can-view-in-progress)
    - [Real-time Data View with DBC File (unimplemented)](#real-time-data-view-with-dbc-file-unimplemented)
    - [CANbus Configuration (unimplemented)](#canbus-configuration-unimplemented)
      - [Command ID Configuration (unimplemented)](#command-id-configuration-unimplemented)
  - [BMS View (unimplemented)](#bms-view-unimplemented)
  - [Vehicle Configuration (unimplemented)](#vehicle-configuration-unimplemented)
    - [Preset Manager (unimplemented)](#preset-manager-unimplemented)
    - [Pedal Calibration (unimplemented)](#pedal-calibration-unimplemented)
    - [Steering Sensor Calibration (unimplemented)](#steering-sensor-calibration-unimplemented)
    - [Brake Temp Sensor Setup (unimplemented)](#brake-temp-sensor-setup-unimplemented)
    - [General Config (unimplemented)](#general-config-unimplemented)
    - [Dash Config (unimplemented)](#dash-config-unimplemented)
    - [Steering Wheel Config (unimplemented)](#steering-wheel-config-unimplemented)
    - [BMS Config (unimplemented)](#bms-config-unimplemented)
    - [DRS Configuration (unimplemented)](#drs-configuration-unimplemented)
    - [Sensor Configuration (unimplemented)](#sensor-configuration-unimplemented)
- [Installation](#installation)
    - [Dependencies](#dependencies)
# ZRE Car Config 
ZRE Car Config is a desktop application for the configuration, monitoring, and debugging of ZRE race cars. As a desktop app, it can serve dual-purpose as a debugging tool for test-bench vehicle electronics and for configuration / monitoring of the vehicle during testing and competition.

It is designed to eventually replace the large touchscreen dashboard, allowing us to keep our easy configuration capabilities while saving weight, reducing the LV battery size, and giving more room for steering wheel position flexibility.

This software is written in python and is based off of code from DASH23. Layout is inspired by the BMSGuiApplication.

# Connecting to the Vehicle
There will be two ways to connect Car Config to the race car:
- USB to CAN Adapter
- Bluetooth

# Software Documentation
## Data View (IN PROGRESS)
![Data View Mockup](./images/Data%20View%20Mockup.png "Data View Mockup")

The Data View is the default screen for the app and shows real-time CANbus data decoded with a .dbc file

## CAN View (IN PROGRESS)
![CAN View Mockup](./images/CAN%20View%20Mockup.png "CAN View Mockup")

### Real-time Data View with DBC File (unimplemented)

### CANbus Configuration (unimplemented)
- CAN 1 DBC File Path
- CAN 2 DBC File Path
- CAN Bitrate
- CAN Message Timeout
- CAN Time Period

#### Command ID Configuration (unimplemented)
- COMMAND_DRIVE_START
- INPUT_PEDALS
- COMMAND_TORQUE_LIMIT
- DATA_TEMP_1
- DATA_TEMP_2
- DATA_TEMP_3
- DATA_MOTOR
- CELL_VOLTAGES_START
- CELL_VOLTAGES_END
- PACK_TEMPERATURES_START
- PACK_TEMPERATURES_END
- CELL_BALANCING_START
- CELL_BALANCING_END
- STATUS_BMS
- DATA_PEDALS
- STATUS_ECU
- CALIBRATE_APPS_RANGE
- CALIBRATE_BRAKE_RANGE

## BMS View (unimplemented)
![BMS View Mockup](./images/BMS%20View%20Mockup.png "BMS View Mockup")

## Vehicle Configuration (unimplemented)
The vehicle configuration allows a number of custom vehicle presets to be created, adjusted, and loaded on the fly. These can be presets for testing, different competition events, etc, and allow for quick loading and adjustment of a number of settings.

### Preset Manager (unimplemented)
- Create Preset
- Delete Preset
- Select Preset for editing
- Save Presets to file
- Load Presets file

### Pedal Calibration (unimplemented)
- Enter pedal calibration mode

### Steering Sensor Calibration (unimplemented)
- Enter steering sensor calibration mode

### Brake Temp Sensor Setup (unimplemented)
- Assigns CAN IDs to Izze Brake Temp Sensors

### General Config (unimplemented)
- Torque Max Limit
- Regen Max Limit
- Radians Per Rotation (???)
- Tire Radius
- Diff Gear Tooth Count
- Motor Gear Tooth Count
- Ready to Drive Sound time (seconds)

### Dash Config (unimplemented)
- Button 1
    - Function
    - Invert
- Button 2
    - Function
    - Invert

The following are used to interpret CAN data:
- Max RPM
- Inverter RPM Scale
- Inverter Temp Scale
- APPS 1 Percent Scale
- APPS 2 Percent Scale
- Brake 1 Percent Scale
- Brake 2 Percent Scale
- LV Battery Voltage Scale
- Cell Voltage Scale
- Pack Temperature Scale
- Pack Temperature Offset
- State of Charge Scale
- Pack Current Low Scale

### Steering Wheel Config (unimplemented)
- Left Button
    - Function
    - Invert
- Right Button
    - Function
    - Invert
- Left Dial
    - Function
    - Zero value
    - Gain
- Right Dial
    - Function
    - Zero value
    - Gain

### BMS Config (unimplemented)
- Regen enable Radiobutton
- Number of BMS ICs
- Cells Per Register
- Cell Voltage Registers Per IC
- Cells Per IC
- Number of temp sensors per IC
- Number of Aux Registers per IC
- over-voltage and under-voltage trip limits
- Battery cell over-temp and under-temp trip limits
- minimum voltage threshold to initiate balancing
- Balance in low voltage Radiobutton
- continuous discharge current limit vs voltage map
- peak discharge current limit vs voltage map
- regen current limit vs voltage map
- cont current % vs temperature map
- peak current % vs temperature map
- regen current % vs temperature map
- regen current % vs brake pedal % map
- Regen minimum speed
- Regen start voltage

### DRS Configuration (unimplemented)
- Front DRS
    - Enable Radiobutton
    - Downforce Position Servo Angle
    - Drag Position Servo Angle
    - Servo Angle Offset
- Rear DRS
    - Enable Radiobutton
    - Downforce Position Servo Angle
    - Drag Position Servo Angle
    - Servo Angle Offset
- DRS Mode Select
    - Manual (button activated)
    - Speed Based Only
    - Speed & Acceleration Based
    - Speed & Steering Angle Based
- Speed Only Options
    - DRS Changeover Speed (mph)
- Speed & Acceleration Options
    - TODO
- Speed & Steering Angle Options
    - TODO
- Force Downforce Position during:
    - Braking Checkbox
    - Regen Checkbox
    - Coasting Checkbox
- DRS Servo Auto Home Radiobutton
    - If the physical DRS airfoils have hard endstops, use those to find and set the servo angle offset automatically upon vehicle turn-on
  
### Sensor Configuration (unimplemented)
General Presets for interpretaation of sensor data.
- Brake Pressure
- Wheel Speed
- Damper Position

# Installation

### Dependencies
Car-Config uses customtkinter, which needs to be installed in addition to tkinter configured python.

Requirements

Websockets
CANmatrix

Finally install tkinter and customtkinter:
```bash
pip3 install websockets
pip3 install CANmatrix
``` 
