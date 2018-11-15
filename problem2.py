number = int(input("Enter an integer upper from 0:"))

for x in range(2, number+1):
    isPrime=True
    for y in range(2, x):
        if(x % y) == 0:
            isPrime=False
            break

    if isPrime:
        print(x)
      
