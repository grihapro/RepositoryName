users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
unique = set(users)
dictionary = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
dictionary["Общее количество"] = len(users)
dictionary["Уникальные посещения"] = len(unique)
print(dictionary)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
