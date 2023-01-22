python_string = 'Hello! My! name! is Python. I. will. help you. to. analyze some data'
python_string_my = python_string.replace('!', '')
python_string_my = python_string_my.replace('.', '')
print(python_string_my)
str_list = python_string_my.split()
print(str_list)