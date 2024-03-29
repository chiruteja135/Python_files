import random
captcha = []
for i in range(0,6):
    a = random.randint(0,127)
    b=chr(a)
    captcha.append(b)
print(captcha[0],captcha[1],captcha[2],captcha[3],captcha[4],captcha[5])

