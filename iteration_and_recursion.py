# factorial() method returns the factorial of a number. Note: This method only accepts positive integers. The factorial of a number is the sum of the multiplication, of all the whole numbers, from our specified number down to 1. For example, the factorial of 6 would be 6 x 5 x 4 x 3 x 2 x 1 = 720.

def iterative_factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return fact
print(iterative_factorial(3))

def recur_factorial(n):
    if n == 1: return n
    else: return n * recur_factorial(n-1)
    
print(recur_factorial(6))


# A permutation, also called an “arrangement number” or “order”, is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself. A string of length n has n! permutation. Examples: Input : str = 'ABC' Output : ABC ACB BAC BCA CAB CBA.

# recursive permutation

def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)
            
print(permute("ABCD"))

# iterative permutation

# The math. factorial() method returns the factorial of a number. Note: This method only accepts positive integers.

from math import factorial
def permutations(str):
    for p in range(factorial(len(str))):
        print(''.join(str))
        i = len(str) - 1
        while i > 0 and str[i - 1] > str[i]:
            i -= 1
        str[i:] = reversed(str[i:])
        if i > 0:
            q = i
            while str[i - 1] > str[q]:
                q+=1
            temp = str[i - 1]
            str[i - 1] = str[q]
            str[q] = temp
s = 'abc'
s = list(s)
permutations(s)

