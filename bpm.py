import pexpect
import time
import struct

child = pexpect.spawn("sudo gatttool -b 18:7A:93:12:13:F0 -I")

print("Connecting to Rossmax BPM")
child.sendline("connect")
child.expect("Connection successful", timeout=5)
print(" Connected!")
