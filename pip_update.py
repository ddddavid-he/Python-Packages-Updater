import subprocess
import tempfile
import locale
from subprocess import call


cmd = ['pip', 'list', '-o']
with tempfile.TemporaryFile() as temp:
    proc = subprocess.Popen(cmd, stdout=temp)
    proc.wait()
    temp.seek(0)
    encode_type = locale.getpreferredencoding()
    if encode_type == 'UTF-8':
        output = temp.read().decode('utf-8')
    elif encode_type == 'cp936' or 'GBK':
        output = temp.read().decode('gbk')

if output is None:
    exit()
else:
    output = output.split('\n')[2:]

update_list = [i.split(' ')[0] for i in output]

if len(update_list) == 0:
    print('All packages are up-to-date.')
else:
    file = open('updated_log.txt', 'w+')
    print('\n\n\nUpdates below are avaliable.\n')
    for i in output:
        print(i)
        file.write(i+'\n')

    det = input('\n Upgrade all?[y/n]')

    while 1:
        if det == 'y':
            for i in update_list:
                call('pip install --upgrade '+i, shell=True)
                print('\n')
            break
        elif det == 'n':
            break
        else:
            pass

    print('\n\n'+'-'*20)
    print(str(len(update_list))+' packages have been updated.\n'
                           'update log have been saved in updated_log.txt')



