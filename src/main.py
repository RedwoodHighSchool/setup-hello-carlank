"""Assignment 00: Setup + Hello

Implement the functions below. Do NOT use input() in these functions.
The tests will call the functions directly.

Tip: Keep your functions pure (same inputs -> same outputs).
"""

def greet(name: str) -> str:
    """Return a friendly greeting.

    Examples:
        greet("Ada") -> "Hello, Ada!"
    """
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b + 1


if __name__ == "__main__":
    # Optional: you can run this file directly for quick manual checks.
    print(greet("World"))
    print(add(2, 3))
