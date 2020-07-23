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
        
def append_str(file, text):
    with open(file, "a") as myfile:
        myfile.write(text+'\n')

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

print(colored("""
¨€¨€¨€¨[   ¨€¨€¨€¨[¨€¨€¨€¨€¨€¨€¨€¨[¨€¨€¨€¨€¨€¨€¨€¨[¨€¨€¨€¨€¨€¨€¨[         ¨€¨€¨€¨€¨€¨€¨[ ¨€¨€¨€¨€¨€¨€¨[ ¨€¨€¨€¨€¨€¨€¨[ 
¨€¨€¨€¨€¨[ ¨€¨€¨€¨€¨U¨€¨€¨X¨T¨T¨T¨T¨a¨€¨€¨X¨T¨T¨T¨T¨a¨€¨€¨X¨T¨T¨€¨€¨[        ¨^¨T¨T¨T¨T¨€¨€¨[¨€¨€¨X¨T¨T¨€¨€¨[¨€¨€¨X¨T¨T¨€¨€¨[
¨€¨€¨X¨€¨€¨€¨€¨X¨€¨€¨U¨€¨€¨€¨€¨€¨[  ¨€¨€¨€¨€¨€¨[  ¨€¨€¨€¨€¨€¨€¨X¨a         ¨€¨€¨€¨€¨€¨X¨a¨€¨€¨U  ¨€¨€¨U¨€¨€¨€¨€¨€¨€¨X¨a
¨€¨€¨U¨^¨€¨€¨X¨a¨€¨€¨U¨€¨€¨X¨T¨T¨a  ¨€¨€¨X¨T¨T¨a  ¨€¨€¨X¨T¨T¨€¨€¨[         ¨^¨T¨T¨T¨€¨€¨[¨€¨€¨U  ¨€¨€¨U¨€¨€¨X¨T¨T¨T¨a 
¨€¨€¨U ¨^¨T¨a ¨€¨€¨U¨€¨€¨€¨€¨€¨€¨€¨[¨€¨€¨€¨€¨€¨€¨€¨[¨€¨€¨€¨€¨€¨€¨X¨a¨€¨€¨€¨€¨€¨€¨€¨[¨€¨€¨€¨€¨€¨€¨X¨a¨€¨€¨€¨€¨€¨€¨X¨a¨€¨€¨U     
¨^¨T¨a     ¨^¨T¨a¨^¨T¨T¨T¨T¨T¨T¨a¨^¨T¨T¨T¨T¨T¨T¨a¨^¨T¨T¨T¨T¨T¨a ¨^¨T¨T¨T¨T¨T¨T¨a¨^¨T¨T¨T¨T¨T¨a ¨^¨T¨T¨T¨T¨T¨a ¨^¨T¨a  
""", "green"))

########################################################################################################################
# Configuration.h
########################################################################################################################
print(colored("""
 ¨€¨€¨€¨€¨€¨€¨[ ¨€¨€¨€¨€¨€¨€¨[ ¨€¨€¨€¨[   ¨€¨€¨[¨€¨€¨€¨€¨€¨€¨€¨[¨€¨€¨[ ¨€¨€¨€¨€¨€¨€¨[ 
¨€¨€¨X¨T¨T¨T¨T¨a¨€¨€¨X¨T¨T¨T¨€¨€¨[¨€¨€¨€¨€¨[  ¨€¨€¨U¨€¨€¨X¨T¨T¨T¨T¨a¨€¨€¨U¨€¨€¨X¨T¨T¨T¨T¨a 
¨€¨€¨U     ¨€¨€¨U   ¨€¨€¨U¨€¨€¨X¨€¨€¨[ ¨€¨€¨U¨€¨€¨€¨€¨€¨[  ¨€¨€¨U¨€¨€¨U  ¨€¨€¨€¨[
¨€¨€¨U     ¨€¨€¨U   ¨€¨€¨U¨€¨€¨U¨^¨€¨€¨[¨€¨€¨U¨€¨€¨X¨T¨T¨a  ¨€¨€¨U¨€¨€¨U   ¨€¨€¨U
¨^¨€¨€¨€¨€¨€¨€¨[¨^¨€¨€¨€¨€¨€¨€¨X¨a¨€¨€¨U ¨^¨€¨€¨€¨€¨U¨€¨€¨U     ¨€¨€¨U¨^¨€¨€¨€¨€¨€¨€¨X¨a
 ¨^¨T¨T¨T¨T¨T¨a ¨^¨T¨T¨T¨T¨T¨a ¨^¨T¨a  ¨^¨T¨T¨T¨a¨^¨T¨a     ¨^¨T¨a ¨^¨T¨T¨T¨T¨T¨a         
""", "white"))
#STRING_CONFIG_H_AUTHOR#################################################################################################
replaceAll('{0:s}/Marlin/Configuration.h'.format(os.getcwd()), '(none, default config)', '(ccrobot-online, MEEB_3DP)')
print(colored('The author of the config file is {0:s}'.format('ccccmagicboy'), "green"))
#SHOW_CUSTOM_BOOTSCREEN#################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable SHOW_CUSTOM_BOOTSCREEN'.format(os.getcwd())))
print(colored('The custom bootscreen is enabled', "green"))
#SHOW_BOOTSCREEN########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_disable SHOW_BOOTSCREEN'.format(os.getcwd())))
print(colored('The marlin logo is disabled', "red"))
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
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set MOTHERBOARD {1:s}'.format(os.getcwd(), os.environ['INPUT_BOARD'])))
print(colored('The select board is {0:s}'.format(os.environ['INPUT_BOARD']), "green"))
#CUSTOM_MACHINE_NAME####################################################################################################
replaceAll('{0:s}/Marlin/Configuration.h'.format(os.getcwd()), '//#define CUSTOM_MACHINE_NAME "3D Printer"', '#define CUSTOM_MACHINE_NAME "Slider"')
print(colored('The machine name is {0:s}'.format('Slider'), "green"))
#MACHINE_UUID###########################################################################################################
replaceAll('{0:s}/Marlin/Configuration.h'.format(os.getcwd()), '//#define MACHINE_UUID "00000000-0000-0000-0000-000000000000"', '#define MACHINE_UUID "9cddc618-9fca-11ea-bb37-0242ac130002"')
print(colored('The machine uuid is {0:s}'.format('9cddc618-9fca-11ea-bb37-0242ac130002'), "green"))
#TEMP_SENSOR_0##########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set TEMP_SENSOR_0 {1:s}'.format(os.getcwd(), '999')))
print(colored('The temperature sensor 0 is {0:s}'.format('999'), "green"))
#TEMP_SENSOR_BED########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set TEMP_SENSOR_BED {1:s}'.format(os.getcwd(), '998')))
print(colored('The temperature bed is {0:s}'.format('998'), "green"))
#ENDSTOPPULLUPS#########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable ENDSTOPPULLUPS'.format(os.getcwd())))
print(colored('The endstop pull-up resistors are enabled', "green"))
#ENDSTOP_INTERRUPTS_FEATURE#############################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable ENDSTOP_INTERRUPTS_FEATURE'.format(os.getcwd())))
print(colored('The endstop interrupt feature is enabled', "green"))
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
replaceAll('{0:s}/Marlin/Configuration.h'.format(os.getcwd()), 'DEFAULT_AXIS_STEPS_PER_UNIT   { 80, 80, 4000, 500 }', 'DEFAULT_AXIS_STEPS_PER_UNIT   { 80, 80, 100, 97.5 }')
print(colored('The default step/mm is set to {0:s}'.format('{ 80, 80, 100, 97.5 }'), "green"))
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
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Z_AFTER_HOMING {1:s}'.format(os.getcwd(), '0')))
print(colored('The z after homing is set to {0:s} mm.'.format('0'), "green"))
#Z_MAX_POS##############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Z_MAX_POS {1:s}'.format(os.getcwd(), '400')))
print(colored('The z max is set to {0:s} mm.'.format('400'), "green"))
#LCD_LANGUAGE###########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set LCD_LANGUAGE {1:s}'.format(os.getcwd(), os.environ['INPUT_LCD_LANGUAGE'])))
print(colored('The language of LCD is set to {0:s}.'.format(os.environ['INPUT_LCD_LANGUAGE']), "green"))
#NEOPIXEL_LED###########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable NEOPIXEL_LED'.format(os.getcwd())))
print(colored('The neopixel led is enabled', "green"))
#NEOPIXEL_PIN###########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_disable NEOPIXEL_PIN'.format(os.getcwd())))
print(colored('The neopixel led pin is define in board file, and here it is disabled', "red"))
#NEOPIXEL_BRIGHTNESS####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set NEOPIXEL_BRIGHTNESS {1:s}'.format(os.getcwd(), '80')))
print(colored('The Initial brightness of neopixel led is set to {0:s}.'.format('80'), "green"))
#NEOPIXEL_TYPE##########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set NEOPIXEL_TYPE {1:s}'.format(os.getcwd(), 'NEO_GRB')))
print(colored('The type of neopixel led is set to {0:s}.'.format('NEO_GRB'), "green"))
#NEOPIXEL_PIXELS########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set NEOPIXEL_PIXELS {1:s}'.format(os.getcwd(), '17')))
print(colored('The number of neopixel led is set to {0:s}.'.format('17'), "green"))
#NEOPIXEL_IS_SEQUENTIAL#################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_disable NEOPIXEL_IS_SEQUENTIAL'.format(os.getcwd())))
print(colored('The neopixel sequential is disabled', "red"))
#NEOPIXEL_STARTUP_TEST##################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable NEOPIXEL_STARTUP_TEST'.format(os.getcwd())))
print(colored('The neopixel led startup test is enabled', "green"))
#HOMING_FEEDRATE_Z######################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set HOMING_FEEDRATE_Z {1:s}'.format(os.getcwd(), '(25*60)')))
print(colored('z axis homing speed is set to {0:s}.'.format('(25*60)'), "green"))



########################################################################################################################
########################################################################################################################
########################################################################################################################
# Configuration_adv.h
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
print(colored("""
 ¨€¨€¨€¨€¨€¨€¨[ ¨€¨€¨€¨€¨€¨€¨[ ¨€¨€¨€¨[   ¨€¨€¨[¨€¨€¨€¨€¨€¨€¨€¨[¨€¨€¨[ ¨€¨€¨€¨€¨€¨€¨[      ¨€¨€¨€¨€¨€¨[ ¨€¨€¨€¨€¨€¨€¨[ ¨€¨€¨[   ¨€¨€¨[
¨€¨€¨X¨T¨T¨T¨T¨a¨€¨€¨X¨T¨T¨T¨€¨€¨[¨€¨€¨€¨€¨[  ¨€¨€¨U¨€¨€¨X¨T¨T¨T¨T¨a¨€¨€¨U¨€¨€¨X¨T¨T¨T¨T¨a     ¨€¨€¨X¨T¨T¨€¨€¨[¨€¨€¨X¨T¨T¨€¨€¨[¨€¨€¨U   ¨€¨€¨U
¨€¨€¨U     ¨€¨€¨U   ¨€¨€¨U¨€¨€¨X¨€¨€¨[ ¨€¨€¨U¨€¨€¨€¨€¨€¨[  ¨€¨€¨U¨€¨€¨U  ¨€¨€¨€¨[    ¨€¨€¨€¨€¨€¨€¨€¨U¨€¨€¨U  ¨€¨€¨U¨€¨€¨U   ¨€¨€¨U
¨€¨€¨U     ¨€¨€¨U   ¨€¨€¨U¨€¨€¨U¨^¨€¨€¨[¨€¨€¨U¨€¨€¨X¨T¨T¨a  ¨€¨€¨U¨€¨€¨U   ¨€¨€¨U    ¨€¨€¨X¨T¨T¨€¨€¨U¨€¨€¨U  ¨€¨€¨U¨^¨€¨€¨[ ¨€¨€¨X¨a
¨^¨€¨€¨€¨€¨€¨€¨[¨^¨€¨€¨€¨€¨€¨€¨X¨a¨€¨€¨U ¨^¨€¨€¨€¨€¨U¨€¨€¨U     ¨€¨€¨U¨^¨€¨€¨€¨€¨€¨€¨X¨a    ¨€¨€¨U  ¨€¨€¨U¨€¨€¨€¨€¨€¨€¨X¨a ¨^¨€¨€¨€¨€¨X¨a 
 ¨^¨T¨T¨T¨T¨T¨a ¨^¨T¨T¨T¨T¨T¨a ¨^¨T¨a  ¨^¨T¨T¨T¨a¨^¨T¨a     ¨^¨T¨a ¨^¨T¨T¨T¨T¨T¨a     ¨^¨T¨a  ¨^¨T¨a¨^¨T¨T¨T¨T¨T¨a   ¨^¨T¨T¨T¨a  
""", "white"))
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
#LCD_INFO_MENU##########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable LCD_INFO_MENU'.format(os.getcwd())))
print(colored('Include a page of printer information in the LCD Main Menu, so is enabled', "green"))
#TURBO_BACK_MENU_ITEM###################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable TURBO_BACK_MENU_ITEM'.format(os.getcwd())))
print(colored('BACK menu items keep the highlight at the top, so is enabled', "green"))
#LED_CONTROL_MENU#######################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable LED_CONTROL_MENU LED_USER_PRESET_STARTUP'.format(os.getcwd())))
print(colored('Add LED Control to the LCD menu, so is enabled', "green"))
#LED_USER_PRESET_RED####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set LED_USER_PRESET_RED {1:s}'.format(os.getcwd(), '0')))
print(colored('User preset red is set to {0:s}.'.format('0'), "green"))
#LED_USER_PRESET_GREEN##################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set LED_USER_PRESET_GREEN {1:s}'.format(os.getcwd(), '0')))
print(colored('User preset green is set to {0:s}.'.format('0'), "green"))
#LED_USER_PRESET_BLUE###################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set LED_USER_PRESET_BLUE {1:s}'.format(os.getcwd(), '0')))
print(colored('User preset blue is set to {0:s}.'.format('0'), "green"))
#MONITOR_DRIVER_STATUS##################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable MONITOR_DRIVER_STATUS'.format(os.getcwd())))
print(colored('Monitor Trinamic drivers, so is enabled', "green"))
#TMC_DEBUG##############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable TMC_DEBUG'.format(os.getcwd())))
print(colored('Enable M122 debugging command for TMC stepper drivers, so is enabled', "green"))
#BUFSIZE################################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set BUFSIZE {1:s}'.format(os.getcwd(), '32')))
print(colored('The ASCII buffer for serial input is set to {0:s}.'.format('32'), "green"))
#TX_BUFFER_SIZE#########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set TX_BUFFER_SIZE {1:s}'.format(os.getcwd(), '32')))
print(colored('Transmission to Host Buffer Size is set to {0:s}.'.format('32'), "green"))
#RX_BUFFER_SIZE#########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set RX_BUFFER_SIZE {1:s}'.format(os.getcwd(), '32')))
print(colored('RX Buffer Size is set to {0:s}.'.format('32'), "green"))
#Z_MICROSTEPS###########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Z_MICROSTEPS {1:s}'.format(os.getcwd(), '16')))
print(colored('Z microsteps is set to {0:s}.'.format('16'), "green"))
#HYBRID_THRESHOLD#######################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_disable HYBRID_THRESHOLD'.format(os.getcwd())))
print(colored('The driver will switch to spreadCycle when stepper speed is over HYBRID_THRESHOLD, but size effect for e axis, so is disabled.', "red"))
#X_HYBRID_THRESHOLD#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set X_HYBRID_THRESHOLD {1:s}'.format(os.getcwd(), '130')))
print(colored('X motor hybrid threshold is set to {0:s}mm/s.'.format('130'), "green"))
#Y_HYBRID_THRESHOLD#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Y_HYBRID_THRESHOLD {1:s}'.format(os.getcwd(), '130')))
print(colored('Y motor hybrid threshold is set to {0:s}mm/s.'.format('130'), "green"))
#Z_HYBRID_THRESHOLD#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Z_HYBRID_THRESHOLD {1:s}'.format(os.getcwd(), '35')))
print(colored('Z motor hybrid threshold is set to {0:s}mm/s.'.format('35'), "green"))
#E0_HYBRID_THRESHOLD####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set E0_HYBRID_THRESHOLD {1:s}'.format(os.getcwd(), '35')))
print(colored('E0 motor hybrid threshold is set to {0:s}mm/s.'.format('35'), "green"))
#X_RSENSE###############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set X_RSENSE {1:s}'.format(os.getcwd(), '0.1')))
print(colored('X Rsense is set to {0:s}.'.format('0.1'), "green"))
#Y_RSENSE###############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Y_RSENSE {1:s}'.format(os.getcwd(), '0.1')))
print(colored('Y Rsense is set to {0:s}.'.format('0.1'), "green"))
#Z_RSENSE###############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Z_RSENSE {1:s}'.format(os.getcwd(), '0.1')))
print(colored('Z Rsense is set to {0:s}.'.format('0.1'), "green"))
#E0_RSENSE##############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set E0_RSENSE {1:s}'.format(os.getcwd(), '0.1')))
print(colored('E0 Rsense is set to {0:s}.'.format('0.1'), "green"))
#X_CURRENT##############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set X_CURRENT {1:s}'.format(os.getcwd(), '900')))
print(colored('X (mA) RMS current. Multiply by 1.414 for peak current is set to {0:s}.'.format('900'), "green"))
#Y_CURRENT##############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Y_CURRENT {1:s}'.format(os.getcwd(), '900')))
print(colored('Y (mA) RMS current. Multiply by 1.414 for peak current is set to {0:s}.'.format('900'), "green"))
#Z_CURRENT##############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set Z_CURRENT {1:s}'.format(os.getcwd(), '900')))
print(colored('Z (mA) RMS current. Multiply by 1.414 for peak current is set to {0:s}.'.format('900'), "green"))
#E0_CURRENT#############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set E0_CURRENT {1:s}'.format(os.getcwd(), '900')))
print(colored('E0 (mA) RMS current. Multiply by 1.414 for peak current is set to {0:s}.'.format('900'), "green"))
#TMC_HOME_PHASE#########################################################################################################
replaceAll('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '//#define TMC_HOME_PHASE { 896, 896, 896 }', '#define TMC_HOME_PHASE { 896, 896, 896 }')
print(colored('Improve homing repeatability by homing to stepper coil nearest absolute, so is set to {0:s}.'.format('{ 896, 896, 896 }'), "green"))
#SOFTWARE_DRIVER_ENABLE#################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_disable SOFTWARE_DRIVER_ENABLE'.format(os.getcwd())))
print(colored('Use for drivers that do not use a dedicated enable pin to save the pin numbers, but is disabled.', "red"))
#STEALTHCHOP_E##########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_disable STEALTHCHOP_E'.format(os.getcwd())))
print(colored('When disabled, Marlin will use spreadCycle stepping mode, so e0 is disabled', "red"))
#CHOPPER_TIMING#######################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set CHOPPER_TIMING {1:s}'.format(os.getcwd(), 'CHOPPER_DEFAULT_12V')))
print(colored('Optimize spreadCycle chopper parameters by using predefined parameter sets, so is set to {0:s}.'.format('CHOPPER_DEFAULT_12V'), "green"))
#USE_BIG_EDIT_FONT######################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable USE_BIG_EDIT_FONT'.format(os.getcwd())))
print(colored('A bigger font is available for edit items, so is enabled.', "green"))
#USE_SMALL_INFOFONT#####################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_disable USE_SMALL_INFOFONT'.format(os.getcwd())))
print(colored('A smaller font may be used on the Info Screen, so is disabled.', "red"))
#PHOTO_GCODE############################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable PHOTO_GCODE'.format(os.getcwd())))
print(colored('Add the M240 G-code to take a photo, so is enabled.', "green"))
#PHOTO_POSITION#########################################################################################################
replaceAll('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '//#define PHOTO_POSITION { X_MAX_POS - 5, Y_MAX_POS, 0 }', '#define PHOTO_POSITION { X_MAX_POS - 5, Y_MAX_POS, 2 }')
print(colored('Set the photo position.', "green"))
#PHOTO_DELAY_MS#########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set PHOTO_DELAY_MS {1:s}'.format(os.getcwd(), '100')))
print(colored('Duration to pause before moving back is set to {0:s} ms.'.format('100'), "green"))
#PHOTO_RETRACT_MM#######################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set PHOTO_RETRACT_MM {1:s}'.format(os.getcwd(), '4.2')))
print(colored('E retract/recover for the photo move is set to {0:s} mm.'.format('4.2'), "green"))
#PHOTO_SWITCH_MS########################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_set PHOTO_SWITCH_MS {1:s}'.format(os.getcwd(), '50')))
print(colored('Duration to hold the switch or keep CHDK_PIN high, so set to {0:s} ms.'.format('50'), "green"))
#EXPECTED_PRINTER_CHECK#################################################################################################
subprocess.call(shlex.split('{0:s}/buildroot/bin/opt_enable EXPECTED_PRINTER_CHECK'.format(os.getcwd())))
print(colored('M16 with a non-matching string causes the printer to halt, so is enabled.', "green"))
#STARTUP_COMMANDS#######################################################################################################
replaceAll('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '//#define STARTUP_COMMANDS "M17 Z"', '#define STARTUP_COMMANDS "M300 S5000 P300"')
print(colored('beep when start.', "green"))
#RESET##################################################################################################################
replaceAll('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_5 "Home & Info"', '#define USER_DESC_5 "Reset"')
replaceAll('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_5 "G28', '#define USER_GCODE_5 "M997')
print(colored('Add reset the board menu command', "green"))

#USER 6#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_6 "test1"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_6 "M997"')
#USER 7#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_7 "test2"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_7 "M997"')
#USER 8#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_8 "test2"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_8 "M997"')
#USER 9#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_9 "test2"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_9 "M997"')
#USER 10#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_10 "test2"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_10 "M997"')
#USER 11#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_11 "test2"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_11 "M997"')

#USER 12#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_12 "test1"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_12 "M997"')
#USER 13#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_13 "test2"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_13 "M997"')
#USER 14#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_14 "test2"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_14 "M997"')
#USER 15#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_15 "test2"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_15 "M997"')
#USER 16#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_16 "test2"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_16 "M997"')
#USER 17#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_17 "test2"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_17 "M997"')

#USER 18#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_18 "test1"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_18 "M997"')
#USER 19#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_19 "test2"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_19 "M997"')
#USER 20#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_20 "test2"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_20 "M997"')
#USER 21#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_21 "test2"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_21 "M997"')
#USER 22#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_22 "test2"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_22 "M997"')
#USER 23#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_23 "test2"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_23 "M997"')
#USER 24#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_24 "test2"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_24 "M997"')
#USER 25#################################################################################################################
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_DESC_25 "test2"')
append_str('{0:s}/Marlin/Configuration_adv.h'.format(os.getcwd()), '#define USER_GCODE_25 "M997"')
########################################################################################################################

########################################################################################################################

str = '0000'
if None != str:
    send_cmd('echo ::set-output name=RESULT::{0:s}'.format(str))

