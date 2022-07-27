import pdb
from models.book import Book
from models.author import Author


import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()


author_1 = Author("Jack", "DiStasio")
author_repository.save(author_1)

author_2 = Author ("Doro", "Schumacher")
author_repository.save(author_2)

author_repository.select_all()


book_1 = Book("Talk to your duck", 'Fantasy', 'DoroBooks', author_1, 11)
book_repository.save(book_1)


book_2 = Book("The chicke and the egg", 'Autobiography', 'DoroBooks', author_2, 30)
book_repository.save(book_2)


pdb.set_trace()
