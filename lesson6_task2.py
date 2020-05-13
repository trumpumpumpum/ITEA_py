import random
import string

new_pass = random.choices(string.printable, k=8)
file = open(r'C:\Users\Igor\PycharmProjects\untitled2\lesson6\passwords.txt', 'a', encoding='utf-8')
for i in new_pass:
    file.write(str(i))
file.close()
