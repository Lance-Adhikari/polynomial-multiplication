def multiply_polynomials(A, B):
    # Both coefficient lists must have the same length.
    n = len(A)
    product = [0] * (2 * n - 1)

    for i in range(n):
        for j in range(n):
            # Multiplying powers i and j contributes to power i + j.
            product[i + j] = product[i + j] + A[i] * B[j]

    return product


# Coefficients are ordered from the constant term to the highest power.
A = [5, 2, 3]
B = [2, 1, 5]

print(multiply_polynomials(A, B))
