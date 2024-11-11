from book import Book
from member import Member

# book1 = Book("Kitap1", "Yazar1", False)
# book2 = Book("Kitap2", "Yazar2", True)
# book3 = Book("Kitap3", "Yazar3", True)

# print(book1.name)

# member1 = Member("Member1")
# print(member1.name)

# member1.books.append(book1)
# member1.books.append(book2)
# print(member1.read_book())

member1 = Member("Üye1")
member1.add_book("Gurur ve Önyargı","Jane Austen")
member1.add_book("İnce Memet", "Yaşar Kemal")
print(member1.books)