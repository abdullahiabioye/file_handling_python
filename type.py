# with open('file_handling/exam.txt', 'r') as file:
#     content = file.read()
#     print(content)

with open('file_handling/exam.txt', 'r') as file:
    for line in file:
        print(line.strip())