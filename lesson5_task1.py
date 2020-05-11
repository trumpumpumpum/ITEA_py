base_file = open('base_script.txt')
file = open('script_copy.txt', 'w', encoding='utf-8')
for i in base_file:
     file.write(str(i))
file.close()