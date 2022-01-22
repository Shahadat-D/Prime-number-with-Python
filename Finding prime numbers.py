num = int(input("Place your number range from 2 to "))

prime_number_set = [2,3,5,7]

for y in range (2, num + 1):    
    for x in prime_number_set:
        if y % x == 0:
            is_prime = False
            break
        else:
            is_prime = True

    if is_prime:
        prime_number_set.append(y)

print(f"total Prime number up to {num}", file=open("prime number result.txt", "w"))
print(len(prime_number_set), file=open("prime number result.txt", "a"))
print("current Prime number:", file=open("prime number result.txt", "a"))
for z in prime_number_set:
    print(z, file=open("prime number result.txt", "a"))




