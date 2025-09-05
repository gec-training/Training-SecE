print('Hello Feature')

def placeholder_function():
    pass  # Placeholder for future implementation

# Recursive function to calculate factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    num = 5
    print(f"Factorial of {num} is {factorial(num)}")
