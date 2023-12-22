# 20. Определить количество женщин, севших в порту Квинстаун,
# в возрастном интервале медиана +- 10 лет и сколько из них выжило
import csv
import statistics


def read_csv(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]
    return header, data


def count_dh(data, header):
    gender_index = header.index('Sex')
    survived_index = header.index('Survived')
    embarked_index = header.index('Embarked')
    age_index = header.index('Age')

    a = []
    a1 = []
    ages_f = []
    f1 = 0
    f2 = 0


    for row in data:
        if (row[age_index]) != '':
            if row[gender_index] == 'female': 
                if row[embarked_index] == 'Q':
                    a.append(row[age_index])
                    if row[survived_index] == '1':
                        a1.append(row[age_index])

    for i in range(len(a)):
        ages_f.append(float(a[i]))
    lower_limit = statistics.median(ages_f) - 10
    upper_limit = statistics.median(ages_f) + 10


    for i1 in range(len(a)):
        if lower_limit <= float(a[i1]) <= upper_limit:
            f1 += 1

    for i2 in range(len(a1)):
        if lower_limit <= float(a1[i2]) <= upper_limit:
            f2 += 1



    return f1, f2


file_path = 'titanic.csv'
header, data = read_csv(file_path)

f1, f2 = f1, f2 = count_dh(data, header)


print(f1, '- количество женщин, севших в порту Квинстаун, в возрастном интервале медиана +- 10 лет')
print(f2, '- количество выживших из них ')

