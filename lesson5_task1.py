base_file = open(r'C:\Users\Igor\PycharmProjects\untitled2\lesson5\lesson5_task1.py')
file = open('script_copy.py', 'w', encoding='utf-8')
for i in base_file:
     file.write(str(i))
file.close()