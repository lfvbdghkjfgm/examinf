from pwn import *
import re
from base64 import b64decode,b32decode
from base58 import b58decode

r = remote("tasks.ctfd.infosec.moscow", 20037)

def caesar(st,sd=23):
    alf = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for i in st:
        d = i.isupper()
        i = i.lower()
        if i not in alf:
            res+=i
        else:
            c =  alf[(alf.index(i)+sd)%len(alf)]
            if d:
                c = c.upper()
            res+=c
    return res

def atbash(st):
    alf = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for i in st:
        d = i.isupper()
        i = i.lower()
        if i not in alf:
            res+=i
        else:
            c =  alf[-alf.index(i)-1]
            if d:
                c = c.upper()
            res+=c
    return res


while True:

    a = r.recv().decode()
    print(a)
    payl = ''
    m = re.findall('"(.+?)"',a)
    if m[1] == 'unicode_escape':
        payl = m[3].encode('utf-8').decode('unicode-escape')
    elif m[1] == 'caesar':
        payl = caesar(m[3])
    elif 'rot' in m[1]:
        s = re.findall(r'\d+',m[1])
        if s:
            payl = caesar(m[3],26-int(s[0]))
        else:
            payl = caesar(m[3],13)
    elif m[1] == 'base64':
        payl = b64decode(m[3]).decode()
    elif m[1] == 'binary':
        for i in m[3].split():
            payl+=chr(int(i,2))
    elif m[1] == 'base58':
        payl = b58decode(m[3]).decode()
    elif m[1] == 'bigint':
        payl = bytes.fromhex(m[3][2:]).decode()
    elif m[1] == 'hex':
        payl = bytes.fromhex(m[3]).decode()
    elif m[1] == 'atbash':
        payl = atbash(m[3])
    elif m[1] == 'base32':
        payl = b32decode(m[3]).decode()
    elif m[1] == 'utf-8':
        payl = bytes(eval(m[3])).decode()
    elif m[1] == 'xor0x42':
        st = bytes([i^0x42 for i in m[3].encode()]).decode()[5:]
        if st.index(' ') == 1:
            payl = 'A' + st[1:]
        else:
            payl = 'The' + st[3:]
        print(payl)
    elif m[1] == 'reverse':
        payl = m[3][::-1]
    else:
        break
    r.sendline(('{"decoded": "'+ payl+'"}').encode())
