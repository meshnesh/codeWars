def sum_dig_pow(a, b):
    def division(x):
        L = []
        while x >= 0:
            L.append(x % 10)
            x = round((x - x % 10)/10)
            if x == 0:
                break
        return L[::-1]
    def sum(y):
        sum = 0
        for index, item in enumerate(division(y)):
            sum += item ** (index+1)
        return sum
    return [i for i in range(a, b+1) if i == sum(i)]