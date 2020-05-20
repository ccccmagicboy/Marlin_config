import os
import sys
import subprocess
import shlex
from termcolor import colored
import fileinput
from shutil import copy

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

def send_cmd(command):
    print(command)
    result_str =os.popen(command).read()
    print(result_str)
    return result_str

print(os.getcwd())
print(os.listdir(os.getcwd()))

send_cmd('chmod +x {0:s}/my_marlin/buildroot/bin/*'.format(os.getcwd()))
sys.path.append('{0:s}/my_marlin/buildroot/bin'.format(os.getcwd()))
print(sys.path)

subprocess.call(['{0:s}/my_marlin/buildroot/bin/restore_configs'.format(os.getcwd())])

# cp _Statusscreen.h and _Bootscreen.h
src = os.path.join('{0:s}/Marlin_v2/_Statusscreen.h'.format(os.getcwd()))
dst = os.path.join('{0:s}/my_marlin/Marlin'.format(os.getcwd()))
copy(src, dst)
print(os.listdir(dst))

src = os.path.join('{0:s}/Marlin_v2/_Bootscreen.h'.format(os.getcwd()))
dst = os.path.join('{0:s}/my_marlin/Marlin'.format(os.getcwd()))
copy(src, dst)
print(os.listdir(dst))

os.chdir('my_marlin')

# replaceAll(mk_path, "#webrepl.start()","import machine;".format(str))
# opt_add
# opt_enable
# opt_disable
# opt_set

########################################################################################################################
# Configuration.h
########################################################################################################################
#STRING_CONFIG_H_AUTHOR#################################################################################################
replaceAll('{0:s}/Marlin/Configuration.h'.format(os.getcwd()), '(none, default config)', '(ccrobot-online, MEEB_3DP)')
print(colored('The author of the config file is {0:s}'.format('ccccmagicboy'), "green"))
#SHOW_CUSTOM_BOOTSCREEN#################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable SHOW_CUSTOM_BOOTSCREEN'.format(os.getcwd())))
print(colored('The custom bootscreen is enabled', "green"))
#CUSTOM_STATUS_SCREEN_IMAGE#############################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable CUSTOM_STATUS_SCREEN_IMAGE'.format(os.getcwd())))
print(colored('The custom status screen is enabled', "green"))
#SERIAL_PORT############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set SERIAL_PORT {1:s}'.format(os.getcwd(), '-1')))
print(colored('The main serial is USB serial.', "green"))
#SERIAL_PORT_2##########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set SERIAL_PORT_2 {1:s}'.format(os.getcwd(), '1')))
print(colored('The second serial is UART1', "green"))
#BAUDRATE###############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set BAUDRATE {1:s}'.format(os.getcwd(), '115200')))
print(colored('The serial bitrate is 115200', "green"))
#MOTHERBOARD############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set MOTHERBOARD {1:s}'.format(os.getcwd(), os.environ['BOARD'])))
print(colored('The select board is {0:s}'.format(os.environ['BOARD']), "green"))
#CUSTOM_MACHINE_NAME####################################################################################################
replaceAll('{0:s}/Marlin/Configuration.h'.format(os.getcwd()), '//#define CUSTOM_MACHINE_NAME "3D Printer"', '#define CUSTOM_MACHINE_NAME "Ender-3"')
print(colored('The machine name is {0:s}'.format('Ender-3'), "green"))
#MACHINE_UUID###########################################################################################################
replaceAll('{0:s}/Marlin/Configuration.h'.format(os.getcwd()), '//#define MACHINE_UUID "00000000-0000-0000-0000-000000000000"', '#define MACHINE_UUID "21d7a8c6-d587-4189-9e5c-414d6990b363"')
print(colored('The machine uuid is {0:s}'.format('21d7a8c6-d587-4189-9e5c-414d6990b363'), "green"))
#DEFAULT_NOMINAL_FILAMENT_DIA###########################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set DEFAULT_NOMINAL_FILAMENT_DIA {1:s}'.format(os.getcwd(), '1.75')))
print(colored('The nominal filament dia is {0:s}'.format('1.75'), "green"))
#TEMP_SENSOR_0##########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set TEMP_SENSOR_0 {1:s}'.format(os.getcwd(), '1')))
print(colored('The temperature sensor 0 is {0:s}'.format('1'), "green"))
#TEMP_SENSOR_BED########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set TEMP_SENSOR_BED {1:s}'.format(os.getcwd(), '1')))
print(colored('The temperature bed is {0:s}'.format('1'), "green"))
#BED_MAXTEMP############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set BED_MAXTEMP {1:s}'.format(os.getcwd(), '125')))
print(colored('The bed max temperature is set to {0:s}'.format('125'), "green"))
#PID_EDIT_MENU##########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable PID_EDIT_MENU'.format(os.getcwd())))
print(colored('The pid menu is enabled', "green"))
#PID_AUTOTUNE_MENU######################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable PID_AUTOTUNE_MENU'.format(os.getcwd())))
print(colored('The pid autotune menu is enabled', "green"))
#PIDTEMPBED#############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable PIDTEMPBED'.format(os.getcwd())))
print(colored('The bed pid is enabled', "green"))
#EXTRUDE_MAXLENGTH######################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set EXTRUDE_MAXLENGTH {1:s}'.format(os.getcwd(), '450')))
print(colored('The max extrude lengthy is set to {0:s}'.format('450'), "green"))
#THERMAL_PROTECTION_CHAMBER#############################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_disable THERMAL_PROTECTION_CHAMBER'.format(os.getcwd())))
print(colored('The chamber thermal protection is disabled', "red"))
#ENDSTOPPULLUPS#########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable ENDSTOPPULLUPS'.format(os.getcwd())))
print(colored('The endstop pull-up resistors are enabled', "green"))
#ENDSTOP_INTERRUPTS_FEATURE#############################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable ENDSTOP_INTERRUPTS_FEATURE'.format(os.getcwd())))
print(colored('The endstop interrupt feature is enabled', "green"))
#SOFT_ENDSTOPS_MENU_ITEM################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable SOFT_ENDSTOPS_MENU_ITEM'.format(os.getcwd())))
print(colored('The soft endstop menu is enabled', "green"))
#X_DRIVER_TYPE##########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set X_DRIVER_TYPE {1:s}'.format(os.getcwd(), 'TMC2208')))
print(colored('The x axis driver is set to {0:s}'.format('TMC2208'), "green"))
#Y_DRIVER_TYPE##########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Y_DRIVER_TYPE {1:s}'.format(os.getcwd(), 'TMC2208')))
print(colored('The y axis driver is set to {0:s}'.format('TMC2208'), "green"))
#Z_DRIVER_TYPE##########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Z_DRIVER_TYPE {1:s}'.format(os.getcwd(), 'TMC2208')))
print(colored('The z axis driver is set to {0:s}'.format('TMC2208'), "green"))
#E0_DRIVER_TYPE#########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set E0_DRIVER_TYPE {1:s}'.format(os.getcwd(), 'TMC2208')))
print(colored('The e0 axis driver is set to {0:s}'.format('TMC2208'), "green"))
#DEFAULT_AXIS_STEPS_PER_UNIT############################################################################################
replaceAll('{0:s}/Marlin/Configuration.h'.format(os.getcwd()), 'DEFAULT_AXIS_STEPS_PER_UNIT   { 80, 80, 4000, 500 }', 'DEFAULT_AXIS_STEPS_PER_UNIT   { 80, 80, 400, 97.5 }')
print(colored('The default step/mm is set to {0:s}'.format('{ 80, 80, 400, 97.5 }'), "green"))
#DEFAULT_MAX_FEEDRATE###################################################################################################
replaceAll('{0:s}/Marlin/Configuration.h'.format(os.getcwd()), 'DEFAULT_MAX_FEEDRATE          { 300, 300, 5, 25 }', 'DEFAULT_MAX_FEEDRATE          { 300, 300, 75, 300 }')
print(colored('The default max feedrate is set to {0:s} mm/s.'.format('{ 300, 300, 75, 300 }'), "green"))
#S_CURVE_ACCELERATION###################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable S_CURVE_ACCELERATION'.format(os.getcwd())))
print(colored('The s-curve acceleration is enabled', "green"))
#INVERT_X_DIR###########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set INVERT_X_DIR {1:s}'.format(os.getcwd(), 'true')))
print(colored('The invert x axis dir is set to {0:s}'.format('true'), "green"))
#INVERT_E0_DIR##########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set INVERT_E0_DIR {1:s}'.format(os.getcwd(), 'true')))
print(colored('The invert e0 axis dir is set to {0:s}'.format('true'), "green"))
#NO_MOTION_BEFORE_HOMING################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable NO_MOTION_BEFORE_HOMING'.format(os.getcwd())))
print(colored('The no motion before homing is enabled', "green"))
#UNKNOWN_Z_NO_RAISE#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable UNKNOWN_Z_NO_RAISE'.format(os.getcwd())))
print(colored('The unknown z no raise is enabled', "green"))
#Z_HOMING_HEIGHT########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Z_HOMING_HEIGHT {1:s}'.format(os.getcwd(), '0')))
print(colored('The z homing height is set to {0:s} mm.'.format('0'), "green"))
#Z_AFTER_HOMING#########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Z_AFTER_HOMING {1:s}'.format(os.getcwd(), '10')))
print(colored('The z after homing is set to {0:s} mm.'.format('10'), "green"))
#X_BED_SIZE#############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set X_BED_SIZE {1:s}'.format(os.getcwd(), '235')))
print(colored('The x bed size is set to {0:s} mm.'.format('235'), "green"))
#Y_BED_SIZE#############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Y_BED_SIZE {1:s}'.format(os.getcwd(), '235')))
print(colored('The y bed size is set ot {0:s} mm.'.format('235'), "green"))
#Z_MAX_POS##############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Z_MAX_POS {1:s}'.format(os.getcwd(), '240')))
print(colored('The z max is set to {0:s} mm.'.format('240'), "green"))
#LEVEL_BED_CORNERS######################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable LEVEL_BED_CORNERS'.format(os.getcwd())))
print(colored('The manunal z bed corners leveling is enabled', "green"))
#LEVEL_CENTER_TOO#######################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable LEVEL_CENTER_TOO'.format(os.getcwd())))
print(colored('The manunal z bed corners leveling center point is enabled', "green"))
#Z_SAFE_HOMING##########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable Z_SAFE_HOMING'.format(os.getcwd())))
print(colored('The z safe homing is enabled', "green"))
#NOZZLE_PARK_FEATURE####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable NOZZLE_PARK_FEATURE'.format(os.getcwd())))
print(colored('The nozzle park feature is enabled', "green"))
#NOZZLE_PARK_POINT######################################################################################################
replaceAll('{0:s}/Marlin/Configuration.h'.format(os.getcwd()), '{ (X_MIN_POS + 10), (Y_MAX_POS - 10), 20 }', '{ (X_MIN_POS + 0), (Y_MIN_POS + 0), 40 }')
print(colored('The nozzle park point is set to {0:s}.'.format('{ (X_MIN_POS + 0), (Y_MIN_POS + 0), 40 }'), "green"))
#INDIVIDUAL_AXIS_HOMING_MENU############################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable INDIVIDUAL_AXIS_HOMING_MENU'.format(os.getcwd())))
print(colored('The lcd individual axis homing menu is enabled', "green"))
#PRINTCOUNTER###########################################################################################################
# subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable PRINTCOUNTER'.format(os.getcwd())))
# print(colored('The print counter is enabled', "green"))
#CR10_STOCKDISPLAY######################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable CR10_STOCKDISPLAY'.format(os.getcwd())))
print(colored('The ender-3 stockdisplay is enabled', "green"))
#SPEAKER################################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable SPEAKER'.format(os.getcwd())))
print(colored('The speaker is enabled', "green"))
#LCD_LANGUAGE###########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set LCD_LANGUAGE {1:s}'.format(os.getcwd(), 'en')))
print(colored('The language of LCD is set to {0:s}.'.format('en'), "green"))
#NEOPIXEL_LED###########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable NEOPIXEL_LED'.format(os.getcwd())))
print(colored('The neopixel led is enabled', "green"))
#NEOPIXEL_PIN###########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_disable NEOPIXEL_PIN'.format(os.getcwd())))
print(colored('The neopixel led pin is define in board file, and here it is disabled', "red"))
#NEOPIXEL_BRIGHTNESS####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set NEOPIXEL_BRIGHTNESS {1:s}'.format(os.getcwd(), '88')))
print(colored('The Initial brightness of neopixel led is set to {0:s}.'.format('88'), "green"))
#NEOPIXEL_TYPE##########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set NEOPIXEL_TYPE {1:s}'.format(os.getcwd(), 'NEO_GRB')))
print(colored('The type of neopixel led is set to {0:s}.'.format('NEO_GRB'), "green"))
#NEOPIXEL_PIXELS########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set NEOPIXEL_PIXELS {1:s}'.format(os.getcwd(), '9')))
print(colored('The number of neopixel led is set to {0:s}.'.format('9'), "green"))
#NEOPIXEL_IS_SEQUENTIAL#################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_disable NEOPIXEL_IS_SEQUENTIAL'.format(os.getcwd())))
print(colored('The neopixel sequential is disabled', "red"))
#NEOPIXEL_STARTUP_TEST##################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable NEOPIXEL_STARTUP_TEST'.format(os.getcwd())))
print(colored('The neopixel led startup test is enabled', "green"))
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
# Configuration_adv.h
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
#QUICK_HOME#############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable QUICK_HOME'.format(os.getcwd())))
print(colored('If G28 contains XY do a diagonal move first is enabled', "green"))
#SLOWDOWN_DIVISOR#######################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set SLOWDOWN_DIVISOR {1:s}'.format(os.getcwd(), '8')))
print(colored('Increase the slowdown divisor for larger buffer sizes, set to {0:s}.'.format('8'), "green"))
#ADAPTIVE_STEP_SMOOTHING################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable ADAPTIVE_STEP_SMOOTHING'.format(os.getcwd())))
print(colored('Adaptive Step Smoothing increases the resolution of multi-axis moves, so is enabled', "green"))
#STATUS_MESSAGE_SCROLLING###############################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable STATUS_MESSAGE_SCROLLING LCD_DECIMAL_SMALL_XY LCD_TIMEOUT_TO_STATUS LCD_SET_PROGRESS_MANUALLY LCD_SHOW_E_TOTAL'.format(os.getcwd())))
print(colored('Scroll a longer status message into view, so is enabled', "green"))
#PRINT_PROGRESS_SHOW_DECIMALS###########################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable PRINT_PROGRESS_SHOW_DECIMALS'.format(os.getcwd())))
print(colored('Show progress with decimal digits, so is enabled', "green"))
#SHOW_REMAINING_TIME####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable SHOW_REMAINING_TIME'.format(os.getcwd())))
print(colored('Display estimated time to completion, so is enabled', "green"))
#USE_M73_REMAINING_TIME#################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable USE_M73_REMAINING_TIME'.format(os.getcwd())))
print(colored('Use remaining time from M73 command instead of estimation, so is enabled', "green"))
#ROTATE_PROGRESS_DISPLAY################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable ROTATE_PROGRESS_DISPLAY'.format(os.getcwd())))
print(colored('Display (P)rogress, (E)lapsed, and (R)emaining time, so is enabled', "green"))
#STATUS_FAN_FRAMES######################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set STATUS_FAN_FRAMES {1:s}'.format(os.getcwd(), '4')))
print(colored('Number of fan animation frames is set to {0:s}.'.format('4'), "green"))
#STATUS_HEAT_PERCENT####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable STATUS_HEAT_PERCENT'.format(os.getcwd())))
print(colored('Show heating in a progress bar, so is enabled', "green"))
#BOOT_MARLIN_LOGO_ANIMATED##############################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable BOOT_MARLIN_LOGO_ANIMATED'.format(os.getcwd())))
print(colored('Animated Marlin logo, so is enabled', "green"))
#MARLIN_GAMES###########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable MARLIN_BRICKOUT MARLIN_INVADERS MARLIN_SNAKE GAMES_EASTER_EGG'.format(os.getcwd())))
print(colored('Add games great!!! so is enabled', "green"))
#LCD_INFO_MENU##########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable LCD_INFO_MENU'.format(os.getcwd())))
print(colored('Include a page of printer information in the LCD Main Menu, so is enabled', "green"))
#TURBO_BACK_MENU_ITEM###################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable TURBO_BACK_MENU_ITEM'.format(os.getcwd())))
print(colored('BACK menu items keep the highlight at the top, so is enabled', "green"))
#LED_CONTROL_MENU#######################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable LED_CONTROL_MENU'.format(os.getcwd())))
print(colored('Add LED Control to the LCD menu, so is enabled', "green"))
#MONITOR_DRIVER_STATUS##################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable MONITOR_DRIVER_STATUS'.format(os.getcwd())))
print(colored('Monitor Trinamic drivers, so is enabled', "green"))
#TMC_DEBUG##############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable TMC_DEBUG'.format(os.getcwd())))
print(colored('Enable M122 debugging command for TMC stepper drivers, so is enabled', "green"))
#CANCEL_OBJECTS#########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable CANCEL_OBJECTS'.format(os.getcwd())))
print(colored('Implement M486 to allow Marlin to skip objects, so is enabled', "green"))
#BUFSIZE################################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set BUFSIZE {1:s}'.format(os.getcwd(), '32')))
print(colored('The ASCII buffer for serial input is set to {0:s}.'.format('32'), "green"))
#TX_BUFFER_SIZE#########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set TX_BUFFER_SIZE {1:s}'.format(os.getcwd(), '32')))
print(colored('Transmission to Host Buffer Size is set to {0:s}.'.format('32'), "green"))
#RX_BUFFER_SIZE#########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set RX_BUFFER_SIZE {1:s}'.format(os.getcwd(), '32')))
print(colored('RX Buffer Size is set to {0:s}.'.format('32'), "green"))
#X_CURRENT##############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set X_CURRENT {1:s}'.format(os.getcwd(), '580')))
print(colored('X (mA) RMS current. Multiply by 1.414 for peak current is set to {0:s}.'.format('580'), "green"))
#Y_CURRENT##############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Y_CURRENT {1:s}'.format(os.getcwd(), '580')))
print(colored('Y (mA) RMS current. Multiply by 1.414 for peak current is set to {0:s}.'.format('580'), "green"))
#Z_CURRENT##############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Z_CURRENT {1:s}'.format(os.getcwd(), '580')))
print(colored('Z (mA) RMS current. Multiply by 1.414 for peak current is set to {0:s}.'.format('580'), "green"))
#E0_CURRENT#############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set E0_CURRENT {1:s}'.format(os.getcwd(), '650')))
print(colored('E0 (mA) RMS current. Multiply by 1.414 for peak current is set to {0:s}.'.format('650'), "green"))
#STEALTHCHOP_E#################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_disable STEALTHCHOP_E'.format(os.getcwd())))
print(colored('When disabled, Marlin will use spreadCycle stepping mode, so e0 is disabled', "red"))
#CHOPPER_TIMING#########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set CHOPPER_TIMING {1:s}'.format(os.getcwd(), 'CHOPPER_DEFAULT_24V')))
print(colored('Optimize spreadCycle chopper parameters by using predefined parameter sets, so is set to {0:s}.'.format('CHOPPER_DEFAULT_24V'), "green"))
#USE_CONTROLLER_FAN#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable USE_CONTROLLER_FAN'.format(os.getcwd())))
print(colored('To cool down the stepper drivers and MOSFETs, so is enabled.', "green"))
#CONTROLLER_FAN_EDITABLE################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable CONTROLLER_FAN_EDITABLE'.format(os.getcwd())))
print(colored('Add controller fan menu, so is enabled.', "green"))
#CONTROLLER_FAN_PIN#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set CONTROLLER_FAN_PIN {1:s}'.format(os.getcwd(), 'FAN1_PIN')))
print(colored('controller fan pin is set to {0:s}.'.format('FAN1_PIN'), "green"))
#FAN_KICKSTART_TIME#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set FAN_KICKSTART_TIME {1:s}'.format(os.getcwd(), '200')))
print(colored('This gets the fan spinning reliably, so set to {0:s} ms.'.format('200'), "green"))
#E0_AUTO_FAN_PIN########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set E0_AUTO_FAN_PIN {1:s}'.format(os.getcwd(), 'FAN2_PIN')))
print(colored('e0 fan pin is set to {0:s}.'.format('FAN2_PIN'), "green"))
#BEEP_ON_FEEDRATE_CHANGE################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable BEEP_ON_FEEDRATE_CHANGE'.format(os.getcwd())))
print(colored('Add beep when feedrate changed, so is enabled.', "green"))
#USE_BIG_EDIT_FONT######################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable USE_BIG_EDIT_FONT'.format(os.getcwd())))
print(colored('A bigger font is available for edit items, so is enabled.', "green"))
#USE_SMALL_INFOFONT#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable USE_SMALL_INFOFONT'.format(os.getcwd())))
print(colored('A smaller font may be used on the Info Screen, so is enabled.', "green"))
#OVERLAY_GFX_REVERSE####################################################################################################
# subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable OVERLAY_GFX_REVERSE'.format(os.getcwd())))
# print(colored('A smaller font may be used on the Info Screen, so is enabled.', "green"))
#BABYSTEPPING###########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable BABYSTEPPING DOUBLECLICK_FOR_Z_BABYSTEPPING BABYSTEP_ALWAYS_AVAILABLE BABYSTEP_DISPLAY_TOTAL MOVE_Z_WHEN_IDLE'.format(os.getcwd())))
print(colored('We need babystepping, so is enabled.', "green"))
#BEZIER_CURVE_SUPPORT###################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable BEZIER_CURVE_SUPPORT'.format(os.getcwd())))
print(colored('Support for G5 with XYZE destination and IJPQ offsets, so is enabled.', "green"))
#DIRECT_STEPPING########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable DIRECT_STEPPING'.format(os.getcwd())))
print(colored('It reduces motion calculations, so is enabled.', "green"))
#BAUD_RATE_GCODE########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable BAUD_RATE_GCODE'.format(os.getcwd())))
print(colored('Add M575 G-code to change the baud rate, so is enabled.', "green"))
#ADVANCED_PAUSE_FEATURE#################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable ADVANCED_PAUSE_FEATURE'.format(os.getcwd())))
print(colored('Advanced Pause is enabled.', "green"))
#PHOTO_GCODE############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable PHOTO_GCODE'.format(os.getcwd())))
print(colored('Add the M240 G-code to take a photo, so is enabled.', "green"))
#M115_GEOMETRY_REPORT###################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable M115_GEOMETRY_REPORT'.format(os.getcwd())))
print(colored('Include capabilities in M115 output, so is enabled.', "green"))
#EXPECTED_PRINTER_CHECK#################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable EXPECTED_PRINTER_CHECK'.format(os.getcwd())))
print(colored('M16 with a non-matching string causes the printer to halt, so is enabled.', "green"))
#M100_FREE_MEMORY_WATCHER###############################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable M100_FREE_MEMORY_WATCHER'.format(os.getcwd())))
print(colored('M100 Free Memory Watcher to debug memory usage, so is enabled.', "green"))
#PINS_DEBUGGING#########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable PINS_DEBUGGING'.format(os.getcwd())))
print(colored('M43 - display pin status, toggle pins, watch pins, watch endstops & toggle LED, test servo probe, so is enabled.', "green"))
#PHOTO_SWITCH_MS#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set PHOTO_SWITCH_MS {1:s}'.format(os.getcwd(), '50')))
print(colored('Duration to hold the switch or keep CHDK_PIN high, so set to {0:s} ms.'.format('50'), "green"))





########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

str = '0000'
if None != str:
    send_cmd('echo ::set-output name=RESULT::{0:s}'.format(str))

