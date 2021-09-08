result = []
def fizzbuzz(n):
    for x in range(1, 1+n):
        if x % 15 == 0:
            result.append("fizzbuzz")
        elif x % 3 == 0:
            result.append("fizz")
        elif x % 5 == 0:
            result.append("buzz")
        else:
            result.append (x)
