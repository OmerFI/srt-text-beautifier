## SRT Text Beautifier

with open('input.txt', 'r') as f:
    data = f.read()

wordlist = []
word = ""
counter = 0
n_counter = 0
for char in data:
    if char == ".":
        word += char
        wordlist.append(word[1:] if word[0] == " " else word)
        word = ""
        counter = 0
        n_counter = 0
    elif char == " ":
        counter += 1
        if counter <= 2:
            word += char
        n_counter = 0
    elif char == "\n":
        n_counter += 1
        if n_counter < 2:
            word += " "
        counter = 0
    elif char == "(":
        if word != "":
            wordlist.append(word[1:] if word[0] == " " else word)
        word = char
        counter = 0
        n_counter = 0
    elif char == ")":
        word += char
        wordlist.append(word[1:] if word[0] == " " else word)
        word = ""    
        counter = 0
    else:
        word += char
        counter = 0
        n_counter = 0


with open('output.txt', 'w') as f:
    f.write('\n\n'.join(wordlist))