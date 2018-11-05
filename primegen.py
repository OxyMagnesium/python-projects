import math
import time
import multiprocessing

def checkPrime(prime):
    for i in range(2, int(math.sqrt(prime)) + 1):
        if prime % i == 0:
            return 0
    return 1

def checkPrimeWorker(prime, endNum, f):
    fPersonal = 0
    while prime <= endNum - 8:
        result = checkPrime(prime)
        if result:
            fPersonal += 1
        if prime == endNum / 2 or prime == (endNum / 2) + 1:
            print("50% complete.\n")
        prime += 8
    f.value += fPersonal

if __name__ == '__main__':
    mode = input("Enable multiprocessing? Y/N: ").lower()
    endNum = int(input("Enter number to find primes up to: "))

    print("")

    start_time = time.time()
    print("Starting...")

    if mode == 'y':
        with multiprocessing.Manager() as manager:
            f = manager.Value('i', 1)

            p0 = multiprocessing.Process(target = checkPrimeWorker, args = (3, endNum, f))
            p1 = multiprocessing.Process(target = checkPrimeWorker, args = (5, endNum, f))
            p2 = multiprocessing.Process(target = checkPrimeWorker, args = (7, endNum, f))
            p3 = multiprocessing.Process(target = checkPrimeWorker, args = (9, endNum, f))

            p0.start()
            print("Worker 0 started.")
            p1.start()
            print("Worker 1 started.")
            p2.start()
            print("Worker 2 started.")
            p3.start()
            print("Worker 3 started.")

            print("")

            p0.join()
            print("Worker 0 done.")
            p1.join()
            print("Worker 1 done.")
            p2.join()
            print("Worker 2 done.")
            p3.join()
            print("Worker 3 done.")

            prime = endNum - 8 + 1
            found = f.value
    else:
        prime = 2
        found = 0

    while prime <= endNum:
        result = checkPrime(prime)
        if result:
            found += 1
        prime += 1

    end_time = time.time()
    print("All done!")

    print("")

    print("Primes found: " + str(found))
    print("Time taken: " + str(round((end_time - start_time), 2)) + " seconds.")

    print("")

    end_stop = input("Press enter to quit.")
