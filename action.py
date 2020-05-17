import os
import sys
import subprocess

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

send_cmd('restore_configs')
send_cmd('opt_set MOTHERBOARD {0:s}'.format(os.environ['BOARD']))
print('The select board is {0:s}'.format(os.environ['BOARD']))

str = '0000'
if None != str:
    send_cmd('echo ::set-output name=RESULT::{0:s}'.format(str))

