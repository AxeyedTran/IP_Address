xl = '\033[1;92m'
v = '\033[1;93m'
xn = '\0331;96m'
t = '\033[1;97m'
import os, sys, time
os.system('pip install requests')
time.sleep(1)
logo = """
\033[1;96m  ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
\033[1;92m  ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
\033[1;93m  ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
\033[1;96m  ██║     ██║   ██║██║   ██║██║██║╚██╗██║
\033[1;92m  ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
\033[1;93m  ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝
\033[1;96m                        Axeyed Tran
"""
def write(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)
cusr = 'Axeyed'
cpwd = 'Tran'

def u():
    os.system('clear')
    print(logo)
    usr = input(t+'Username >> ')
    if usr == cusr:
        p()
    else:
        os.system('clear')
        print (logo)
        print ('Username >> ' + usr + ' [Wrong]')
        time.sleep(1)
        os.system('xdg-open https://www.facebook.com/Axeyed.Tran191')
        u()


def p():
    os.system('clear')
    print (logo)
    print ('Username >> Axeyed [Correct]')
    pwd = input('Password >> ')
    if pwd == cpwd:
        z()
    else:
        os.system('clear')
        print (logo)
        print ('Username >> Axeyed [Correct]')
        print ('Password >> ' + pwd + ' [Wrong]')
        time.sleep(1)
        os.system('xdg-open https://www.facebook.com/Axeyed.Tran191')
        p()


def z():
    os.system('clear')
    print (logo)
    print ('Username >> Axeyed [Correct]')
    print ('Password >>  Tran [Correct]')
    print (' \x1b[1;92mLogin Successfull As Axeyed Tran\x1b[0m')
    write('\x1b[1;93mPlease Wait a Minutes, All Packages Are Checking...')
    time.sleep(3)
    os.system('python .IP.py')
if __name__ == '__main__':
    u()