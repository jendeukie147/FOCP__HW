def cel_to_far(temp):
    temp = float(temp)
    f = (temp * 1.8) + 32
    result = (f"{temp}C is equivalent to {f}F")
    return result

def far_to_cel(temp):
    temp = float(temp)
    c = (temp - 32) / 1.8
    result = (f"{temp}F is equivalent to {c}C")
    return result

print(cel_to_far(30))
print(far_to_cel(86))