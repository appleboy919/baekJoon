N = int(input())
scores = list(map(int, input().split()))

max = scores[0]
max_index = 0
index = 0
for i in scores:
    if i > max:
        max = i
        max_index = index
    index += 1

sum = 0
index = 0
for i in scores:
    if index == max_index:
        continue
    sum += i/max * 100

print('%f' % (sum/N))