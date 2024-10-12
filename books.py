from fastapi import FastAPI, Body

app = FastAPI()

#Order of functions is important. If the function with dynamic path parameter is placed before the function with query parameter, the dynamic path parameter function will be called instead of the query parameter function.


BOOKS = [
    {
        "title":"title1",
        "author":"author1",
        "category":"category1"
    },
    {
        "title":"title2",
        "author":"author2",
        "category":"category2"
    },
    {
        "title":"title3",
        "author":"author3",
        "category":"category2"
    },

    {
        "title":"title4",
        "author":"author1",
        "category":"category1"
    }

]

#Endpoint to get all books

@app.get("/books")
 
async def read_all_books():

    return {"books": BOOKS}


#Endpoint to get a specific book by title - Use of dynamic path parameter
@app.get("/books/{book_title}")
async def read_book(book_title : str):

    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            return book
    return {"message":"Book not found"}

#Endpoint to get all books by a specific author - Use of dynamic path parameter

@app.get("/books/byauthor/{author}")
async def read_books_by_author(author: str):

    books_to_return = []

    for book in BOOKS:
        if book["author"].casefold() == author.casefold():
            books_to_return.append(book)

    return {"books_by_author": books_to_return}
        

#Endpoint to get all books by a specific category - Use of query parameter
@app.get("/books/")        
async def read_category_by_query(category: str) :
    books_to_return = []

    for book in BOOKS:
        if book["category"].casefold() == category.casefold():
            books_to_return.append(book)
    
    return {"books": books_to_return}


#Endpoint to get all books by a specific author and category - Use of dynamic path parameter (author) and query parameter (category)
@app.get("/books/{author}/")
async def read_author_category_by_query (author: str, category: str):

    books_to_return = []

    for book in BOOKS:
        if book["author"].casefold() == author.casefold() and book["category"].casefold() == category.casefold():
            books_to_return.append(book)

    return {"books": books_to_return}


#Endpoint to create a new book

@app.post("/books/create_book")

async def create_book(new_book= Body()):

    BOOKS.append(new_book)

    return {"message":"Book created successfully"}

#Endpoint to update a book by title - Use of Body parameter

@app.put("/books/update_book")

async def update_book(updated_book=Body()):

    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == updated_book["title"].casefold():
            BOOKS[i] = updated_book
            return {"message":"Book updated successfully"}
    return {"message":"Book not found"}

#Endpoint to delete a book by title - Use of dynamic path parameter

@app.delete("/books/delete_book/{book_title}")

async def delete_book(book_title: str):
    
        for i in range(len(BOOKS)):
            if BOOKS[i]["title"].casefold() == book_title.casefold():
                BOOKS.pop(i)
                return {"message":"Book deleted successfully"}
        return {"message":"Book not found"}