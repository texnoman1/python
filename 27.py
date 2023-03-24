"""Задача No27. Решение в группах
Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13"""


import re
str = """She sells sea shells on the sea shore;The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore,I'm sure that the shells are sea
shore shells."""
#print(str)

str = str.replace("\n", " ")
str = str.replace(";", " ")
str = str.replace(".", "")
str = str.replace(",", " ")
str = str.lower()
print(str)

str = str.split(" ")
print(str)

str = set(str)
print(str)
print(len(str))

#res = re.split(';" " |, |\*|\n', str)
#print(len(res))

#res = re.findall('\w+', s)

Mirsoat Tangriev: string = """She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells"""


def word_counter(string: str):
result = {i for i in string
.lower()
.replace(".", " ")
.split()}

print(result)
return f"There is - {len(result)} different words"


print(word_counter(string))
