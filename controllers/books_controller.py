from flask import Flask, render_template, request, redirect
from repositories import book_repository, author_repository
from models.book import Book


from flask import Blueprint

books_blueprint = Blueprint('books', __name__)


#SELECT ALL BOOKS
@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template('index.html', all_books=books)

#DELETE BOOK BY ID
@books_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete(id):
    book_repository.delete(id)
    return redirect('/books')

#DELETE all BOOK 
def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)
    
    