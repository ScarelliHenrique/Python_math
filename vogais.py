user_word = input("Enter a word: ")
user_word = user_word.upper()

for ch in user_word:
    if ch == 'A' or ch == 'E' or ch=='I' or ch == 'O' or ch=='U':

        continue
    
    print(ch,end='')