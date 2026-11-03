def multiply(A, B):
    n = len(A)

    # Base case: multiply two numbers
    if n == 1:
        return [A[0] * B[0]]

    mid = n // 2

    # Divide into lower and upper halves
    D0 = A[:mid]
    D1 = A[mid:]
    E0 = B[:mid]
    E1 = B[mid:]

    # Four recursive multiplications
    low = multiply(D0, E0)
    high = multiply(D1, E1)
    cross1 = multiply(D1, E0)
    cross2 = multiply(D0, E1)

    # Combine the four results
    result = [0] * (2 * n - 1)

    for i in range(len(low)):
        result[i] = result[i] + low[i]
        result[i + mid] = result[i + mid] + cross1[i] + cross2[i]
        result[i + 2 * mid] = result[i + 2 * mid] + high[i]

    return result


A = [1, 2, 3, 4]
B = [4, 3, 2, 1]

print(multiply(A, B))
