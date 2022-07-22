import math

if __name__ == "__main__":
    n = 100
    sum = 0
    for i in range(math.ceil(n / 2)):
        c = math.comb(n, i)
        sum += c
        
    print("Number of combinations:", sum)
    print("Number of rounds:", math.ceil(math.log2(sum)))