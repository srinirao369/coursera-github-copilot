# Function add two numbers
def add(a, b):
    try:
        return a + b
    except TypeError:
        raise ValueError("Both inputs must be numbers")
    
# Function to test add to test_add function using 5  test cases
def test_add():
    try:
        assert add(1, 2) == 3, "Test case 1 failed"
        print("Test case 1 passed")
    except AssertionError as e:
        print(e)

    try:
        assert add(-1, -1) == -2, "Test case 2 failed"
        print("Test case 2 passed")
    except AssertionError as e:
        print(e)

    try:
        assert add(0, 0) == 0, "Test case 3 failed"
        print("Test case 3 passed")
    except AssertionError as e:
        print(e)

    try:
        assert add(1.5, 2.5) == 4.0, "Test case 4 failed"
        print("Test case 4 passed")
    except AssertionError as e:
        print(e)

    try:
        assert add("1", "2") == "12", "Test case 5 failed"  # This will raise ValueError
        print("Test case 5 passed")
    except AssertionError as e:
        print(e)
    except ValueError as e:
        print(f"Test case 5 failed with error: {e}")

    print("Test cases execution completed")

# call the test_add functon
test_add()
