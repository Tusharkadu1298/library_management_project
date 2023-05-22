print("-"*40)
print(" welcome to e-library ")
print("-"*40)
print(" enter your id and password. ")
    
books = {'math':30,'science':20,'history':35,'geography':15,'economics':10}
borrow_books ={}

while True :
    username = "tushar"
    password = "1230"
    user = input(" enter your username :-- ")
    if user == username:
        pd = input(" enter password :-- ")
        if pd == password:
            print("-"*50)
            print("login successful") 
            print("-"*50)
            break   
        else:
            print("-"*50)
            print(" invalid password ")
            print(" try again ")
            print("-"*50)
    else:
        print("-"*50)
        print("invalid username")
        print(" try again ")
        print("-"*50)

while True: 
    print("-"*50)   
    print('''
    press 1 to see total available books
    press 2 to add book
    prees 3 to add new book
    press 4 to borrow book
    press 5 to return book
    press 6 to to display borrowed books details along with name
    ''')
    print("-"*50)

    choice = int(input(" choose number from 1 to 6 :-- " ))
    if choice == 1:
        if len(books) == 0:
            print("-"*50)
            print(" no books available ")
            print("-"*50)
        else:      
            print("-"*50)
            for i,j in books.items():
                print(i , "->", j)
            print("-"*50)

    if choice == 2:
        if len(books) == 0:
            print("-"*50)
            print(" no books available ")
            print("-"*50)
        else:
            book  = input(" enter the book name :-- ").upper().lower()
            amount = int(input("enter the amount :-- "))
            books[book] = books[book] + amount
            print("-"*50)
            print(books)
            print("-"*50)

    if choice == 3:
        book = input("which book do you want to add ? -> ")
        amount = int(input("how much amount you want to add -> "))

        books[book] = amount
        print("-"*50)
        print(books)
        print("-"*50)

    if choice == 4:
        if len(books) == 0:
            print("-"*50)
            print(" no books available ")
            print("-"*50)
        else:
            name = input(" Enter name -> ")
            book = input(" Which book do you want ? -> ")

            borrow_books[name] = book
            books[book] = books[book]-1

            print("-"*50)
            print(borrow_books)
            print(books)
            print("-"*50)

    if choice == 5:
        name = input(" Enter your name -> ")
        name = input(" Enter name of book you want to return -> ")
        borrow_books[name] = book
        books[book] = books[book]+1

        print("-"*50)
        print(borrow_books)
        print(books)
        print("-"*50)
    
    if choice == 6:
        for i,j in borrow_books.items():
            print(i , "-->", j)

        repeat  = input(" Do you want to repeat again ? (yes/no) --> ")
        if repeat == "no":
            break    
        
