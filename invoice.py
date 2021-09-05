import MySQLdb
def exit1():
    print("********************Thank you********************")


def database():
    print("")
    print("Welcome to the Nursary")
    try:
            mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nursary")
            query="SELECT * FROM daisies"
            cur=mycon.cursor()
            cur.execute(query)
            tdata=cur.fetchall()
            print(" \n Types of Daisies are: ")
            print("Id: ","\t\tRate: ","\t\tName : ")
            for row in tdata:
                print(row[0],"\t","",row[2],"\t  ",row[1])
            print("_______________________________________")    
                    
    except:
            print("Error")

    finally:
            mycon.commit()
            cur.close()
                
                

        
    

    #print("1. Chrysanthemum Daisy\t : Rs.527 \n2. Barberton Daisy\t : Rs.449 \n3. Shasta Daisy\t :  Rs.145 \n4.Osteospermum Daisies\t : Rs.129 \n5.Pale Purple Coneflower\t : Rs.489 \n6.Gerbera Virdifolia\t : Rs.380 \n7.English Daisy \t: Rs.359 \n8.Rogh Daisy\t : Rs.89 \n9.Mojave Desert Star \t: Rs.229 \n10.Curly Leaf Daisy \t: Rs.95 \n11.To exit")
    ch=int(input("\nEnter your choice "))
    print("")
    print("----------------------------------------------------")
    
    if ch==11:
        print("_____________________EXIT___________________________")
    

    while (ch!=11):
        
        if ch==1:
            
            x1 = 527
            print("\nYou have selected Chrysanthemum Daisy")
            print("Price is ",x1)
            a1 = int(input("Enter number of quantities:"))
            print("Total Amount: ",a1 * x1)
            b1 = int(input("Press 1 to continue \nPress 2 to exit: "))
            if(b1 == 1):
                database()
            if(b1 == 2):
                exit1()
            break
            
            
        if ch==2:
            
            x2 = 449
            print("\nYou have selected Barberton Daisy")
            print("Price is ",x2)
            a2 = int(input("Enter number of quantities:"))
            print("Total Amount: ",a2 * x2)
            b1 = int(input("Press 1 to continue \nPress 2 to exit: "))
            if(b1 == 1):
                database()
            if(b1 == 2):
                exit1()
            break

        if ch==3:
            
            x3 = 145
            print("\nYou have selected Sashta Daisy")
            print("Price is ",x3)
            a3 = int(input("Enter number of quantities:"))
            print("Total Amount: ",a3 * x3)
            b1 = int(input("Press 1 to continue \nPress 2 to exit: "))
            if(b1 == 1):
                database()
            if(b1 == 2):
                exit1()
            break

        if ch==4:
            
            x4 = 129
            print("\nYou have selected Ostermum Daisy")
            print("Price is ",x4)
            a4 = int(input("Enter number of quantities:"))
            print("Total Amount: ",a4 * x4)
            b1 = int(input("Press 1 to continue \nPress 2 to exit: "))
            if(b1 == 1):
                database()
            if(b1 == 2):
                exit1()
            break

        if ch==5:
            
            x5 = 489
            print("\nYou have selected Pale Purple Coneflower")
            print("Price is ",x5)
            a5 = int(input("Enter number of quantities:"))
            print("Total Amount: ",a5 * x5)
            b1 = int(input("Press 1 to continue \nPress 2 to exit: "))
            if(b1 == 1):
                database()
            if(b1 == 2):
                exit1()
            break

        if ch==6:
            
            x6 = 380
            print("\nYou have selected Gerbera Virdifolia")
            print("Price is ",x6)
            a6 = int(input("Enter number of quantities:"))
            print("Total Amount: ",a6 * x6)
            b1 = int(input("Press 1 to continue \nPress 2 to exit: "))
            if(b1 == 1):
                database()
            if(b1 == 2):
                exit1()
            break

        if ch==7:
            
            x7 = 359
            print("\nYou have selected English Daisy")
            print("Price is ",x7)
            a7 = int(input("Enter number of quantities:"))
            print("Total Amount: ",a7 * x7)
            b1 = int(input("Press 1 to continue \nPress 2 to exit: "))
            if(b1 == 1):
                database()
            if(b1 == 2):
                exit1()
            break

        if ch==8:
            
            x8 = 89
            print("\nYou have selected Rough Daisy")
            print("Price is ",x8)
            a8 = int(input("Enter number of quantities:"))
            print("Total Amount: ",a8 * x8)
            b1 = int(input("Press 1 to continue \nPress 2 to exit: "))
            if(b1 == 1):
                database()
            if(b1 == 2):
                exit1()
            break

        if ch==9:
            
            x9 = 229
            print("\nYou have selected Mojave Desert Star")
            print("Price is ",x9)
            a9 = int(input("Enter number of quantities:"))
            print("Total Amount: ",a9 * x9)
            b1 = int(input("Press 1 to continue \nPress 2 to exit: "))
            if(b1 == 1):
                database()
            if(b1 == 2):
                exit1()
            break

        if ch==10:
            
            x10 = 95
            print("\nYou have selected Curly Leaf Daisy")
            print("Price is ",x10)
            a10 = int(input("Enter number of quantities:"))
            print("Total Amount: ",a10 * x10)
            b1 = int(input("Press 1 to continue \nPress 2 to exit: "))
            if(b1 == 1):
                database()
            if(b1 == 2):
                exit1()
            break


database()


exit1()
