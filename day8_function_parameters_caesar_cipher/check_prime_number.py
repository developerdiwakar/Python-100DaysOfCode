#Write your code below this line ๐
def prime_checker(number):
    half_of_number = round(number/2)
    prime = True
    for n in range(2, half_of_number + 1):
        if number % n == 0:
            prime = False
            break
    if prime == False:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)