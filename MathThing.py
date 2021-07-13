sequence = []
for n in range(1, 20):
    sequence.append(2 ** n - 1)

def alt_sum(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i] if i % 2 == 0 else -numbers[i]
    return abs(sum)
    