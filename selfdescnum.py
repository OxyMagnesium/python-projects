import time

ans = []

print("Started...\n")
start_time = time.time()
for i in range(1000000000, 10000000000):
    flag = 1
    num_str = str(i)
    num_counts = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
    for j in range(10):
        num_counts[int(num_str[j])] += 1
    for k in range(10):
        if int(num_str[k]) != num_counts[k]:
            flag = 0
            break
    if flag:
        ans.append(i)

print("The answers are {0}.".format(ans))
print("Elapsed time: {0} seconds.".format(round(time.time() - start_time, 2)))
