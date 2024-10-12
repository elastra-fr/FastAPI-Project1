from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {
        "title":"title1",
        "author":"author1",
        "category":"category1",
    },
    {
        "title":"title2",
        "author":"author2",
        "category":"category2",
    },
    {
        "title":"title3",
        "author":"author3",
        "category":"category2",
    },

    {
        "title":"title4",
        "author":"author1",
        "category":"category1",
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
        



