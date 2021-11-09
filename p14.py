g = int(input().strip())

grades = []

for i in range(g):
        grades_item = int(input().strip())
        grades.append(grades_item)

for i in grades:

    z=int(i/5)
    z=z*5+5
    if(z-i<3):
        if(i<38):
            print(i)
        else:
            print(z)
    else:
        print(i)

