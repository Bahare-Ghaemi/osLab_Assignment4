
count_ = int(input("How many terms? "))

n1, n2 = 0, 1
e = 0

if count_ <= 0:
   print("Please enter a positive integer")
elif count_ == 1:
   print("Fibonacci sequence upto",count_,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while e < count_:
       print(n1,end=" ")
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       e += 1