class Book:
    def __init__(self, name, author, read):
        self.name = name
        self.author = author
        self.read = read
    def __repr__(self):
        return f"Kitap: {self.name} Yazar: {self.author}"