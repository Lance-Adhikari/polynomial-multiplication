def karatsuba(A, B):
    n = len(A)

    # Base case
    if n == 1:
        return [A[0] * B[0]]

    mid = n // 2

    # Split each polynomial into its low and high powers.
    D0 = A[:mid]
    D1 = A[mid:]
    E0 = B[:mid]
    E1 = B[mid:]

    # First two recursive multiplications
    low = karatsuba(D0, E0)
    high = karatsuba(D1, E1)

    # Add the halves
    sum_D = [D0[i] + D1[i] for i in range(mid)]
    sum_E = [E0[i] + E1[i] for i in range(mid)]

    # Third recursive multiplication
    combined = karatsuba(sum_D, sum_E)

    # Subtract the low and high products to isolate both cross terms.
    middle = [combined[i] - low[i] - high[i]
              for i in range(len(combined))]

    # Combine results
    result = [0] * (2 * n - 1)

    for i in range(len(low)):
        result[i] = result[i] + low[i]
        result[i + mid] = result[i + mid] + middle[i]
        result[i + 2 * mid] = result[i + 2 * mid] + high[i]

    return result


A = [1, 2, 3, 4]
B = [4, 3, 2, 1]

print(karatsuba(A, B))
