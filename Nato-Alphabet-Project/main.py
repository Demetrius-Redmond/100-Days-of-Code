import pandas


df = pandas.read_csv("nato_phonetic_alphabet.csv")

alpha_dict = { row.letter:row.code for (index, row) in df.iterrows()}


word = input("Enter a word: ")
result = [alpha_dict[letter.upper()] for letter in word]
print(result)