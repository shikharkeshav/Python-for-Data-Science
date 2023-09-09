marks=[]
subject=["Physics","Chemistry","Maths"]
for i in range(3):
    marks.append(int(input("Enter marks in {}  ".format(subject[i]))))
avg = sum(marks)/3
print("Average is {}".format(avg))

if avg>40:
    print("Passed")
else:
    print("Failed")