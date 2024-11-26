'''Akhon amra arektu advance topic e moveon korbo. Ekhane Akdom machine level code niye kaj kora hobe. Python oneek versalite akta language. Jeta amader
ke machine language e convert korteo help kore. Apadato aita ke direct machine language nh bole sob theke besi preferable word shellcode bolbo. Ba aitake 
opCode oh bola jay. Now ai part e amra akta shellcode ke kivabe directly execute kora jay seta dekbo. porer bar dekbo kivabe shellcode ke binary file
e convert kora jay, then dekbo kivabe assembly code ke shellcode e convert kora jay'''
from pwn import *
import sys

context(os='linux',arch='amd64',log_level='error')
run_shellcode(unhex(sys.argv[1])).interactive() # ekhane amader pass kora first argument hobe shellcode tah.

'''Ekhane first argument hisabe amra jodi shellcode pass kori tahole amder ke python sei shellcode tah execute kore dibe'''