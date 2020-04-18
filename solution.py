from collections import Counter
n=sorted(input())
z=Counter(n).most_common(3)

for k in z:
    print(k[0],k[1])

