| Message | Name | Length (Bit) | Byte Order | Value Type | Factor | Offset | Unit | Comment |
|---|---|---|---|---|---|---|---|---|
| Status_ECU (0x703) | Error_100ms_Implausible | 1 | Intel | Unsigned | 1 | 0 | Boolean | 100ms APPS Plausibility |
| | Error_25_5_Implausible | 1 | Intel | Unsigned | 1 | 0 | Boolean | APPS 25/5 Plausibility | 
| | Error_ACAN_Implausible | 1 | Intel | Unsigned | 1 | 0 | Boolean | ACAN Pedal Plausibility |
| | Error_Inverter_Fault | 1 | Intel | Unsigned | 1 | 0 | Boolean | Inverter Status |
| | Resistance_IMD | 16 | Intel | Unsigned | 1 | 0 | ADC | IMD Resistance |
| | State_Accelerating | 1 | Intel | Unsigned | 1 | 0 | Boolean | ECU Accelerator Status |
| | State_Braking | 1 | Intel | Unsigned | 1 | 0 | Boolean | ECU Brake Status |
| | State_Drive_State | 2 | Intel | Unsigned | 1 | 0 | Enumerable | ECU Drive Status |
| | State_DRS | 1 | Intel | Unsigned | 1 | 0 | Boolean | DRS Status |
| | State_Regen | 1 | Intel | Unsigned | 1 | 0 | Boolean | Regen Braking Status |
| | Torque_Percentage_Max | 8 | Intel | Unsigned | 1 | 0 | Percent | Maximum Torque Percentage |
| | Torque_Percentage_Regen | 8 | Intel | Unsigned | 1 | 0 | Percent | Regen Percentage |
| | Voltage_LV_Battery | 16 | Intel | Unsigned | 0.0196888 | 0 | Volts | LV Battery Voltage |
| Status_Dashboard (0x321) | Error_25_5_Implausible | 1 | Intel | Unsigned | 1 | 0 | Boolean | APPS 25/5 Plausibility |
| | Error_Inverter_Fault | 1 | Intel | Unsigned | 1 | 0 | Boolean | Inverter Status |
| | State_Drive_State | 2 | Intel | Unsigned | 1 | 0 | Enumerable | ECU Drive Status |
| | Warning_LV_Battery | 1 | Intel | Unsigned | 1 | 0 | Boolean | Warning for Low Charge on LV Battery |
| Status_BMS_2 (0x100) | Current_BMS | 16 | Intel | Unsigned | 0.01 | 0 | Amperes | Current Drawn from Accumululator |
| | Error_BMS_Self_Test_Fault | 1 | Intel | Unsigned | 1 | 0 | Boolean | BMS Self Test Fault |
| | Error_BMS_Sense_Line_Fault | 1 | Intel | Unsigned | 1 | 0 | Boolean | BMS Sense Line Fault |
| | Error_BMS_Temperature_Fault | 1 | Intel | Unsigned | 1 | 0 | Boolean | BMS Temperature Fault |
| | Error_BMS_Voltage_Fault | 1 | Intel | Unsigned | 1 | 0 | Boolean | BMS Voltage Fault |
| | Power_BMS | 8 | Intel | Unsigned | 1 | 0 | KiloWatts | Accumulator Power Draw |
| | State_of_Charge | 8 | Intel | Unsigned | 1 | 0 | Percentage | Accumulator State of Charge |
| | Temperature_BMS_Max | 8 | Intel | Unsigned | 1 | 0 | Celsius | Highest Accumulator Temperature |
| | Voltage_BMS | 16 | Intel | Unsigned | 1 | 0 | Volts | Pack Cell Voltage |
| Status_BMS (0x440) | Current_BMS_Hi | 16 | Intel | Unsigned | 0.1 | 0 | Amperes | Current Hi Byte |
| | Current_BMS_Lo | 16 | Intel | Unsigned | 0.01 | 0 | Amperes | Current Lo Byte |
| | Error_BMS_Self_Test_Fault | 1 | Intel | Unsigned | 1 | 0 | Boolean | BMS Self Test Fault |
| | Error_BMS_Sense_Line_Fault | 1 | Intel | Unsigned | 1 | 0 | Boolean | BMS Sense Line Fault |
| | Error_BMS_Temperature_Fault | 1 | Intel | Unsigned | 1 | 0 | Boolean | BMS Temperature Fault |
| | Error_BMS_Voltage_Fault | 1 | Intel | Unsigned | 1 | 0 | Boolean | BMS Voltage Fault |
| | State_of_Charge | 16 | Intel | Unsigned | 0.1 | 0 | Percentage | Accumulator State of Charge |
| Input_Pedals (0x005) | APPS_1_Raw | 10 | Intel | Unsigned | 1 | 0 | ADC | APPS-1 ACAN Reading |
| | APPS_2_Raw | 10 | Intel | Unsigned | 1 | 0 | ADC | APPS-2 ACAN Reading |
| | Brake_1_Raw | 10 | Intel | Unsigned | 1 | 0 | ADC | Brake-1 ACAN Reading |
| | Brake_2_Raw | 10 | Intel | Unsigned | 1 | 0 | ADC | Brake-2 ACAN Reading |
| Input_Dashboard (0x0FF) | Button_Clear_Faults | 1 | Intel | Unsigned | 1 | 0 | Boolean | Clear Inverter Faults Button |
| | Button_DRS | 1 | Intel | Unsigned | 1 | 0 | Boolean | DRS Button |
| | Button_Regen | 1 | Intel | Unsigned | 1 | 0 | Boolean | Regen Button | 
| | Button_Start | 1 | Intel | Unsigned | 1 | 0 | Boolean | Start Button |
| | Switch_Drive_Mode | 3 | Intel | Unsigned | 1 | 0 | Enumerable | Dashboard Switch for Drive Mode |
| | Switch_DRS | 3 | Intel | Unsigned | 1 | 0 | Enumerable | Dashboard Switch for DRS Percentage |
| Error_Inverter_Fault (0x0AB) | Error_POST_Fault | 32 | Intel | Unsigned | 1 | 0 | Word | Inverter POST Fault Code |
| | Error_Run_Fault | 32 | Intel | Unsigned | 1 | 0 | Word | Inverter Run Fault Code |
| Data_Voltage (0x0A7) | Voltage_D_Axis | 16 | Intel | Signed | 0.1 | 0 | Volts | Inverter D-Axis Voltage. Refers to Phase A-B Voltage when disabled |
| | Voltage_DC_Bus | 16 | Intel | Signed | 0.1 | 0 | Volts | Voltage of the Inverter DC Bus |
| | Voltage_Inverter_Output | 16 | Intel | Signed | 0.1 | 0 | Volts | Voltage of the Inverters Output |
| | Voltage_Q_Axis | 16 | Intel | Signed | 0.1 | 0 | Volts | Inverter Q-Axis Voltage. Refers to Phase B-C when disabled |
| Data_Torque (0x0FA) | Torque_Percentage_Max | 8 | Intel | Unsigned | 1 | 0 | Percent | Maximum Torque Percentage |
| | Torque_Percentage_Regen | 8 | Intel | Unsigned | 1 | 0 | Percent | Regen Percentage |
| Data_Temperature_3_Torque (0x0A2) | Temperature_Inverter_RTD4 | 16 | Intel | Signed | 0.1 | 0 | Celsius | Temperature of RTD #4 |
| | Temperature_Inverter_RTD5 | 16 | Intel | Signed | 0.1 | 0 | Celsius | Temperature of RTD #5 |
| | Temperature_Motor | 16 | Intel | Signed | 0.1 | 0 | Celsius | Temperature of the Motor |
| | Torque_Shudder | 16 | Intel | Signed | 0.1 | 0 | Newton Meters | Motor Torque Shudder |
| Data_Temperature_2 (0x0A1) | Temperature_Inverter_CB | 16 | Intel | Signed | 0.1 | 0 | Celsius | Temperature of the Control Board |
| | Temperature_Inverter_RTD1 | 16 | Intel | Signed | 0.1 | 0 | Celsius | Temperature of RTD #1 |
| | Temperature_Inverter_RTD2 | 16 | Intel | Signed | 0.1 | 0 | Celsius | Temperature of RTD #2 |
| | Temperature_Inverter_RTD3 | 16 | Intel | Signed | 0.1 | 0 | Celsius | Temperature of RTD #3 |
| Data_Temperature_1 (0x0A0) | Temperature_Inverter_GDB | 16 | Intel | Signed | 0.1 | 0 | Celsius | Temperature of the Gate Driver Board |
| | Temperature_Inverter_Module_C | 16 | Intel | Signed | 0.1 | 0 | Celsius | Temperature of IGBT Module |
| | Temperature_Inverter_Module_B | 16 | Intel | Signed | 0.1 | 0 | Celsius | Temperature of IGBT Module |
| | Temperature_Inverter_Module_A | 16 | Intel | Signed | 0.1 | 0 | Celsius | Temperature of IGBT Module |
| Data_Pedals (0x701) | APPS_1_Percent | 16 | Intel | Unsigned | 0.1 | 0 | Percent | APPS-1 Percentage |
| | APPS_2_Percent | 16 | Intel | Unsigned | 0.1 | 0 | Percent | APPS-2 Percentage |
| | Brake_1_Percent | 16 | Intel | Unsigned | 0.1 | 0 | Percent | Brake-1 Percentage |
| | Brake_2_Percent | 16 | Intel | Unsigned | 0.1 | 0 | Percent | Brake-2 Percentage |
| Data_Motor (0x0A5) | Motor_Angle | 16 | Intel | Signed | 0.1 | 0 | Degrees | Current Angle of the Motor |
| | Motor_Filtered_Delta_Resolver | 16 | Intel | Signed | 0.1 | 0 | Degrees | Motor Filtered Delta Resolver Value |
| | Motor_Frequency | 16 | Intel | Signed | 0.1 | 0 | Hz | Current Frequency of the Motor |
| | Motor_Speed | 16 | Intel | Signed | 1 | 0 | RPM | The Angluar Velocity of the Motor |
| Data_Flux (0x0A8) | Current_D_Axis | 16 | Intel | Signed | 0.1 | 0 | Amps | Current of Inverter D-Axis |
| | Current_Q_Axis | 16 | Intel | Signed | 0.1 | 0 | Amps | Current  of Inverter Q-Axis |
| | Flux | 16 | Intel | Signed | 0.001 | 0 | Webers | Inverter Actual Flux |
| | Flux_Target | 16 | Intel | Signed | 0.001 | 0 | Webers | Inverter Target Flux |
| Data_Current (0x0A6) | Current_DC_Bus | 16 | Intel | Signed | 0.1 | 0 | Amps | Current of Inverter DC Bus |
| | Current_Phase_A | 16 | Intel | Signed | 0.1 | 0 | Amps | Current of Inverter Phase A |
| | Current_Phase_B | 16 | Intel | Signed | 0.1 | 0 | Amps | Current of Inverter Phase B |
| | Current_Phase_C | 16 | Intel | Signed | 0.1 | 0 | Amps | Current of Inverter Phase C |
| Data_Accelerometer_Angle (0x126) | Acceleration_Pitch_Angle | 16 | Motorola | Unsigned | 0.01962 | -627.84 | m/s^2 |  |
| | Acceleration_Roll_Angle | 16 | Motorola | Unsigned | 0.01962 | -627.84 | m/s^2 |  |
| Data_Accelerometer_Acceleration (0x127) | Acceleration_x_Axis | 16 | Motorola | Unsigned | 0.01 | -4 | g |  |
| | Acceleration_y_Axis | 16 | Motorola | Unsigned | 0.01 | -4 | g |  |
| | Acceleration_z_Axis | 16 | Motorola | Unsigned | 0.01 | -4 | g |  |
| Command_Inverter (0x0C0) | Inverter_Direction | 1 | Intel | Unsigned | 1 | 0 | Boolean | Inverter Direction Command |
| | Inverter_Discharge | 1 | Intel | Unsigned | 1 | 0 | Boolean | Inverter Discharge Command |
| | Inverter_Enable | 1 | Intel | Unsigned | 1 | 0 | Boolean | Inverter Enable Command |
| | Speed_Mode | 1 | Intel | Unsigned | 1 | 0 | Boolean | Inverter Speed Mode Command |
| | Speed_Target | 16 | Intel | Signed | 1 | 0 | RPM | Inverter Speed Command |
| | Torque_Limit | 16 | Intel | Signed | 0.1 | 0 | Newton Meters | Inverter Torque Limit Command |
| | Torque_Target | 16 | Intel | Signed | 0.1 | 0 | Newton Meters | Inverter Torque Command |
| Command_DRS_Status (0x123) | State_DRS | 1 | Intel | Unsigned | 1 | 0 | Boolean | DRS Status |
| Command_APPS_Calibration (0x533) | APPS_1_Max | 10 | Intel | Unsigned | 1 | 0 | ADC |  |
| | APPS_1_Min | 10 | Intel | Unsigned | 1 | 0 | ADC |  |
| | APPS_2_Raw_Max | 10 | Intel | Unsigned | 1 | 0 | ADC |  |
| | APPS_2_Raw_Min | 10 | Intel | Unsigned | 1 | 0 | ADC |  |