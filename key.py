import os
import sys
import time

w = '\x1b[97;4m'
m = '\x1b[91;1m'
h = '\x1b[92;1m'
k = '\x1b[93;1m'
u = '\x1b[94;1m'
p = '\x1b[95;1m'
a = '\x1b[96;1m'
s = '\x1b[97;1m'
b = '\x1b[30;2m'
n = '\x1b[30;0m'
zz = ['.   ', '..  ', '... ', '.... ', '.....\n']
logo = '\n\x1b[1;92m                 ╦╔═╔═╗╦ ╦\n\x1b[1;92m                 ╠╩╗║╣ ╚╦╝\n\x1b[1;92m                 ╩ ╩╚═╝ ╩ \n\x1b[1;97m╔═════════════════════════════════════════╗\n\x1b[1;97m║\x1b[1;93m* \x1b[1;97m Author \x1b[1;91m: \x1b[1;97m Angga                       ║\n\x1b[1;97m║\x1b[1;93m* \x1b[1;97m Wa \x1b[1;91m    : \x1b[1;97m 082211661007                ║\n\x1b[1;97m║\x1b[1;93m* \x1b[1;97m Github \x1b[1;91m: \x1b[1;97m Https://Github.com/Mr-XsZ   ║\n\x1b[1;97m╚═════════════════════════════════════════╝\n'

def menu():
    lagi = 'y'
    while 1:
        if lagi == 'y':
            print(h, logo)
            print('\n{}1. {}Standart\n{}2. {}My Version\n{}99. {}Exit`\n'.format(m, k, m, k, m, k, m, k))
            pil = int(input('\n{}[{}+{}] Masukkan Pilihan:{} '.format(h, m, h, a)))
            if pil == 1:
                stndrt()
            if pil == 2:
                myv()
            if pil == 99:
                thx()
                sys.exit(1)
            lagi = input('{}[{}*{}]Kembali ke Menu??{}[{}y/n{}]{}:{} '.format(h, m, h, u, m, u, h, a))


def stndrt():
    a = '\x1b[92m'
    b = '\x1b[91m'
    c = '\x1b[0m'
    os.system('clear')
    print((a + '\t  Key for help you'))
    print((b + '\t    By Angga'))
    print('\t Subcribe channel : https://www.youtube.com/channel/UCLU9H65QrIC6u2UetU6476w ')
    print((a + '++++++++++++++++++++++++++++++++++++++++'))
    print('\nProses..')
    time.sleep(1)
    print((b + '\n[!] Making termux properties directory..'))
    time.sleep(1)
    try:
        os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
        pass

    print((a + '[!]Success !'))
    time.sleep(1)
    print((b + '\n[!] Making setup file..'))
    time.sleep(1)
    key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    kontol = open('/data/data/com.termux/files/home/.termux/termux.properties', 'w')
    kontol.write(key)
    kontol.close()
    time.sleep(1)
    print((a + '[!] Success !'))
    time.sleep(1)
    print((b + '\n[!] Setting up..'))
    time.sleep(2)
    os.system('termux-reload-settings')
    print((a + '[!] Successfully !! ^^' + c + '\n\nSupport dgn cara subcribe channel saya  : https://www.youtube.com/channel/UCLU9H65QrIC6u2UetU6476w \n\n'))


def myv():
    a = '\x1b[92m'
    b = '\x1b[91m'
    c = '\x1b[0m'
    os.system('clear')
    print((a + '\t  Shorcut for help you'))
    print((b + '\t    By Angga'))
    print('\t Subcribe channel : https://www.youtube.com/channel/UCLU9H65QrIC6u2UetU6476w ')
    print((a + '++++++++++++++++++++++++++++++++++++++++'))
    print('\nProses..')
    time.sleep(1)
    print((b + '\n[!] Making termux properties directory..'))
    time.sleep(1)
    try:
        os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
        pass

    print((a + '[!]Success !'))
    time.sleep(1)
    print((b + '\n[!] Making setup file..'))
    time.sleep(1)
    key = "extra-keys = [['ESC','/','-','HOME','END','UP'],['TAB','CTRL','ALT','LEFT','RIGHT','DOWN','PGDN']]"
    kontol = open('/data/data/com.termux/files/home/.termux/termux.properties', 'w')
    kontol.write(key)
    kontol.close()
    time.sleep(1)
    print((a + '[!] Success !'))
    time.sleep(1)
    print((b + '\n[!] Setting up..'))
    time.sleep(2)
    os.system('termux-reload-settings')
    print((a + '[!] Successfully !! ^^' + c + '\n\nSupport dgn cara subcribe channel saya  : https://www.youtube.com/channel/UCLU9H65QrIC6u2UetU6476w \n\n'))


def thx():
    print(w, 'Thanks for use!', n)
    print(u)
    os.system('figlet Thanks for use !')
    print(s)
    with open('README.md') as (md):
        print(md.read())
        md.close


if __name__ == '__main__':
    menu()
