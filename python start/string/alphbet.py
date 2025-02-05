s = input()
letter_count = {}
l_input = s.lower()
for i in l_input:
    if letter.isalpha():
        if letter in l_count:
            l_count[letter] +=1
        else:
            l_count[letter]