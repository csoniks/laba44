def z1():
    '''try: #исключение для не числа, чтобы отрабатывал
        a = int(input("введите число, чтобы проверить делимость на 3"))
    except ValueError:
        print("Ввели не число")
    else: '''
    a = int(input("введите число, чтобы проверить делимость на 3"))
    if a != 0 and a % 3 == 0:
        print("число делится на 3")
    elif a == 0:
        print("Ввели 0")
    else:
        print("число не делится на 3")


def z2():
    try:
        a = int(input("введите число, чтобы проверить делимость на 100: "))
        ostat = 100 // a
    except ValueError:
        print("ввели не число")

    except ZeroDivisionError:
        print("введен 0")
    else:
        if a % 100 == 0 and a != 0:
            print("число делится на 100")
        else:
            print("число не делится на 100")


def z3():
    def mag():
        data = input("введите дату: ")
        data = data.split(".")
        #print(data)
        if int(data[0]) * int(data[1]) == int(data[2][2:4]):
            return True
        else:
            return False

    print(mag())


def z4():
    bilet = input("введите номер билета: ")
    lpolovina = 0
    prpolovina = 0
    if len(bilet) % 2 == 0:
        for i in bilet[:int(len(bilet) / 2)]:
            lpolovina += int(i)
        for i in bilet[int(len(bilet) / 2):int(len(bilet)) + 1]:
            prpolovina += int(i)
        if lpolovina == prpolovina:
            print("это счастливый билет")
            print(lpolovina)
            print(prpolovina)

        else:
            print("это несчастливый билет")
            print(lpolovina)
            print(prpolovina)

    else:
        print("количество цифр нечетно")


z1()
z2()
z3()
z4()
