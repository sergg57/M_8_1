def add_everything_up(a,b):
    try:
        summ = a + b

    except TypeError as exc:
        #print(f'Ошибка {exc}')
        if (type(a) == int or type(a) == float) and type(b) ==str:
            a = str(a)
        elif (type(b) == int or type(b) == float) and type(a) ==str:
                b = str(b)
        #elif (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        elif (type(a)  and (type(b)) == int or (type(a) and type(b)) == float):
            a = str(a)
            b = str(b)
        summ = a + b
    return summ


if __name__ == __name__:
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456,7))

