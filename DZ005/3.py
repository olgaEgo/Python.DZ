# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def compress(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
        string = file.readline()
    i = 0
    compress = ''
    print(string)
    while i < len(string):
        count = 1
        while (i + 1 < len(string)) and (string[i] == string[i + 1]):
            count += 1
            i += 1
        compress += str(count) + string[i]
        i += 1
    print(compress)
    with open("comp_rle.txt", 'w+', encoding="utf-8") as file:
        file.writelines(compress)


# compress("decomp_rle.txt")


def decompress(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
    i = 0
    quantity = ''
    result = ''
    print(text)
    while i < len(text):
        while text[i].isdigit():
            quantity += text[i]
            i += 1
        result += text[i] * int(quantity)
        quantity = ''
        i += 1
    print(result)
    with open('decomp_rle.txt', 'w+', encoding="utf-8") as file:
        file.writelines(result)


decompress("comp_rle.txt")
