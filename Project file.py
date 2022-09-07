print('Please select language // Пожалуйста выберите язык')
l = int(input('0 to EN 1 to RU  = '))
if(l == 1):
    print('Эта программа предназначена для лёгкого счета процента от указанного числа')
    a = int(input('Введите пожалуйста число:  '))
    b = int(input('Введите пожалуйста какой процент от числа: '))
    a = int(a)
    b = int(b)
    c = a / 100 * b
    c = str(c)
    print('Процент равен ' + c)
    input('Нажмите Enter для закрытия     ')
else:
    print('This program is designed to easily count a percentage of a specified number')
    a = int(input('Enter the number:  '))
    b = int(input('Enter the percent of number:    '))
    a = int(a)
    b = int(b)
    c = a / 100 * b
    c = str(c)
    print('Percent is ' + c)
    input('Press Enter to close    ')
