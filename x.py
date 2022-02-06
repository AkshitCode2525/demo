from operator import index
cc = []
cn = []
def addCourse():
    d1 = input("Please enter course code : ")
    d2 = input("Please enter course name : ")
    cc.append(d1)
    cn.append(d2)
    print(cc, cn)
    ch = input("Would you like to add[A] a new course or return[R] to the previous menu?  : ")
    if ch == 'A':
        addCourse()
    elif ch == 'R':
        menu()
    else:
        pass
    
sid=[]
sn=[]
def addStudent():
    d1 = input("Please enter student id : ")
    d2 = input("Please enter student name : ")
    sid.append(d1)
    sn.append(d2)
    print(sid, sn)
    ch = input("Would you like to add[A] a new student or return[R] to the previous menu?  : ")
    if ch == 'A':
        addStudent()
    elif ch == 'R':
        menu()
    else:
        pass

r=[]
data=[]#sid,sn,cc,cn,r
def addResult():
    d1 = input("Please enter student id : ")
    if d1 in sid:
        d4 = sid.index(d1)
        d2 = input("Please enter course code : ")
        if d2 in cc:
            d5 = cc.index(d2)
            d3 = int(input("Please enter the final score(Out of 100) : "))
            if d3 in range(0,100):
                r.append(d3)
                data.append(d1)
                data.append(sn[d4])
                data.append(d2)
                data.append(cn[d5])
                data.append(d3)
                print(r)
                print(data)
                ch = input("Would you like to add[A] a new course or return[R] to the previous menu?  : ")
                if ch == 'A':
                    addResult()
                elif ch == 'R':
                    menu()
                else:
                    pass
            else:
                print("Score is not between 0.0 and 100.0 inclusive")
                addResult()
        else:
            print("Course does not exist.")
            addResult()
    else:
        print("Student does not exist.")
        addResult()


def viewResult():
    d2 = input("Please enter course code : ")
    for i in data:
        if i == d2:
            print("student id : ", data[data.index(i)-2])
            print("student name : ", data[data.index(i)-1])
            print("course code : ", data[data.index(i)])
            print("course name : ", data[data.index(i)+1])
            print("Mark Obtained : ", data[data.index(i)+2])
        else:
            print("Course does not exist.")
    ch = input("Would you like to add[A] a new course or return[R] to the previous menu?  : ")
    if ch == 'A':
        viewResult()
    elif ch == 'R':
        menu()

def menu():
    print("""
    1.) Add a course
    2.) Add a student
    3.) Add a result
    4.) View a result
    5.) Quit
    """)
menu()
choice = int(input("Enter your choice : "))
while choice != 5:
    if choice == 1:
        addCourse()
    elif choice == 2:
        addStudent()
    elif choice == 3:
        addResult()
    elif choice == 4:
        viewResult()
    elif choice == 5:
        print("Thank you")
    else:
        print("Invalid option.")
        menu()
    choice = int(input("Enter your choice : "))