from pwn import *

HOST = "pwnable.kr"
PASS = "guest"
USER = "col"
PORT = 2222

payload = p32(0x6c5cec8) * 4 + p32(0x6c5cecc)

shell = ssh(user=USER, password=PASS, host=HOST, port=PORT)
process = shell.process(executable='./col', argv=['col',payload])
print(process.recvline())