current_year = 2023

birth_year = int(input("Введите год вашего рождения: "))
age = current_year - birth_year

if age >= 18:
    print("Да, вы можете получить водительские права категории 'B'")
else:
    coming_of_age = 18 - age
    print("Вы сможете получить права через " + str(coming_of_age) + " лет")
