with open('file_handling/students.txt', 'r') as file:
    for line in file:
        print("Good Morning", line.strip())
        