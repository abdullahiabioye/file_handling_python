# with open('file_handling/line.txt', 'w') as file:
#     file.write("Hello, World")

#for line by line writing
lines = ['Ameer\n', 'Suleiman\n', 'Saleem\n']

with open('file_handling/line.txt', 'w') as file:
    file.writelines(lines)