# Car-Config Overview
Desktop application for the configuration, monitoring, and debugging of ZRE race cars. Car-Config is run as a desktop app, and thus can serve dual-use as a debugging tool for test-bench vehicle electronics, and for configuration and monitoring of the vehicle during testing and competition.

Car-Config is written in python and is based off of code from DASH23. Layout is inspired by the BMSGuiApplication.

# GUI Overview
## CAN View
## BMS View
## Vehicle Configuration
The vehicle configuration allows a number of custom vehicle presets to be created, adjusted, and loaded on the fly. These can be presets for testing, different competition events, etc, and allow for quick loading and adjustment of a number of settings.
### Pedal Calibration
- Enter pedal calibration mode
### Torque Config
- adjustable torque limit for driver practice
### BMS Config
- over-voltage and under-voltage trip limits
- minimum delta voltage to initiate balancing
- Mapping BMS Current limits, including continuous discharge limits, peak discharge limits, and charging limits versus battery voltage

# Instalaltion 
### Dependencies
Car-Config uses customtkinter, which needs to be installed in addition to tkinter configured python. First make sure python is installed by checking the python version:
'python3 -version'

 and that pip is up to date:
'pip3 install --upgrade pip'

Sometimes 'packaging' isn't installed:
'pip3 install packaging'

Finally install tkinter and customtkinter:
'pip3 install python-tk'
'pip3 install customtkinter'

