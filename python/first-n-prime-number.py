#!/usr/bin/env python

class Primes:

    def __init__(self):
        self.fc = 0

    def is_prime(self, x):
        for i in range(x):
            ignore = [0,1,x]
            # import pdb;pdb.set_trace()
            if i in ignore:
                continue 
            mod = x % i
            if mod == 0:
                return False
        return True

    def first(self, n):
        out = []
        x = 2
        while self.fc != n:
            if not self.is_prime(x):
                x = x + 1
                continue
            out.append(x)
            x = x + 1
            self.fc = self.fc + 1
        return out

if __name__ == "__main__":
    p = Primes()
    print p.first(3)
