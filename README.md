# Polynomial Multiplication

Each list stores coefficients starting with the constant term. For example, multiplying `[1, 2]` by `[3, 4]` gives `[3, 10, 8]`, representing `3 + 10x + 8x^2`.

- [Direct multiplication](polynomial_multiplication.py) multiplies every pair of coefficients and adds terms with the same power.
- [Naive recursive multiplication](naive_polynomial.py) splits each polynomial in half and combines four smaller products.
- [Karatsuba multiplication](karatsuba_polynomial.py) uses three smaller products. Multiplying the sums of the halves and subtracting the low and high products gives the middle terms.

All three use nonempty lists of equal length. The recursive versions also require that length to be a power of two, such as 1, 2, 4, or 8.
