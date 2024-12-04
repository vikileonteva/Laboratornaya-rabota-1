# TODO Найдите количество книг, которое можно разместить на дискете
#Характеристики памяти
disk_size_mbyte = 1.44
symbol_size_byte = 4
disk_size_byte = disk_size_mbyte * 1024 * 1024
#Характеристики книги
page = 100
str_ = 50
symbols = 25

total_symbols = page * str_ * symbols
book_size = total_symbols * symbol_size_byte
numbers_of_books = int(disk_size_byte / book_size )
print("Количество книг, помещающихся на дискету:", numbers_of_books)
