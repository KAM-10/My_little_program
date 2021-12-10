## Book DataBase

### 25.day tasks

1. A console app should be created as in day16-day19, but the data will be written to the database instead of being written to a file.
2. Create a virtual environment
3. Install PyMySQL pip package
4. Connect to the database.
5. The app should have some functions. (create_table, create_book, show_all, show_book)

6. When the user enters the command add table (python main.py add table), The application should create the Book_info table.
7. When the user enters the command add book (python main.py add book), The application should ask the fields.

8. When the user enters the all fields, The application should insert the book to the Book_info table.
9. When the user enters the command show all (python main.py ahow all), The application should show all books from the table.

10. When the user enters the command show book (python main.py ahow book), The application should ask the id.
11. When the user enters the id of a book, The application should show info about this book.


### Step 2

12. When the user enters the command change status (python main.py change status), The application should ask the id.
13. When the user enters the id of a book, The exist fiels should be true if it is false or should be false if it is true.

14. When the user enters the command change price (python main.py change price), The application should ask the id and new price.
15. When the user enters the id of a book and new price, the price of this book should change to given price.

16. When the user enters the command remove (python main.py remove), The application should ask the id.
17. When the user enters the id of a book, this book should be deleted from table.

18. When the user enters the command search (python main.py search), The application should ask the search word.
19. When the user enters the search word, The application should show all books which title or author contains this word.