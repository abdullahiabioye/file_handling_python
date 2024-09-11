word_counts = {}
#Reading the file
with open('file_handling/input.txt', 'r') as file:
    content = file.read()
    print(content)

#Counting the occurences of each word
words = content.lower().split()

for word in words:
    word = ''.join(char for char in word if char.isalnum())
    if word in word_counts:
        word_counts[word] += 1

    else:
        word_counts[word] = 1

#Writing the count results to a new file word_count.txt
with open('file_handling/word_count.txt', 'w') as file:
    file.write(f"Words, {word}: {word_counts} \n")

