def find_largest_k(n):
    k = 1
    S = 0
    while S < n:
        k += 1
        S += k
    return k - 1


n = int(input("n: "))

largest_k = find_largest_k(n)
print(f"k max sao cho S(k) < {n} la {largest_k}")
