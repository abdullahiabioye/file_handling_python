with open('file_handling/new.txt', 'w') as file:
    file.write("Alhamdulillah, it is another tuesday")


with open('file_handling/new.txt', 'r') as file:
    content = file.read()
    print(content)