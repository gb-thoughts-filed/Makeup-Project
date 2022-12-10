from bs4 import BeautifulSoup

raw_list = open("2022_12_07_Sephora_JustDropped_Raw.csv","r")

soup = BeautifulSoup("")

raw_list_split = raw_list.readlines()



no_newline_characters = []
no_newline_characters_further_refined = []
product_titles = []

for i in raw_list_split:
    no_newline_characters.append(i.rstrip("\n"))





#print(raw_list_split)
#print(product_titles)

