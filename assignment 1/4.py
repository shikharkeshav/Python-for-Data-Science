sample=[]
def menu():
    print(sample)
    print("insertion or deletion")


    fn= int(input("enter 1 for insertion, 2 for deletion \n"))

    if fn==1:

        sample.append(int(input("Enter value to be inserted  ")))

        print("value inserted")

    elif fn==2:

        print("1 for deletion by value")

        print("2 for deletion by position")

        print("3 for deletion by range")

        del_command= int(input('>'))

        if del_command==1:

            x=int(input("value to be deleted"))

            if x in sample: sample.remove(x)
            else: 
                print("not in list")

        elif del_command==2:

            x=int(input("Enter position (By index)"))

            if x in sample:

                del sample[x]
            else: print("not in list")

        elif del_command==3:

            lower=int(input("Enter beginning index"))

            upper = int(input("Enter final index (included)"))

            del sample[lower:upper+1]
        else:
            print("wrong input 22")

    else:

        print("wrong input")


while(1):
    menu()

    print("Do you wish to continue? ")

    z= input("y for yes, n for no  ")

    if z=='y':
        pass

    elif z=='n':

        break