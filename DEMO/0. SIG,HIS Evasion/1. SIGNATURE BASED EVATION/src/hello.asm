section .data

msg db "Hello World",0xa

section .text

global _start
_start:

MOV RDX,12
MOV RCX,msg
MOV RBX,2
MOV RAX,4
INT 0x80

MOV RAX,1
XOR RBX,RBX
INT 0x80
