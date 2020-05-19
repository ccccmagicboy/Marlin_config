import os
import sys
import subprocess
import shlex
from termcolor import colored
import fileinput
from shutil import copyfile

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

# cp _Statusscreen.h and _Bootscreen.h
src = os.path.join('{0:s}/Marlin_v2/_Statusscreen.h'.format(os.getcwd()))
dst = os.path.join('{0:s}/my_marlin/Marlin'.format(os.getcwd()))
copy(src, dst)
src = os.path.join('{0:s}/Marlin_v2/_Bootscreen.h'.format(os.getcwd()))
dst = os.path.join('{0:s}/my_marlin/Marlin'.format(os.getcwd()))
copy(src, dst)

os.chdir('my_marlin')

# replaceAll(mk_path, "#webrepl.start()","import machine;".format(str))
# opt_add
# opt_enable
# opt_disable
# opt_set

subprocess.call(['{0:s}/buildroot/bin/restore_configs'.format(os.getcwd())])
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
#PIDTEMPBED#############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable PIDTEMPBED'.format(os.getcwd())))
print(colored('The bed pid is enabled', "green"))
#EXTRUDE_MAXLENGTH################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set EXTRUDE_MAXLENGTH {1:s}'.format(os.getcwd(), '450')))
print(colored('The max extrude lengthy is set to {0:s}'.format('450'), "green"))
#THERMAL_PROTECTION_CHAMBER################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_disable THERMAL_PROTECTION_CHAMBER'.format(os.getcwd())))
print(colored('The chamber thermal protection is disabled', "red"))
#ENDSTOPPULLUPS#########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable ENDSTOPPULLUPS'.format(os.getcwd())))
print(colored('The endstop pull-up resistor are enabled', "green"))
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
#Z_AFTER_HOMING########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Z_AFTER_HOMING {1:s}'.format(os.getcwd(), '10')))
print(colored('The z after homing is set to {0:s} mm.'.format('10'), "green"))
#X_BED_SIZE########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set X_BED_SIZE {1:s}'.format(os.getcwd(), '235')))
print(colored('The x bed size is set to {0:s} mm.'.format('235'), "green"))
#Y_BED_SIZE########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Y_BED_SIZE {1:s}'.format(os.getcwd(), '235')))
print(colored('The y bed size is set ot {0:s} mm.'.format('235'), "green"))
#Z_MAX_POS########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Z_MAX_POS {1:s}'.format(os.getcwd(), '240')))
print(colored('The z max is set to {0:s} mm.'.format('240'), "green"))
#LEVEL_BED_CORNERS#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable LEVEL_BED_CORNERS'.format(os.getcwd())))
print(colored('The manunal z bed corners leveling is enabled', "green"))
#LEVEL_CENTER_TOO#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable LEVEL_CENTER_TOO'.format(os.getcwd())))
print(colored('The manunal z bed corners leveling center point is enabled', "green"))
#Z_SAFE_HOMING#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable Z_SAFE_HOMING'.format(os.getcwd())))
print(colored('The z safe homing is enabled', "green"))
#NOZZLE_PARK_FEATURE#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable NOZZLE_PARK_FEATURE'.format(os.getcwd())))
print(colored('The nozzle park feature is enabled', "green"))
#NOZZLE_PARK_POINT########################################################################################################
replaceAll('{0:s}/Marlin/Configuration.h'.format(os.getcwd()), '{ (X_MIN_POS + 0), (Y_MIN_POS + 0), 40 }', '{ (X_MIN_POS + 10), (Y_MAX_POS - 10), 20 }')
print(colored('The nozzle park point is set to {0:s}.'.format('{ (X_MIN_POS + 10), (Y_MAX_POS - 10), 20 }'), "green"))
#INDIVIDUAL_AXIS_HOMING_MENU#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable INDIVIDUAL_AXIS_HOMING_MENU'.format(os.getcwd())))
print(colored('The lcd individual axis homing menu is enabled', "green"))
#CR10_STOCKDISPLAY#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable CR10_STOCKDISPLAY'.format(os.getcwd())))
print(colored('The ender-3 stockdisplay is enabled', "green"))
#NEOPIXEL_LED#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable NEOPIXEL_LED'.format(os.getcwd())))
print(colored('The neopixel led is enabled', "green"))
#NEOPIXEL_PIN#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_disable NEOPIXEL_PIN'.format(os.getcwd())))
print(colored('The neopixel led pin is define in board file, and here it is disabled', "red"))
#NEOPIXEL_BRIGHTNESS########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set NEOPIXEL_BRIGHTNESS {1:s}'.format(os.getcwd(), '30')))
print(colored('The Initial brightness of neopixel led is set to {0:s}.'.format('30'), "green"))
#NEOPIXEL_TYPE########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set NEOPIXEL_TYPE {1:s}'.format(os.getcwd(), 'NEO_GRB')))
print(colored('The type of neopixel led is set to {0:s}.'.format('NEO_GRB'), "green"))
#NEOPIXEL_PIXELS########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set NEOPIXEL_PIXELS {1:s}'.format(os.getcwd(), '1')))
print(colored('The number of neopixel led is set to {0:s}.'.format('1'), "green"))
#NEOPIXEL_IS_SEQUENTIAL################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_disable NEOPIXEL_IS_SEQUENTIAL'.format(os.getcwd())))
print(colored('The neopixel sequential is disabled', "red"))
#NEOPIXEL_STARTUP_TEST#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable NEOPIXEL_STARTUP_TEST'.format(os.getcwd())))
print(colored('The neopixel led startup test is enabled', "green"))
########################################################################################################################
########################################################################################################################
# Configuration_adv.h
########################################################################################################################

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

