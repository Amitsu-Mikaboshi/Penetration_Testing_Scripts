'''Shellcode ke amra chaile executable binary file e convert kore nite pari. Aitar subidha hobe amra tahole dynamic ba static analysis er jono binary file
peye jabo. Means amader ke jodi opcode/shellcode deowa thake tahole amra seta ke binary file e convert kore analysis chaite parbo. Opcode e analysis
chalano almost impossible until amra sei OPcode ke binary file e convert kore nicchi.'''

from pwn import *
import sys,os,stat
context(os='linux',arch='amd64',log_level='error')
ELF.from_bytes(unhex(sys.argv[1])).save(sys.argv[2])
os.chmod(sys.argv[2], stat.S_IEXEC)

'''ei python script er kaj hocche amader theke duita argument nibe. First argument hocche amader targeted opcode/shellcode then second argument hobe
amader output binary file er ki name dibo seta. Tahole amader shellcode binary code e convert hobe and aki satey binary file tah tey executable permission
set hoye jabe'''