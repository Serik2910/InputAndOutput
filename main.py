# content = open(r"C:\Users\kobla\Documents\new 3.txt", "r")
#
# for line in content:
#     print(line, end='')
# content.close()

# with open(r"C:\Users\kobla\Documents\new 3.txt", "r") as content:
#     for line in content:
#         print(line, end='')

# with open(r"C:\Users\kobla\Documents\new 3.txt", "r") as content:
#     line = content.readline()
#     while line:
#         print(line, end='')
#         line = content.readline()

# with open(r"C:\Users\kobla\Documents\new 3.txt", "r") as content:
#     lines = content.readlines()
# for line in lines:
#     print(line, end='')

# with open(r"C:\Users\kobla\Documents\new 3.txt", "r") as content:
#     text = content.read()
# print(text, end='')

# имя файла
# FILENAME = "messages.txt"
#
# messages = list()
#
# for i in range(4):
#     message = input("Введите строку " + str(i + 1) + ": ")
#     messages.append(message + "\n")
#
# # запись списка в файл
# with open(FILENAME, "a", encoding="utf8") as file:
#     for message in messages:
#         file.write(message)

# считываем сообщения из файла
# print("Считанные сообщения")
# with open(FILENAME, "r") as file:
#     for message in file:
#         print(message, end="")
# data = list()
# with open(FILENAME, "r", encoding="utf8") as file:
#     for message in file:
#         # print(message, end="")
#         data.append(message)
# print(data)

p = iter('ret')

print(p.__sizeof__())


def count_up_to(x):
    count = 1
    while count <= x:
        yield count
        count += 1