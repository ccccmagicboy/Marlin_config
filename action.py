import os

def send_cmd(command):
    print(command)
    result_str = os.popen(command).read()
    print(result_str)
    return result_str

print(os.listdir(os.getcwd()))

send_cmd('export PATH=/home/runner/work/MEEB_3DP/MEEB_3DP/my_marlin/buildroot/bin:$PATH')
send_cmd('restore_configs')
send_cmd('opt_set MOTHERBOARD {0:s}'.format(os.environ['BOARD']))
print('The select board is {0:s}'.format(os.environ['BOARD']))

str = '0000'
if None != str:
    send_cmd('echo ::set-output name=RESULT::{0:s}'.format(str))

