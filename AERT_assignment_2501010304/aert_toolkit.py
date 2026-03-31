#Part A: Stack ADT (ADT + Operations)
class StackADT:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    

#Part B : Factorial & Fibonacci (Recursion + Complexity)
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

#Fibonacci naive with call counter
naive_calls = 0

def fib_naive(n):
    global naive_calls
    naive_calls += 1

    if n < 0:
        return "Invalid input"
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_naive(n - 1) + fib_naive(n - 2)

#Fibonacci memoized with call counter
memo_calls = 0

def fib_memo(n, memo=None):
    global memo_calls
    memo_calls += 1

    if memo is None:
        memo = {}

    if n < 0:
        return "Invalid input"
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


#Part C : Tower of Hanoi (Recursion + Trace)
def hanoi(n, source, auxiliary, destination, move_stack):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        move_stack.push(move)
        return

    hanoi(n - 1, source, destination, auxiliary, move_stack)

    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    move_stack.push(move)

    hanoi(n - 1, auxiliary, source, destination, move_stack)



#Part D: Recursive Binary Search (Divide & Conquer + Recurrence)
def binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)
    
def main():
    print("****AERT: Algorithmic Efficiency & Recursion Toolkit****\n")

    # Part A: Stack ADT
    print("----- Part A: Stack ADT -----")
    stack = StackADT()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack size:", stack.size())
    print("Top element:", stack.peek())
    print("Popped element:", stack.pop())
    print("Is stack empty?", stack.is_empty())
    print("Stack size after pop:", stack.size())

    print("\n")

    # Part B: Factorial
    print("----- Part B: Factorial -----")
    factorial_tests = [0, 1, 5, 10]
    for n in factorial_tests:
        print(f"factorial({n}) = {factorial(n)}")

    print("\n")

    # Part B: Fibonacci
    print("----- Part B: Fibonacci -----")
    fibonacci_tests = [5, 10, 20, 30]

    for n in fibonacci_tests:
        global naive_calls, memo_calls

        naive_calls = 0
        naive_result = fib_naive(n)

        memo_calls = 0
        memo_result = fib_memo(n)

        print(f"n = {n}")
        print(f"Naive Fibonacci result = {naive_result}, calls = {naive_calls}")
        print(f"Memoized Fibonacci result = {memo_result}, calls = {memo_calls}")
        print()

    # Part C: Tower of Hanoi
    print("----- Part C: Tower of Hanoi (N = 3) -----")
    move_stack = StackADT()
    hanoi(3, 'A', 'B', 'C', move_stack)

    print("\nStored Hanoi moves in Stack:")
    temp_stack = StackADT()

    while not move_stack.is_empty():
        temp_stack.push(move_stack.pop())

    while not temp_stack.is_empty():
        print(temp_stack.pop())

    print("\n")

    # Part D: Recursive Binary Search
    print("----- Part D: Recursive Binary Search -----")
    arr = [1, 3, 5, 7, 9, 11, 13]
    search_keys = [7, 1, 13, 2]

    for key in search_keys:
        result = binary_search(arr, key, 0, len(arr) - 1)
        print(f"Search {key} in {arr} -> Index = {result}")

    empty_arr = []
    result = binary_search(empty_arr, 5, 0, len(empty_arr) - 1)
    print(f"Search 5 in empty list -> Index = {result}")    

if __name__ == "__main__":
    main()