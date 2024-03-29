import random

ca = []
for i in range(0, 6):
  a = random.randint(33, 127)
  c = chr(a)
  if c in ('"', "'", '*', ' ', '.', '/', '\\', '\'', '^', '_', '`', '|', '~'):
    pass
  else:
    ca.append(c)

print(f'{ca[0]}{ca[1]}{ca[2]}{ca[3]}{ca[4]}{ca[5]}')
print(ca)
print(len(ca))
