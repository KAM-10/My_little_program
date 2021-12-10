import sys
import datetime
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                                port=3306,
                                user='root',
                                password='321',
                                database='Books_db',
                                cursorclass=pymysql.cursors.DictCursor)

def create_table():
    with connection.cursor() as cursor:
        sql= """
        create table if not exists Book_info(
            id int(11) unsigned AUTO_INCREMENT primary key,
            book_name varchar(50) not null,
            autor_name varchar(50) not null,
            adding_date datetime,
            price DECIMAL(10,2) default 12.00,
            exist boolean default true
        )
        """
        cursor.execute(sql)
    connection.commit()


def create_book(book_name,autor_name,adding_date):
    with connection.cursor() as cursor:
        sql= """
        insert into Book_info(book_name,autor_name,adding_date) values(%s,%s,%s)
        """
        cursor.execute(sql,(book_name,autor_name,adding_date))
    connection.commit()

def show_all():
    with connection.cursor() as cursor:
        sql="""
        select*from  Book_info;
        """
        cursor.execute(sql)
        result=cursor.fetchall()
    for i in result:
        id=i['id']
        book=i['book_name']
        autor=i['autor_name']
        price=i['price']
        exist=i['exist']
        print('**********')
        print(f'Book id: {id}')
        print(f'Book name: {book}')
        print(f'Book autor: {autor}')
        print(f'Price: {price}')
        print(f'Exist: {exist}')

def show_book(id):
    with connection.cursor() as cursor:
        sql="""
        select*from  Book_info where id=%s;
        """
        cursor.execute(sql,(id))
        result=cursor.fetchall()
    for i in result:
        id=i['id']
        book=i['book_name']
        autor=i['autor_name']
        price=i['price']
        exist=i['exist']
        print('**********')
        print(f'Book id: {id}')
        print(f'Book name: {book}')
        print(f'Book autor: {autor}')
        print(f'Price: {price}')
        print(f'Exist: {exist}')


def change_status(id):
    with connection.cursor() as cursor:
        sql="""
        select Book_info.exist where id=%s
        when exist=1 then exist=0
        when exist=0 then exist=1
        update Book_info set where id=%s;
        """
        cursor.execute(sql,(id))
        connection.commit()
        result=cursor.fetchall()
    print(result)

def change_price(price,id):
    with connection.cursor() as cursor:
        sql="""
        update Book_info set price=%s where id=%s;
        """
        cursor.execute(sql,(price,id))
    connection.commit()

def remove_book(id):
    with connection.cursor() as cursor:
        sql="""
        delete from Book_info where id=%s;
        """
        cursor.execute(sql,(id))
    connection.commit()

def search_book(book_name,autor_name):
    with connection.cursor() as cursor:
        sql="""
        select * from Book_info where book_name   LIKE CONCAT('%%', %s, '%%')or autor_name LIKE CONCAT('%%', %s, '%%')
        
        """
        cursor.execute(sql,(book_name,autor_name))
    connection.commit()
    result=cursor.fetchall()
    print(result)



if sys.argv[-1] =="table" and sys.argv[-2]=="add":
    create_table()
    print("Created Table")

elif sys.argv[-1] =="book" and sys.argv[-2]=="add":
    book_name = input("Enter book name: "'\n')
    autor_name = input("Enter writer name: "'\n')
    adding_date= (datetime.datetime.now()).strftime("%Y/%m/%d")
    create_book(book_name,autor_name,adding_date)

elif sys.argv[-1] == "all":
	show_all()

elif sys.argv[-1] == "book" and sys.argv[-2]=="show":
    book_id = input("Enter book id: "'\n')
    show_book(book_id)

elif sys.argv[-1] == "status" and sys.argv[-2]=="change":
    id = input("Enter book id: "'\n')
    change_status(id)

elif sys.argv[-1] == "price" and sys.argv[-2]=="change":
    id = input("Enter book id: "'\n')
    price = input("Enter book price: "'\n')
    change_price(price,id)

elif sys.argv[-1] == "remove":
    id = input("Enter book id: "'\n')
    remove_book(id)

elif sys.argv[-1] == "search":
    word = input("Enter word: "'\n')
    word1 = input("Enter word: "'\n')
    search_book(word,word1)

#pip install -r requeriments.txt 
# commandin yazarsaq txt faylinda olan paketleri bizim ucun bir basa yukleyer.