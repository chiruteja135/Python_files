'''import random
Asciii=[]
for i in range (0,127):
    c=chr(i)
    i+=1
    Asciii.append(c)
print(random.randrange(Asciii))
'''
import random
captcha = []
for i in range(0,6):
    a = random.randint(0,127)
    b=chr(a)
    captcha.append(b)

print(captcha[0],captcha[1],captcha[2],captcha[3],captcha[4],captcha[5])
#captcha_rev=f'{captcha[0]}{captcha[1]}{captcha[2]}{captcha[3]}{captcha[4]}{captcha[5]}
