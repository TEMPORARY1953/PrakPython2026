while (line := input()) != "":
    x = int(line)
    if x == 13:
        print("Найдено 13!")
        break
    if x % 2 == 0:
        print(x)
else:
    print("Поздравляю, 13 не встретилось!")
