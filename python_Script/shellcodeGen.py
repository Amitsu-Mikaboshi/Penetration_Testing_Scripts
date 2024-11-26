'''Ekhane amra binary file theke kivabe shellcode generate korte hoy tah dekbo.'''
from pwn import *
import sys
context(os='linux',arch='amd64',log_level='error')
elf = ELF(sys.argv[1]) # ekhane must be binary file provide korte hobe
shellcode = elf.section('.text')
print(shellcode.hex())
print("%d bytes - Found NULL byte" % len(shellcode)) if [i for i in shellcode if i == 0] else print("%d bytes - No NULL bytes" % len(shellcode))

'''Ekhane amader binary file ke analysis korbe tarpor shellcode variable e amader assembly language er .text section tah ke hold korabe. Assembly language
jara janbe tara bujbe keno amon kora hoise!! tarpor sei .text section ke amra hex e conver korbo ja shellcode er representation

note: ekhane amader shellcode generate kora onnek tough. Akta well build assembly language thekei proper executable shellcode generate kora jay
proper assembly er nomuna. The assembly must not contain any direct varible, The assembly must not refer any memory address directly. And most important
the register should be used efficiently. Eigulo strictly follow korte hobe. noile amrader shellcode e null byte exist kora suru korbe ja amader programe
crash korabe. Akhon null byte remove er main fundamental hocche stack theke variable register e save kora use kore agey. ar proper size er register use kora
jemon 2byte er jonno BX register use kora rather than RBX. Means amader ke register ke partition akare use korte hobe. tahole amra efficient assembly
code likte parbo. ja theke shellcode easily generate kora jabe. And most important: ekhane last print funcion aitai output dibe je ekhane kono null byte
exist kore kina. Karon jodi exist kore tahole bujhe nite hobe amader shellcode thik moton kaj nao korte pare.'''