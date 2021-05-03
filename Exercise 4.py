print("Enter the no. of rows you want to print pattern")
rows=int(input())
print("IN which style you want to print i.e 1/0 \n ")
style=int(input())
new= bool(style)
if style == True:
    for i in range(1,rows+1):
        # print(i)
        for j in range(1,i+1):
            print("*",end=" ")
        print()

elif style== False:
    for i in range(rows,0,-1):
        for j in (1,i+1):
            print("*",end=" ")
        print()
