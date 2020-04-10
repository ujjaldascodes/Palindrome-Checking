num=input("Enter the number or any string:")
list=[]
for i in str(num):
    list.append(i)
revlist=list[::-1]
if str(list) in str(revlist):
    print("Palindrome")
else:
    print("Sorry,Not a Palindrome")
