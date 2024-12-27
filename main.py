T = input()
x = [['1', '0']]
if len(T) <= 3:
    x.append([T])
print(x)
result = 0
for i in range(len(x)):
    inner_result = 1
    for j in range(len(x[i])):
        inner_result *= (26 - j)
    result += inner_result

print(result)
