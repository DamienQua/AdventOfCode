def count_occurences_in_string(str, choice):
    counts = dict()
    words = str
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts[choice]

def second_smallest(numbers):
    m1, m2 = float('inf'), float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2