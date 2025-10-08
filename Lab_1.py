RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLUE = '\u001b[44m'
END = '\u001b[0m'
GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'

#Япония

k =2
def Japan():
    for i in range(-2, 15+1+2): 
        if i==1 or i==14: 
            print(f'{WHITE}{"  " * (15+k)}{RED}{"  " * (5)}{WHITE}{"  " * (15+k)}{END}')
        elif i==2 or i== 13:
            print(f'{WHITE}{"  " * (13+k)}{RED}{"  " * (9)}{WHITE}{"  " * (13+k)}{END}')
        elif i==3 or i==12:
            print(f'{WHITE}{"  " * (12+k)}{RED}{"  " * (11)}{WHITE}{"  " * (12+k)}{END}')
        elif 10<=i<=11 or 4<=i<=5:
            print(f'{WHITE}{"  " * (11+k)}{RED}{"  " * (13)}{WHITE}{"  " * (11+k)}{END}')
        elif 6<=i<=9:
            print(f'{WHITE}{"  " * (10+k)}{RED}{"  " * (15)}{WHITE}{"  " * (10+k)}{END}')
        else:
            print(f'{WHITE}{"  " * (35+2*k)}{END}')

#Узор

repeat = 5 #зададим количество повторений узора
n=5
def romb(repeat):
    height = 2 * n - 1
    num = 0 
    for i in range(height):
        line = ''
        num+=1
        # Повторяем узор repeats раз
        for rep in range(repeat):
            # Определяем позицию в текущем ромбе
            if i < n:
                # Верхняя часть ромба
                if i == 0:
                    # Верхняя вершина
                    stroka = f'{WHITE}{"  " * (n-1)}{BLUE}{"  "}{WHITE}{"  " * (n-2)}{END}'
                elif i == n-1:
                    # Средняя линия (самая широкая)
                    stroka = f'{BLUE}{"  "}{WHITE}{"  " * (height-2)}'
                else:
                    # Промежуточные линии верхней части
                    spaces_before = n - 1 - i
                    spaces_between = 2 * i - 1
                    spaces_after = (n +1 - spaces_between)-spaces_before
                    stroka = f'{WHITE}{"  " * spaces_before}{BLUE}{"  "}{WHITE}{"  " * spaces_between}{BLUE}{"  "}{WHITE}{"  " * spaces_after}{END}'
            else:
                # Нижняя часть ромба (симметрична верхней)
                j = height - 1 - i
                if j == 0:
                    # Нижняя вершина
                    stroka = f'{WHITE}{"  " * (n-1)}{BLUE}{"  "}{WHITE}{"  " * (n-2)}{END}'
                else:
                    # Промежуточные линии нижней части
                    spaces_before = n - 1 - j
                    spaces_between = 2 * j - 1
                    spaces_after = (n +1 - spaces_between)-spaces_before
                    stroka = f'{WHITE}{"  " * spaces_before}{BLUE}{"  "}{WHITE}{"  " * spaces_between}{BLUE}{"  "}{WHITE}{"  " * spaces_after}{END}'
            line += stroka 
        if num == n : 
            line += f'{BLUE}{"  "}{END}'
        else:
            line += f'{WHITE}{"  "}{END}'
        print(line)

#График

def graph(): 
    plot_list = [[0 for i in range(11)] for i in range(10)]  # Увеличиваем до 11 столбцов
    result = [0 for i in range(10)]

    for i in range(10):
        result[i] = 3 * i

    step = round(abs(result[0] - result[9]) / 9, 2)
    print(f'Step is {step}')

    for i in range(10):
        plot_list[i][0] = step * (9 - i)

    for i in range(10):
        for j in range(10):
            if abs(plot_list[i][0] - result[j]) < step / 2:
                if j + 1 < 11: 
                    plot_list[i][j + 1] = 1

    for i in range(10):
        line = ''
        for j in range(11):
            if j == 0:
                line += '\t' + str(int(plot_list[i][j])) + '\t'
            else:
                if plot_list[i][j] == 0:
                    line += '--'
                elif plot_list[i][j] == 1:
                    line += '!!'
        print(line)
    x_gr = '\t0\t'
    for i in range(0, 10):
        x_gr += str(i) + ' '
    print(x_gr)

#Диаграммма

def diag():
    file = open('sequence.txt', 'r')
    more = 0
    less = 0
    for el in file:
        el = float(el)
        if el<0:
            if abs(el)<5:
                more+=1
            elif abs(el)!=5:
                less+=1
    per_m= int(more*100/(more+less))
    per_l=100-per_m

    for i in range(2): 
        if i == 0: 
            print('Больше -5:', f'{GREEN}{' '*per_m}{END}', str(per_m)+'%')
        else: 
            print('Меньше -5:', f'{YELLOW}{' '*per_l}{END}', str(per_l)+'%')

Japan()
print()
romb(5)
print()
graph()
print()
diag()