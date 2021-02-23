def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n-1)*n


def main():
    N = int(input())
    print(factorial(N))


if __name__ == '__main__':
    main()
