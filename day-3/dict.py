def lms():
    library={}
    while True:
        print("library options")
        print("1.count")
        print("2.add")
        print("3.remove")
        print("4.search")
        print("5.update")
        print("6.display")
        print("7.serach by book title")
        print("8.exit")
        choice=int(input("Enter the number b/w 1-8"))
        if(choice==1):
            print(len(library))
        elif choice==2:
            book_title=input("Enter the book tilte:")
            book_id=int(input("Enter the book id:"))
            library[book_id]=book_title
        elif choice==3:
            book_id=int(input("Enetr the book id of that you need to remove:"))
            library.pop(book_id)
        elif choice==5:
            book_title=input("Enter the book tilte:")
            book_id=int(input("Enter the book id:"))
            library[book_id]=book_title
        elif choice==4:
            book_id=int(input("Enter the book id:"))
            if book_id in library:
                print("we have your book")
        elif choice==6:
            print(library)
        elif choice==7:
            book_title=input("Enter the book title")
            if book_title in book_title:
                print("found")
        else:
            exit(0)
lms()