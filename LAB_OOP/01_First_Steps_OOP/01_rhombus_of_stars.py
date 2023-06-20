def print_row(n, count):
    print(" " * (n - count), end="")
    print(*["*"] * count)

def print_triangle(n):
    for count in range(1, n + 1):
        print_row(n, count)

def print_reversed_triangle(n):
    for count in range(n - 1, 0, -1):
        print_row(n, count)

def print_romb(n):
    print_triangle(n)
    print_reversed_triangle(n)


n = int(input())
print_romb(n)

