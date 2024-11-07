my_file = open("lorem.txt", "r")
print(my_file.read())
my_file.close()
print(my_file.closed)
print(my_file.read())  ##error operation on closed file.

##contex manager kullanılırsa dosya kapatmaya gerek yok

# with open("lorem.txt", "r") as my_file:
#     print(my_file.read())