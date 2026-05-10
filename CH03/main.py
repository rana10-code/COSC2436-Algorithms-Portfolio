from recursion import countdown, fact, recursive_sum, recursive_count, recursive_max

def print_header(title: str) -> None:
    # Prints a header for each section to clearly separate output sections
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)

def demo_countdown() -> None:
    # Demonstrates countdown from a given number
    print_header("PART 1: countdown()")
    print("countdown:")
    countdown(5)  # Replace 5 with any number to test different cases

def demo_factorial() -> None:
    # Demonstrates factorial calculation
    print_header("Factorial of 5:")
    print(fact(5))  # Replace 5 with any number to calculate its factorial

def demo_sum() -> None:
    # Demonstrates summing elements of a list using recursion
    print_header("Sum of [2, 4, 6]:")
    print(recursive_sum([2, 4, 6]))  # Replace list with any list of numbers

def demo_count() -> None:
    # Demonstrates counting elements in a list using recursion
    print_header("Count of [1, 2, 3, 4, 5]:")
    print(recursive_count([1, 2, 3, 4, 5]))  # Replace list with any list

def demo_max() -> None:
    # Demonstrates finding the maximum element in a list using recursion
    print_header("Max of [3, 7, 2, 9, 1]:")
    print(recursive_max([3, 7, 2, 9, 1]))  # Replace list with any list of numbers

def main() -> None:
    # Runs all demonstration functions
    demo_countdown()
    demo_factorial()
    demo_sum()
    demo_count()
    demo_max()

if __name__ == "__main__":
    main()  # Calls the main function to execute all demos
