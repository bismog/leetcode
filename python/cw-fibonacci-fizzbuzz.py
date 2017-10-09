#!/usr/bin/env python


def fibs_fizz_buzz(m):
    def fib(n):
       a,b = 1,1
       for i in range(n-1):
           a,b = b,a+b
       return a

    def replace(d):
        if d % 15 == 0:
            return "FizzBuzz"
        elif d % 5 == 0:
            return "Buzz"
        elif d % 3 == 0:
            return "Fizz"
        else:
            return d

    fib_list = [replace(fib(x)) for x in range(m+1) if x != 0]
    return fib_list

def main():
    print fibs_fizz_buzz(20)

if __name__ == "__main__":
    main()
