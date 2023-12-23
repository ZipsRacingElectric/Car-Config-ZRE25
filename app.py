# App -------------------------------------------------------------------------------------------------------------------------
# Author: Brian Glen
# Date Created: 12/22/23
# Date Updated: 12/22/23
#   The main file for the application, execute this file to instance the app. This file is responsible for instancing and
#   initializing the CAN and GUI modules.
#
# Adapted from the DASH23 software

# Libraries -------------------------------------------------------------------------------------------------------------------
import logging
import os

# Includes --------------------------------------------------------------------------------------------------------------------
import config
import gui
import can_interface
import gpio_interface
import database

# App Execution ---------------------------------------------------------------------------------------------------------------
if(__name__ == "__main__"):
    # Initialization
    logPath = os.path.join(os.path.dirname(__file__), config.LOG_FILE)
    logging.basicConfig(filename=logPath,
                        filemode='w',
                        format="%(asctime)s [%(levelname)s] %(message)s",
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

    try:
        logging.debug("APP - Initializing...")
        mainDatabase = database.Setup()                            # Setup Database
        mainCan      = can_interface.Setup(mainDatabase)           # Setup CAN Interface
        mainGpio     = gpio_interface.Setup(mainDatabase, mainCan) # Setup GPIO Interface
        mainGui      = gui.Setup(mainDatabase, mainCan)            # Setup GUI
        
        # Begin
        logging.debug("APP - Begining...")
        mainCan.Begin()                                            # Begin CAN
        if(mainGpio != None): mainGpio.Begin()                     # Begin GPIO

        mainDatabase["Torque_Config_Limit"] = 22
        mainDatabase["Torque_Config_Limit_Regen"] = 0

        mainGui.Begin()                                            # Begin GUI

        # GUI Begin function will not return until app is closed.
        
        # Exit
        logging.debug("APP - Terminating...")
        mainCan.Kill()
        if(mainGpio != None): mainGpio.Kill()
        logging.debug("APP - Terminated.")
        logging.shutdown()
        exit()
    except Exception as e:
        # Exit as Failure
        logging.error("App Failure: " + str(e))
        logging.error("Terminating...")
        logging.shutdown()
        exit(1)