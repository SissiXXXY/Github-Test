"""A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""
product = []
palindrome = []

def get_product():
    for k in range(10, 100):
        for m in range(10, 100):
            product.append(k * m)


def is_palindrome(num):
    tostr = str(num)
    if tostr[0:] == tostr[-1::-1]:
        return True
    else:
        return False


get_product()
print(product)
print(str(121))
print('forward ' + str(121)[0:])
print('backward ' + str(121)[-1:])

for p in product:
    print(is_palindrome(p))
    if is_palindrome(p):
        palindrome.append(p)

print(max(palindrome))
