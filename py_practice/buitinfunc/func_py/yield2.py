def nextSquare():
    i = 1

    # an infinite loop to generate squares
    while True:
        yield i * i
        i += 1


for num in nextSquare():
    if num > 100:
        break
    print(num)
