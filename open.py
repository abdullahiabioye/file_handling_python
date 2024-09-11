with open('file_handling/example.txt', 'w') as file:
    file.write("Hello World")


with open('file_handling/example.txt', 'r') as file:
    content = file.read()
    print(content)