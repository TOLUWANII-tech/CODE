def prime_checker(number):
    prime=True
    for num in range(2,number):
        if number % num==0:
            prime=False
    if prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")



n = int(input('What number do you want to check? '))
prime_checker(number = n)
