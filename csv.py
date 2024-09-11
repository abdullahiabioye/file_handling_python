name = input("Enter your name: ")
age = int(input("Enter your age: "))
email = input("Enter your email address: ")

line = [f"{name}\n{age}\n{email}\n"]

with open('file_handling/contacts.csv', 'w') as file:
    file.writelines(line)

# with open('file_handling/contacts.csv', 'w') as file:
#     file.write(f"{name}, {age}, {email} \n")

with open('file_handling/contacts.csv', 'r') as file:
    for line in file:
        print(line.strip())
    


        