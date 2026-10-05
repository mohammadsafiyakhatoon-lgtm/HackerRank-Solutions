A, B = map(int, input().split())
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return d, x, y
D, x, y = extended_gcd(A, B)
if x > y:
    k = (x - y + (B // D) - 1) // (B // D)
    x = x - k * (B // D)
    y = y + k * (A // D)
print(x, y, D)
  
  
