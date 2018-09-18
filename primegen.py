import math
import time

prime = 2
is_prime = True
found = 0
endno = input("Enter number to find primes up to: ")

print("")

start_time = time.time()
print("Starting...")

while prime <= int(endno):
    for i in range(2, int(math.sqrt(prime)) + 1):
        if prime % i == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime == True:
        print(prime)
        found += 1
    prime += 1
    

end_time = time.time()     
print("Done!")

print("")

print("Primes found: " + str(found))
print("Time taken: " + str(round((end_time - start_time), 2)) + " seconds.")

print("")

end_stop = input("Press enter to quit.")
