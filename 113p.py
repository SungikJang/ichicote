H = int(input())
count = 0

for i in range(H+1):
    for p in range(60):
        for l in range(60):
            if "3" in str(i)+str(p)+str(l):
                count += 1

print(count)