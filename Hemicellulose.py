import sys

# Данный алгоритм был написан в рамках научно-исследовательской работы для выбора оптимального вида сырья.
# В словарях собрана информация для представленных видов сырья: молекулярная масса и степень этерификации
# гемицеллюлозных структур, известных для данных видов, отсортированная по двум словарям соответственно.

molecular_mass = {'Prunus armeniaca': [1800, 7200],
                  'Cydonia oblonga': [3900, 1440, 3600],
                  'Citrullus lanatus': [1170, 12600, 1260],
                  'Pyrus communis': [17500, 20700],
                  'Beta vulgaris': [5700, 10000, 12960, 18000],
                  'Ribes rubrum': [29400],
                  'Malus domestica': [35000, 12960, 18000, 156000, 200000],
                  'Solanum melongena': [7200, 9900]}

ether = {'Prunus armeniaca': [5.32],
         'Cydonia oblonga': [33],
         'Pyrus communis': [13, 33.76],
         'Capsicum annuum': [90],
         'Beta vulgaris': [69.1, 60.8, 55],
         'Ribes rubrum': [61.53],
         'Malus domestica': [71],
         'Solanum melongena': [69],
         'Daucus carota': [71, 54, 67, 75.4, 22.17, 23.01]}

# Пользователь вводит интересующие его параметры гемицеллюлоз:
mass = int(input('Введите молекулярную массу, Да: '))
ester = float(input('Введите степень этерификации, %: '))

# Два цикла сначала отбирают значения, параметры которых меньше или больше указанных пользователем:
list_1 = []
for key, value in molecular_mass.items():
    for i in value:
        if int(i) < mass:
            list_1.append(key)

list_2 = []
for key, value in molecular_mass.items():
    for i in value:
        if int(i) > mass:
            list_2.append(key)

# Затем формируется список, который содержит только значения, одновременно оказавшиеся в числе больших и меньших:
list_3 = [i for i in list_1 if i in list_2]

# По тому же алгоритму получаем список подходящих видов по значению этерификации:
lst_1 = []
for key, value in ether.items():
    for i in value:
        if float(i) < ester:
            lst_1.append(key)

lst_2 = []
for key, value in ether.items():
    for i in value:
        if float(i) > ester:
            lst_2.append(key)

lst_3 = [i for i in lst_1 if i in lst_2]

# Затем объединяем в один список одинаковые значения из двух полученных списков:
lst_4 = [i for i in lst_3 if i in list_3]

# На выходе пользователь получает список видов, соответствующих его критериям:
print('Подходящие виды: ', list(set(lst_4)))

print('Объем в памяти словаря с молекулярной массой гемицеллюлоз:', sys.getsizeof(molecular_mass), 'байт.')
print('Объем в памяти словаря со степенью этерификации гемицеллюлоз:', sys.getsizeof(ether), 'байт.')


def Memory(dict):
    """Функция показывает объем памяти, занимаемый каждым ключом и значением словаря"""
    for key, value in dict.items():
        print(f'Ключ: {key}, объем в памяти: {sys.getsizeof(key)}')
        print(f'Значение: {value}, объем в памяти: {sys.getsizeof(value)}')


memory_1 = Memory(molecular_mass)
memory_2 = Memory(ether)

print(memory_1)
print(memory_2)