"""
Factorial Function with Input Validation
Time Complexity: O(n)
Space Complexity: O(n)
"""
def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        print("Factorial of 5:", factorial(5))
    except ValueError as e:
        print(e)
