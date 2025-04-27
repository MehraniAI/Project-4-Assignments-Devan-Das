def main():
    print("Delete this line and write your code here! :)")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False  # No need for else, because if the if condition fails, it reaches this line

def main():
    print(in_range(5, 1, 10))  # Example usage: prints True
    print(in_range(15, 1, 10)) # Example usage: prints False

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
