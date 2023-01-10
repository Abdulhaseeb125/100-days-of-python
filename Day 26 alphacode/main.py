import pandas as pd

def alpha_geneartor():
    data = pd.read_csv("nato_phonetic_alphabet.csv")
    new_data ={row.letter:row.code for (index, row) in data.iterrows()}

    user_input = input("Enter the word:").upper()
    try:
        code_list = [new_data[letter] for letter in user_input]
    except KeyError:
        print("Please Enter valid data")
        alpha_generator()
    else:
        print(code_list)

alpha_generator()
