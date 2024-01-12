import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import datetime
from datetime import date
from datetime import timedelta
print("            |************************|")
print("=:-------:{=|WELCOME TO ABYSS LIBRARY|=}:--------:=")
print("            |************************|")
m=1
#LOGIN
while(m==1):
    print("               |::::::::::::::::|")
    print("               |:   1.ADMIN    :|")
    print("               |:   2.USER     :|")
    print("               |::::::::::::::::|")
    a=int(input("               Enter your choice:"))
#Admin_LOGIN
    if(a==1):
        print("______________________________")
        ad=input("Enter the ADMIN name:")
        pwd=input("Enter the Passward:")
        df=pd.read_csv("admin_list.csv")
        df1=df[(df['Admin']==ad) & (df['Password']==pwd)]
        if(df1.empty):
            print("=X=TRY AGAIN=X=")
            m=1
        else:
            q=1
            print("------||WELCOME ",ad,"||------")
#Admin_OPTIONS
            while (q==1):
                print("______________________________")
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ")
                print("1.Book Issue Management")
                print("2.Admins Management")
                print("3.Users Management")
                print("4.Books Management")
                print("5.===BACK===")
                b=int(input("Enter your choice: "))
                if(b==1):
                    w=1
#BOOK_ISSUE_MANGMENT(IMang)
                    while(w==1):
                        print("______________________________")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("1. Book Issued list")
                        print("2. Issue Book")
                        print("3. Availablity of Book")
                        print("4. Issued Name Check")
                        print("5. Remove Entry")
                        print("6. ==BACK==")
                        c=int(input("Enter your choice: "))
#IMang_ISSUE LIST
                        if(c==1):
                            df2=pd.read_csv('Issued.csv')
                            df3=df2.sort_values("User")
                            print("______________________________")
                            print(df3)
                            q=0
                            w=1
#IMang_ISSUE BOOK                            
                        elif(c==2):
                            print("______________________________")
                            i=int(input("Enter the no. of entries:"))
                            for s in range(i):
                                print("______________________________")
                                print("Entry",s+1)
                                na=input("Enter User Name:")
                                bd=input("Enter BookID(One Book at a time):")
                                df2=pd.read_csv('Issued.csv')
                                df3=df2[df2["BookID"]== bd]
                                if df3.empty:
                                    di=input("Enter Issue date(MM/DD/YYYY):")
                                    date_1 = datetime.datetime.strptime(di, "%m/%d/%Y")
                                    r = date_1 + datetime.timedelta(days=10)
                                    df2=pd.read_csv('Issued.csv')
                                    data={"User":[na],"BookID":[bd],"D_o_Issue":[di], "D_o_Return":[r]}
                                    df3=pd.DataFrame(data)
                                    df4=df2.append(df3)
                                    df4.to_csv('Issued.csv',index=False)
                                    df4=pd.read_csv('Issued.csv')
                                    print("---SUCCESSFULLY ISSUED---")
                                    print("   ^^^^^^^^^^^^^^^^^^^")
                                    print(df4)
                                    q=0
                                    w=1
                                else:
                                    print("--This Book is NOT available--")
                                    print("It will be available after:", (df3['D_o_Return'].to_string(index=False)))
                                    q=0
                                    w=1
#IMang_AVAILABILITY OF BOOK
                        elif(c==3):
                            print(" ")
                            id=input("Enter the BookID(Example- BK1,BK2..): ")
                            df2=pd.read_csv('Issued.csv')
                            df3=df2[df2['BookID']==id]
                            if(df3.empty):
                                print("---THIS BOOK IS AVAILABLE---")
                                print("   ^^^^^^^^^^^^^^^^^^^^^^")
                                q=0
                                w=1
                            else:
                                print(" ")
                                print("--SORRY THIS BOOK IS Currently ISSUED--")
                                print("  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                print("It will be available after:", (df3['D_o_Return'].to_string(index=False)))
                                q=0
                                w=1
#IMang_Issued Name Check                                
                        elif(c==4):
                            print(" ")
                            nam=input("Enter User Name: ")
                            df2=pd.read_csv('Issued.csv')
                            df3=df2[df2['User']==nam]
                            if(df3.empty):
                                print("-- No Book Issued under", nam, " --")
                                q=0
                                w=1
                            else:
                                print("Issue Date:", df3["D_o_Issue"].to_string(index=False))
                                print("Returning Date: ", df3["D_o_Return"].to_string(index=False))
                                re=input("Enter Returned date(mm/dd/yyYy):")
                                dd=input("No.Of Delay Days: ")
                                fe= dd*10
                                df4=df3["Returned on"].fillna(re)
                                df5=df4['Delay Days'].fillna(dd)
                                df6=df5['Fee'].fillna(fe)
                                print("Fee: Rs.10/day")
                                print("Here is your Recipt Mr./Ms.",nam)
                                print(df6)
                                print("Your pay=",(df6['Fee'].to_string(index=False)), "Rupees")
                                print("==Thanks for visiting==")
                                data2=(df2[df2['User']==nam].index.values)
                                df2=df2.drop(data2)
                                df2.to_csv('Issued.csv',index=False)
                                df2=pd.read_csv('Issued.csv')
                                q=0
                                w=1
#IMang_delete entry                                
                        elif(c==5):
                            print(" ")
                            add=input("Enter User Name you want to Delete: ")
                            df2=pd.read_csv('Issued.csv')
                            df3=df2[df2['User']==add]
                            if(df3.empty):
                                q=0
                                w=1
                                print("---This User Not Found---")
                            else:
                                data=(df2[df2['User']==add].index.values)
                                df2=df2.drop(data)
                                df2.to_csv('Issued.csv',index=False)
                                df2=pd.read_csv('Issued.csv')
                                q=0
                                w=1
                                print("=Succefully Deleted Entry=")
                                print(df2)
#IMang_BACK
                        elif(c==6):
                            w=0
                            q=1
#ADMIN_MANAGEMENT                            
                elif(b==2):
                    x=1
                    while x==1:
                        print("______________________________")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("1. Admin Account List")
                        print("2. Add new Admin")
                        print("3. Update Admin Details")
                        print("4. My Shift Schedule")
                        print("5. Remove Entry")
                        print("6. ==BACK==")
                        c=int(input("Enter your choice: "))
#ADMIN_LIST
                        if(c==1):
                            print(" ")
                            df2=df.sort_values("Admin")
                            print(df2)
                            q=0
                            x=1
#ADMIN_ADD
                        elif(c==2):
                            print(" ")
                            i=int(input("Enter the no. of Entries"))
                            print("Enter the following details")
                            for s in range (i):
                                print(" ")
                                print("Entry",(s+1))
                                adn=input("Admin Name: ")
                                Pass=input("Create Password: ")
                                pn=input("Phoneno.: ")
                                ci=input("City: ")
                                ag=input("Age: ")
                                sh=input("shift: ")
                                sal=input("Salary: ")
                                df=pd.read_csv('admin_list.csv')                            
                                data={"Admin":[adn],"Password":[Pass], "Phone no.":[pn],"City":[ci],"Age":[ag],"Shift":[sh],"Salary":[sal]}
                                df2=pd.DataFrame(data)
                                df4=df.append(df2)
                                df4.to_csv('admin_list.csv',index=False)
                                df4=pd.read_csv('admin_list.csv')
                            print(" ")    
                            print(df4)
                            print("-- SUCCESSFULLY ADDED--")
                            print("   ^^^^^^^^^^^^^^^^^^")
                            q=0
                            x=1
#ADMIN_UPDATE                           
                        elif(c==3):
                            adn=input("Admin name whose detail you want to change")
                            df2=pd.read_csv('Admin_list.csv')
                            df3=df2[df2['Admin']==adn]
                            if(df3.empty):
                                q=0
                                x=1
                                print("--Admin not exists--")
                            else:
                                l=1
                                while l==1:
                                    print("--WHAT YOU WANT TO CHANGE--")
                                    print("1. Passward")
                                    print("2. Age")
                                    print("3. City")
                                    print("4. Phone No.")
                                    print("5. Shift")
                                    print("6. Salary")
                                    print("7. ==BACK==")
                                    h=int(input("Enter your choice:"))
                #PASSWORD
                                    if h==1:
                                        df2=pd.read_csv('Admin_list.csv')
                                        pas=input("Enter New Password: ")
                                        d=(df2[df2['Admin']==adn].index.values)
                                        df2.loc[d,["Password"]]=pas
                                        df2.to_csv('Admin_list.csv',index=False)
                                        df3=df2[df2['Admin']==adn]
                                        print(df3)
                                        print("==Successfully changed==")
                                        l=1
                                        q=0
                                        x=0
                #AGE
                                    elif h==2:
                                        df2=pd.read_csv('Admin_list.csv')
                                        pas=input("Enter New Age: ")
                                        d=(df2[df2['Admin']==adn].index.values)
                                        df2.loc[d,["Age"]]=pas
                                        df2.to_csv('Admin_list.csv',index=False)
                                        df3=df2[df2['Admin']==adn]
                                        print(df3)
                                        print("==Successfully changed==")
                                        l=1
                                        q=0
                                        x=0
                #CITY
                                    elif h==3:
                                        df2=pd.read_csv('Admin_list.csv')
                                        pas=input("Enter New City: ")
                                        d=(df2[df2['Admin']==adn].index.values)
                                        df2.loc[d,["City"]]=pas
                                        df2.to_csv('Admin_list.csv',index=False)
                                        df3=df2[df2['Admin']==adn]
                                        print(df3)
                                        print("==Successfully changed==")
                                        l=1
                                        q=0
                                        x=0
                #PHONE_NO.
                                    elif h==4:
                                        df2=pd.read_csv('Admin_list.csv')
                                        pas=input("Enter New Phone no.: ")
                                        d=(df2[df2['Admin']==adn].index.values)
                                        df2.loc[d,["Phone no."]]=pas
                                        df2.to_csv('Admin_list.csv',index=False)
                                        df3=df2[df2['Admin']==adn]
                                        print(df3)
                                        print("==Successfully changed==")
                                        l=1
                                        q=0
                                        x=0
                #SHIFT
                                    elif h==5:
                                        df2=pd.read_csv('Admin_list.csv')
                                        pas=input("Enter New Shift: ")
                                        d=(df2[df2['Admin']==adn].index.values)
                                        df2.loc[d,["Shift"]]=pas
                                        df2.to_csv('Admin_list.csv',index=False)
                                        df3=df2[df2['Admin']==adn]
                                        print(df3)
                                        print("==Successfully changed==")
                                        l=1
                                        q=0
                                        x=0
                #SALARY
                                    elif h==6:
                                        df2=pd.read_csv('Admin_list.csv')
                                        pas=input("Enter New Salary: ")
                                        d=(df2[df2['Admin']==adn].index.values)
                                        df2.loc[d,["Salary"]]=pas
                                        df2.to_csv('Admin_list.csv',index=False)
                                        df3=df2[df2['Admin']==adn]
                                        print(df3)
                                        print("==Successfully changed==")
                                        l=1
                                        q=0
                                        x=0
#BACK TO ADMIN PHASE OPTIONS
                                    elif h==7:
                                        l=0
                                        q=0
                                        x=1
                                    else:
                                        print("--Enter the correct choise--")
                                        l=1
                                        q=0
                                        x=0
#ADMIN_Shift                                        
                        elif (c==4):
                            print(" ")
                            print(ad, ",your shift will be from: ",(df1["Shift"].to_string(index=False)))
                            q=0
                            x=1
#ADMIN_Delete 
                        elif (c==5):
                             if (ad== "Jhanvi"):
                                print(" ")
                                add=input("Enter Admin you want to Delete: ")
                                df2=pd.read_csv('admin_list.csv')
                                df3=df2[df2['Admin']==add]
                                if(df3.empty):
                                     q=0
                                     x=1
                                     print("---This Admin already not exists---")
                                else:
                                    data=(df2[df2['Admin']==add].index.values)
                                    df2=df2.drop(data)
                                    df2.to_csv('admin_list.csv',index=False)
                                    df2=pd.read_csv('admin_list.csv')
                                    q=0
                                    x=1
                                    print("-- ", add, " record is successfully deleted. --")
                             else:
                                 print("--Sorry you are not allowed to remove staff details--")
                                 print("--ONLY HEAD ADMIN 'Jhanvi' is allowed--")
                                 q=0
                                 x=1
#Admin_BACK
                        elif (c==6):
                            x=0
                            q=1
#USER_MANAGEMENT
                elif(b==3):
                    y=1
                    while y==1:
                        print("______________________________")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("1. User Account List")
                        print("2. Add new User")
                        print("3. Remove Entry")
                        print("4. ==BACK==")
                        c=int(input("Enter your choice:"))
#USER_MANAGEMENT_list
                        if(c==1):
                            df2=pd.read_csv('User_list.csv')
                            print(df2)
                            q=0
                            y=1
#USER_MANAGEMENT_Add new                           
                        elif(c==2):
                            i=int(input("Enter the no. of Entries:"))
                            print("Enter the following")
                            for s in range (i):
                                print("Entry",(s+1))
                                u=input("User Name")
                                Pass=input("Create Password")
                                pn=input("Phoneno.: ")
                                ci=input("City: ")
                                ag=input("Age:")
                                df=pd.read_csv('User_list.csv')                            
                                data={"User":[u],"Password":[Pass], "Phone no.":[pn],"City":[ci],"Age":[ag]}
                                df2=pd.DataFrame(data)
                                df4=df.append(df2)
                                df4.to_csv('User_list.csv',index=False)
                                df4=pd.read_csv('User_list.csv')
                                print(df4)
                                print("--SUCCESSFULLY ADDED--")
                                q=0
                                y=1
#USER_MANAGEMENT_Delete entry
                        elif (c==3):
                            add=input("Enter User Name you want to Delete: ")
                            df2=pd.read_csv('User_list.csv')
                            df3=df2[df2['User']==add]
                            if(df3.empty):
                                 q=0
                                 y=1
                                 print("User already not exists")
                            else:
                                data=(df2[df2['User']==add].index.values)
                                df2=df2.drop(data)
                                df2.to_csv('User_list.csv',index=False)
                                df2=pd.read_csv('User_list.csv')
                                q=0
                                y=1
                                print("=X= ", add, " record is successfully deleted. =X=")
#USER_MANGEMENT_BACK                                
                        elif (c==4):
                            y=0
                            q=1
#BOOK MANAGEMENT
                elif(b==4):
                    k=1
                    while k==1:
                        print("______________________________")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("1. Books List")
                        print("2. Add new Book")
                        print("3. Reading Rate(Histogram)")
                        print("4. Remove Entry")
                        print("5. ==BACK==")
                        c=int(input("Enter your choice:"))
#BK MANAG._LIST
                        if(c==1):
                            print(" ")
                            df2=pd.read_csv("Book.csv")
                            print(df2)
                            q=0
                            k=1
#BK MANAG._ADD                            
                        elif(c==2):
                            print(" ")
                            i=int(input("Enter the no. of Entries"))
                            print("Enter the following details")
                            for s in range (i):
                                print(" ")
                                print("Entry",(s+1))
                                bi=input("Book ID:")
                                bn=input("Book Name:")
                                au=input("Auther")
                                pu=input("Publisher: ")
                                g=input("Genre: ")
                                ra=input("Rating: ")
                                r=input("No. of reads") 
                                df=pd.read_csv('Book.csv')                            
                                data={"BookID":[bi],"Book Name":[bn], "Author":[au],"Publisher":[pu],"Genre":[g],"Rating":[ra], "No. Of Reads": [r]}
                                df2=pd.DataFrame(data)
                                df4=df.append(df2)
                                df4.to_csv('Book.csv',index=False)
                                df4=pd.read_csv('Book.csv')
                                print(df4)
                                print("--SUCCESSFULLY ADDED--")
                                q=0
                                k=1
#BK MANAG._READING RATE(GR)
                        elif (c==3):
                            gr=pd.read_csv('Book.csv')
                            plt.hist(gr['No. Of Reads'])
                            plt.title("=| No. of Books as per reads |=",fontsize=15)
                            plt.xlabel("No.of Reads",fontsize=10)
                            plt.ylabel("No. of Books",fontsize=10)
                            plt.show()
                            q=0
                            k=1
#BK MANA._REMOVE
                        elif (c==4):
                            print(" ")
                            add=input("Enter Book Name you want to Delete: ")
                            df2=pd.read_csv('Book.csv')
                            df3=df2[df2['Book Name']==add]
                            if(df3.empty):
                                 q=0
                                 k=1
                                 print("Book already not exists")
                            else:
                                data=(df2[df2['Book Name']==add].index.values)
                                df2=df2.drop(data)
                                df2.to_csv('Book.csv',index=False)
                                df2=pd.read_csv('Book.csv')
                                q=0
                                k=1
                                print("--SUCCESSFULLY DELETED--")
#BK MANAG._BACK
                        elif (c==5):
                            k=0
                            q=1
#ADMIN_BACK
                elif (b==5):
                    q=0
#USER PHASE
    if(a==2):
        q=1
        while (q==1):
            print(" ")
            print("             |-*-*-*-*-*-*-*-*-*-*-|")
            print("             |*  1. LOGIN         *|")
            print("             |*  2. REGISTRATION  *|")
            print("             |*  3. ==BACK==      *|")
            print("             |-*-*-*-*-*-*-*-*-*-*-|")
            df=pd.read_csv("User_list.csv")
            f=int(input("             Enter the choise:"))
#USER_LOGIN(Direct)
            if(f==1):
                print("_______________________")
                u=input("Enter the User name:")
                pwd=input("Enter the Passward:")
                df1=df[(df['User']==u) & (df['Password']==pwd)]
                if(df1.empty):
                    print(":=X= Try Again =X=:")
                    print("Please Enter Correct Details")
                    q=1
                else:           
                    s=1
                    print(":-:-|*|HELLO ",u,"|*|-:-:")
#USER_Login options
                    while s==1:
                        print("|---------------------------|")
                        print("|!  1. My Account          !|")
                        print("|!  2. Reading Suggestions !|")
                        print("|!  3. Search Books        !|")
                        print("|!  4. Issue Book          !|")
                        print("|!  5. Update MY details   !|")
                        print("|!  6. ==BACK==            !|")
                        print("|---------------------------|")
                        b=int(input("Enter your choice: "))
#User_MY ACC.
                        if (b==1):
                            print(" ")
                            print("ooo:| WELCOME TO YOUR ACCOUNT ",u,"|:ooo")
                            print("            My DETAILS")
                            print("            ^^^^^^^^^^")
                            print("Name          : ", df1['User'].to_string(index=False))
                            print("Age           : ",df1['Age'].to_string(index=False))
                            print("PhoneNo.      : ",df1['Phone no.'].to_string(index=False))
                            print("City          : ",df1['City'].to_string(index=False))
                            print("Issued History: ",df1['Issued History'].to_string(index=False))
                            print("")
                            s=1
                            q=0
#USER_READING SUGG.
                        elif (b==2):
                            t=1
                            while (t==1):
                                print("__________________________")
                                print("|************************|")
                                print("| ---SUGGESTION BOARD--- |")
                                print("|   1. Top Rating        |")
                                print("|   2. Toppers of Genres |")
                                print("|   3. ===BACK===        |")
                                print("|************************|")
                                p=int(input("Enter your choise: "))
                    #TOP RATED
                                if p==1:
                                    gr=pd.read_csv("Book.csv")
                                    gr1=gr.sort_values('Rating', ascending=False)
                                    plt.bar(gr1['BookID'],gr1['Rating'])
                                    plt.title("Top Rated Books",fontsize=20)
                                    plt.xlabel('Book Name',fontsize=10)
                                    plt.ylabel('Rating',fontsize=10)
                                    plt.grid()
                                    plt.show()
                                    t=1
                                    q=0
                                    s=0
                    #TOP OF GENRES
                                elif p==2:
                                    gr=pd.read_csv("Book.csv")
                                    gr=pd.read_csv("Book.csv")
                                    df2=gr[gr['Genre']== "Novel"]
                                    df3=gr[gr['Genre']== "Fiction"]
                                    df4=gr[gr['Genre']== "Suspence"]
                                    df5=gr[gr['Genre']== "Romance"]
                                    df6=gr[gr['Genre']== "Horror"]
                                    df7=gr[gr['Genre']== "Teen-Fiction"]
                                    plt.plot(df2.BookID, df2['Rating'], 'yellow', label='NOVEL')
                                    plt.plot(df3.BookID, df3['Rating'], 'red', label='FICTION')
                                    plt.plot(df4.BookID, df4['Rating'], 'blue', label='SUSPENCE')
                                    plt.plot(df5.BookID, df5['Rating'], 'pink', label='ROMANCE')
                                    plt.plot(df6.BookID, df6['Rating'], 'black', label='HORROR')
                                    plt.plot(df7.BookID, df7['Rating'], 'green', label='TEEN-FICTION')
                                    plt.legend(loc='upper left')
                                    plt.title("=|Top Rated Books(Genre Wise)|= \n -Zoom the gener section you are interested-",fontsize=20)
                                    plt.xlabel('Book Name',fontsize=10)
                                    plt.ylabel('Ratings',fontsize=10)
                                    plt.grid()
                                    plt.show()
                                    t=1
                                    q=0
                                    s=0
                    #BACK
                                elif p==3:
                                    t=0
                                    q=0
                                    s=1
                                else:
                                    print("x-x-x-x-Enter the correct choise-x-x-x-x")
                                    t=1
                                    q=0
                                    s=0
#USER_BK BROWSER
                        elif (b==3):
                            v=1
         #BROWSING METHODS
                            while v==1:
                                print("|-----------------------|")
                                print("|   = SEARCH METHODS =  |")
                                print("|   1. By BOOK ID       |")
                                print("|   2. By BOOK NAME     |")
                                print("|   3. My Genre Books   |")
                                print("|   4. ==BACK==         |")
                                print("|-----------------------|")
                                sm=int(input("Enter your Choise: "))
             #BY BK ID
                                if sm==1:
                                    i=input("Enter the Book ID")
                                    df2=pd.read_csv('Book.csv')
                                    df3=pd.read_csv('Issued.csv')
                                    df4=df2[df2['BookID']== i]
                                    print(df4)
                                    df5=df3[df3['BookID']==i]
                                    if df5.empty:
                                        print("--This Book Is Available in Our Library--")
                                        print("--Get the Book ID and Please go back If you want to Issue This Book--")
                                        v=1
                                        q=0
                                        s=0
                                    else:
                                        print("--THIS BOOK IS Currently ISSUED--")
                                        print("It will be available after:", (df5['D_o_Return'].to_string(index=False)))
                                        v=1
                                        q=0
                                        s=0
             #BY BK NAME
                                elif sm==2:
                                    am=input("Enter the Book Name")
                                    df2=pd.read_csv('Book.csv')
                                    df3=pd.read_csv('Issued.csv')
                                    df4=df2[df2['Book Name']== am]
                                    print(df4)
                                    df5=df3[df3['BookID']==i]
                                    if df5.empty:
                                        print("--This Book Is Available in Our Library--")
                                        print("--Get the Book ID and Please go back If you want to Issue This Book--")
                                        v=1
                                        q=0
                                        s=0
                                    else:
                                        print("--THIS BOOK IS Currently ISSUED--")
                                        print("It will be available after:", (df5['D_o_Return'].to_string(index=False)))
                                        v=1
                                        q=0
                                        s=0
            #GENER-WISE
                                elif sm==3:
                                    print("|-----------------------| ")
                                    print("|    AVAILABLE GENRES   |")
                                    print("|      1. Fiction       |")
                                    print("|      2. Novel         |")
                                    print("|      3. Suspence      |")
                                    print("|      4. Romance       |")
                                    print("|      5. Horror        |")
                                    print("|      6. Teen-Fiction  |")
                                    print("|      7. ==Back==      |")
                                    print("|-----------------------|")
                                    g=int(input("Enter your choise: "))
                                    mg=pd.read_csv('Book.csv')
                    #FICTION
                                    if g==1:
                                        ng=mg[mg['Genre']== "Fiction"]
                                        print(ng)
                                        v=1
                                        q=0
                                        s=0
                    #NOVEL
                                    elif g==2:
                                        ng=mg[mg['Genre']== "Novel"]
                                        print(ng)
                                        v=1
                                        q=0
                                        s=0
                    #SUSPENCE
                                    elif g==3:
                                        ng=mg[mg['Genre']== "Suspence"]
                                        print(ng)
                                        v=1
                                        q=0
                                        s=0
                    #ROMANCE
                                    elif g==4:
                                        ng=mg[mg['Genre']== "Romance"]
                                        print(ng)
                                        v=1
                                        q=0
                                        s=0
                    #HORROR
                                    elif g==5:
                                        ng=mg[mg['Genre']== "Horror"]
                                        print(ng)
                                        v=1
                                        q=0
                                        s=0
                    #TEEN-FICTION
                                    elif g==6:
                                        ng=mg[mg['Genre']== "Teen-Fiction"]
                                        print(ng)
                                        v=1
                                        q=0
                                        s=0
                    #BACK TO BROWSING OPTIONS
                                    else:
                                        v=1
                                        q=0
                                        s=0
            #BACK TO USER OPTIONS
                                elif sm==4:
                                    v=0
                                    q=0
                                    s=1
                                else:
                                    print("--Enter correct choise--")
                                    v=1
                                    q=0
                                    s=0
#USER_ISSUE BOOK
                        elif (b==4):
                            print(":-:-:-:-:-:-:-:-:-:-:-:")
                            df2=pd.read_csv('Book.csv')
                            df3=pd.read_csv('Issued.csv')
                            na=input("Enter Your Name:")
                            i=input("Enter the BookID")
                            df5=df3[df3['BookID']==i]
                            if df5.empty:
                                print("--This Book Is Available in Our Library--")
                                di=input("Enter Issue date(MM/DD/YYYY):")
                                date_1 = datetime.datetime.strptime(di, "%m/%d/%Y")
                                r = date_1 + datetime.timedelta(days=10)
                                df3=pd.read_csv('Issued.csv')
                                data={"User":[na],"BookID":[i],"D_o_Issue":[di], "D_o_Return":[r]}
                                df4=pd.DataFrame(data)
                                df5=df3.append(df4)
                                df5.to_csv('Issued.csv',index=False)
                                df5=pd.read_csv('Issued.csv')
                                df6=df5[df5['User']== na]
                                print(df6)
                                print("---SUCCESSFULLY ISSUED---")
                                print("Enjoy your read and return the book with in 10 days of issue date i.e.: ", df6['D_o_Return'].to_string(index=False))
                                q=0
                                s=1
                            else:
                                print("--THIS is already Issued--")
                                print("It will be availabel after: ", (df5['D_o_Return'].to_string(index=False)))
                                q=0
                                s=1
#USER_UPDATE
                        elif b==5:
                            l=1
                            while l==1:
                                print("|=============================|")
                                print("| --WHAT YOU WANT TO CHANGE-- |")
                                print("|        1. Passward          |")
                                print("|        2. Age               |")
                                print("|        3. City              |")
                                print("|        4. Phone No.         |")
                                print("|        5. ==BACK==          |")
                                print("|=============================|")
                                c=int(input("Enter your choice:"))
                #PASSWARD
                                if c==1:
                                    df2=pd.read_csv('User_list.csv')
                                    pas=input("Enter New Password: ")
                                    d=(df2[df2['User']==u].index.values)
                                    df2.loc[d,["Password"]]=pas
                                    df2.to_csv('User_list.csv',index=False)
                                    df3=df2[df2['User']== u]
                                    print(df3)
                                    print("==Successfully changed==")
                                    l=1
                                    q=0
                                    s=0
                #AGE
                                elif c==2:
                                    df2=pd.read_csv('User_list.csv')
                                    pas=input("Enter Current new Age: ")
                                    d=(df2[df2['User']==u].index.values)
                                    df2.loc[d,["Age"]]=pas
                                    df2.to_csv('User_list.csv',index=False)
                                    df3=df2[df2['User']== u]
                                    print(df3)
                                    print("==Successfully changed==")
                                    l=1
                                    q=0
                                    s=0
                #CITY
                                elif c==3:
                                    df2=pd.read_csv('User_list.csv')
                                    pas=input("Enter New City: ")
                                    d=(df2[df2['User']==u].index.values)
                                    df2.loc[d,["City"]]=pas
                                    df2.to_csv('User_list.csv',index=False)
                                    df3=df2[df2['User']== u]
                                    print(df3)
                                    print("==Successfully changed==")
                                    l=1
                                    q=0
                                    s=0
                #PHONE_NO.
                                elif c==4:
                                    df2=pd.read_csv('User_list.csv')
                                    pas=input("Enter New Phone no: ")
                                    d=(df2[df2['User']==u].index.values)
                                    df2.loc[d,["Phoneno."]]=pas
                                    df2.to_csv('User_list.csv',index=False)
                                    df3=df2[df2['User']== u]
                                    print(df3)
                                    print("==Successfully changed==")
                                    l=1
                                    q=0
                                    s=0
                #BACK TO USER OPTIONS
                                elif c==5:
                                    l=0
                                    q=0
                                    s=1
                                else:
                                    print("x-x-x-x-Enter the correct choise-x-x-x-x")
                                    l=1
                                    q=0
                                    s=0
#BACK TO LOGIN OPTION
                        elif(b==6):
                            q=1
                            s=0
                        else:
                            print("x-x-x-x-Enter the correct choise-x-x-x-x")
                            q=1
                            s=0
#USER_REGISTRATION
            elif (f==2):
                print(" ")
                print("!==============================================!")
                print("!-Please Enter the following details carefully-!")
                print("!==============================================!")
                u=input("        User Name: ")
                Pass=input("        Create Password: ")
                pn=input("        Phoneno.: ")
                ci=input("        City: ")
                ag=input("        Age: ")
                df=pd.read_csv('User_list.csv')                            
                data={"User":[u],"Password":[Pass], "Phone no.":[pn],"City":[ci],"Age":[ag]}
                df2=pd.DataFrame(data)
                df4=df.append(df2)
                df4.to_csv('User_list.csv',index=False)
                df4=pd.read_csv('User_list.csv')
                print("---Successfully Registered---")
                print("")
                print("xxxx--WELCOME TO ABYSS READING WORLD--xxxx")
                print("      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                q=1
            elif(f==3):
                q=0
                m=1
            else:
                print("x-x-x-x-Enter the correct choise-x-x-x-x")
                q=0
                m=1
    else:
        print("x-x-x-x-Enter the correct choise-x-x-x-x")
        m=1
