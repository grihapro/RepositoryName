# TODO Найдите количество книг, которое можно разместить на дискете
size = 1.44 * 1024 * 1024
pages = 100
strings = 50
symbols = 25
size_of_symbol = 4
amount = int(size//(pages*strings*symbols*size_of_symbol))
print("Количество книг, помещающихся на дискету:", amount)
