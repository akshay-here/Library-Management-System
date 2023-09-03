import mysql.connector
mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'mysqlpassword', database = 'library3')
mycursor = mydb.cursor()


def addbook():
    book_name = input('enter the name of the book you want to add: ')
    book_code = int(input("enter a book code: "))
    total_books = int(input("enter how many of that book you want to add: "))
    subject = input("enter the subject of the book: ")
    data = (book_name, book_code, total_books, subject)
    sql = "insert into books(book_name,book_code,total_books,subject)values(%s,%s,%s,%s)"
    mycursor.execute(sql,data)
    mydb.commit()
    print("\nBook enter successfully! Thnak you!")
    print(">--------------------------<")
    main()

def displaybook():
    sql = "select distinct * from books"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for i in result:
        print('Book name: ' , i[0])
        print('Book code: ', i[1])
        print('Total books: ', i[2])
        print('Genre: ', i[3])
        print('\n>----------------------------------<')
    main()


def addstudent():
    student_name = input('enter name of student: ')
    reg_no = input("enter registration number: ")
    sql = "insert into student(student_name,reg_no)values(%s,%s)"
    data = (student_name,reg_no)
    mycursor.execute(sql,data)
    mydb.commit()
    print("New student entered successfully!")
    print('>--------------------------<')
    main()


def seestudent():
    sql = "select * from student"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for i in result:
        print('Student Name', 'Registration No', sep = '\t\t')
        print(i[0], i[1], sep = '\t\t\t')
        print('\n>-----------------------------------------------<')
    main()


def modifystudent():
    check = input("Are you sure you want to modify student name?   (y/n) :  ")
    if check == 'y' or 'Y' or 'Yes' or 'yes' or 'YES':
        student_name = input("enter current student name that has to be modified: ")
        student_name_modified = input("enter modified student name: ")
        sql = "update student set student_name = %s where student_name = %s"
        data = (student_name_modified, student_name)
        mycursor.execute(sql,data)
        mydb.commit()
        print("Modified Successfully!")
        main()
        
    elif check == 'n' or 'N' or 'no' or 'No' or 'NO':
        print("No Changes Made!")
        main()
    else:
        print("invalid input")
        modifystudent()
        

def modifybook():
    check = input("Are you sure you want to modify book name?   (y/n) :  ")
    if check == 'y' or 'Y' or 'Yes' or 'yes' or 'YES':
        book_name = input("enter current book name that has to be modified: ")
        book_name_modified = input("enter modified book name: ")
        sql = "update books set book_name = %s where book_name = %s"
        data = (book_name_modified, book_name)
        mycursor.execute(sql,data)
        mydb.commit()
        print("Modified Successfully!")
        main()
        
    elif check == 'n' or 'N' or 'no' or 'No' or 'NO':
        print("No Changes Made!")
        main()
    else:
        print("invalid input")
        modifybook()
            

def search():
    print('''
1. search for Student
2. search for Book
3. search for Genre''')
    ch = int(input("enter your choice for searching: "))
    if ch == 1 :
        search_student = input("enter search term in student's name: ") 
        sql = "select  student_name from student where student_name like '%{}%' ".format(search_student)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
           print("Student Name : ", i[0])
           print(">-------------------------<")
        main()

    elif ch == 2 :
        search_book = input("enter search term in book name : ")
        sql = "select book_name from books where book_name like '%{}%' ".format(search_book)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            
            print("Book Name :", i[0])
            print(">-----------------------<")
        main()

    elif ch == 3 :
        search_genre = input("Enter book Genre: ")
        sql = "select book_name, genre from books where genre like '%{}%'  ".format(search_genre)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print("\nBook Name: ", i[0] )
            print("Genre :", i[1])
            print(">------------------<")
        main()

    else:
        print("invalid choice")
        search()
                

#or(BUT INPUT HAS TO BE ENTERED AS SO %___%
'''
search = input("enetr search term: ")
sql = "select student_name,reg_no from student where student_name like %s "
data = (search,)
mycursor.execute(sql,data)
result = mycursor.fetchall()
for i in result:
print(i)

'''

def deletestudent():
    sure = input("Are you sure you want to delete student? Changes are permanent! (y/n): ")
    if sure == 'y' or 'Y' or 'YES' or 'Yes' or 'yes' :
        student_name = input("enter name of student that has to be deleted: ")
        data = (student_name, )
        sql = "delete from student where student_name = %s "
        mycursor.execute(sql,data)
        mydb.commit()
        print("Student successfully removed!")
        main()
    elif sure == 'n' or 'N' or 'no' or 'No' or 'NO':
        print("No Changes Made!")
        main()
    else:
        print("Invalid option")
        deletestudent()


def deletebook():
    sure = input("Are you sure you want to delete book? Changes are permanent! (y/n): ")
    if sure == 'y' or 'Y' or 'YES' or 'Yes' or 'yes' :
        book_name = input("enter name of book that has to be deleted: ")
        data = (book_name, )
        sql = "delete from books where book_name = %s "
        mycursor.execute(sql,data)
        mydb.commit()
        print("Book successfully removed!")
        main()
    elif sure == 'n' or 'N' or 'no' or 'No' or 'NO':
        print("No Changes Made!")
        main()
    else:
        print("Invalid option")
        deletebook()

def issue():
    check = input("Are you a member of the library? (y/n): ")
    if check == 'y' or'Y' or 'yes' or 'YES' or 'Yes' :
        reg_check = input("enter your 10 digit Registration ID: ")
        sql = "select * from student where reg_no = '{}' ".format(reg_check)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        if mycursor.rowcount > 0 :
            for i in result:
                if i[1] == reg_check :
                    print("Verification Complete!")
                    print("Issuing Books...")
                    reg_no = input("Enter your 10 digit registration number: ")
                    sql1 = "select book_name, book_code, total_books from books"
                    mycursor.execute(sql1)
                    result = mycursor.fetchall()
                    for i in result:
                        print("\nBook Name:", i[0])
                        print("Book Code:", i[1])
                        print("Total available Books: ", i[2])
                        print(">-------------------------<\n")
                    book_code = int(input("Please enter the Book code: "))
                    sql2 = "insert into issue(reg_no, book_code, issue_date)values(%s,%s, now())"
                    data = (reg_no, book_code)
                    mycursor.execute(sql2, data)
                    mydb.commit()
                    print("Book issued!")
                    sql3 = "update books set total_books = total_books - 1 where book_code = %s "
                    data3 = (book_code,)
                    mycursor.execute(sql3, data3)
                    mydb.commit()
                    main()
        else:
            print("Student not found. Please try again!")
            main()
    elif check == 'n' or 'N' or 'no' or 'No' or 'NO':
        print("You will have to register first!")
        main()
    else:
        print("invalid input. Try again")
        issue()


def issuetable():
    sql = "select * from issue"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for i in result:
        print("\nRegistration No: ", i[0])
        print("Book Code :", i[1])
        print("Issued Date: ", i[2])
        print("Status: ", i[3])
        print(">--------------------------------------<")
    main()

def submit():
    check = input("Have you issued a book? (y/n): ")
    if check == 'y' or'Y' or 'yes' or 'YES' or 'Yes':
        reg_check = input("Enter your Registration number: ")
        sql = "select * from issue where status = 'DUE' and reg_no = '{}' ".format(reg_check)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        if mycursor.rowcount > 0 :
            for i in result:
                if i[0] == reg_check :
                    print("Verification complete. You have issued a book")
                    print("Returning books.....")
                    reg_no = input("Enter your 10 digit registration number: ")
                    book_code = int(input("Please enter the Book code: "))
                    sql1 = "insert into submit(reg_no, book_code, return_date)values(%s,%s, now())"
                    data1 = (reg_no, book_code)
                    mycursor.execute(sql1, data1)
                    mydb.commit()
                    print("Book Returned!")
                    sql2 = "update books set total_books = total_books + 1 where book_code = %s "
                    data2 = (book_code,)
                    mycursor.execute(sql2, data2)
                    mydb.commit()
                    sql3 = "update issue set status = 'RETURNED' where reg_no = %s and book_code = %s and status = 'DUE' "
                    data3 = (str(reg_no),book_code)
                    mycursor.execute(sql3,data3)
                    mydb.commit()
                    main()
        else:
            print("Have not issued any book yet to return it. Please issue a book first")
            main()
    elif check == 'n' or 'N' or 'no' or 'No' or 'NO':
        print("You will have to issue a book before returning")
        main()
    else:
        print("Invalid input. Try again")
        submit()
        

def submittable():
    sql = "select * from submit"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for i in result:
        print("\nRegistration No: ", i[0])
        print("Book Code :", i[1])
        print("Returned Date: ", i[2])
        print(">--------------------------------------<")
    main()
        

def choices():
    choice  = input("\nEnter your option: ")
    if choice == '1':
        addbook()
    elif choice == '2':
        displaybook()
    elif choice == '3' :
        addstudent()
    elif choice == '4' :
        seestudent()
    elif choice == '5' :
        modifystudent()
    elif choice == '6':
        modifybook()
    elif choice ==  '7' :
        search()
    elif choice == '8' :
        deletestudent()
    elif choice == '9' :
        deletebook()
    elif choice == '10' :
        issue()
    elif choice == '11':
        issuetable()
    elif choice == '12':
        submit()
    elif choice == '13':
        submittable()
    elif choice == '14':
        quit()
    else:
        print("please enter valid option!")
        choices()



def main():
    print('''
                                                    LIBRARY MANAGER
    1. ADD BOOK
    2. DISPLAY BOOKS
    3. ADD A STUDENT
    4. DISPLAY STUDENTS
    5. MODIFY STUDENT NAME
    6. MODIFY BOOK NAME
    7. SEARCH 
    8. DELETE A STUDENT
    9. DELETE A BOOK
    10. ISSUE BOOK
    11. SEE ISSUE TABLE
    12. RETURN BOOK
    13. SEE RETURN TABLE
    14. QUIT
    ''')
    choices()
    


def passwd():
    entry_pwd =  input('Enter the password: ')
    if entry_pwd == '1234':
        main()
    else:
        print("wrong password! Try again")
        passwd()
passwd()
