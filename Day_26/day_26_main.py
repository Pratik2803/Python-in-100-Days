import pandas as pd

alpha_dataframe = pd.read_csv(filepath_or_buffer='./nato_phonetic_alphabet.csv')

alpha_dict = {row['letter']: row['code'] for (index, row) in alpha_dataframe.iterrows()}

name = input('Enter your Name : ')

name_list = [alpha.upper() for alpha in name]

result = [alpha_dict[alphabet] for alphabet in name_list]



print(result)
