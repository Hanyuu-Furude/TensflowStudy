# def loop(n: int) -> int:
#     if n >= 3:
#         return loop(n - 3) + loop(n - 2) + loop(n - 1)
#     elif n == 2:
#         return loop(n - 2) + loop(n - 1)
#     elif n == 1:
#         return loop(n - 1)
#     else:
#         return 1

# if __name__ == "__main__":
#     x = int(input('Please input the number of stairs:'))
#     print('---\nTotal',loop(x),'ways to reach the extra stairs you have input. ')
import numpy


def loop(target: int) -> int:
    if target == 1:
        return 1
    if target == 2:
        return 2
    if target == 3:
        return 4
    a = 1
    b = 2
    c = 4
    for n in range(4, target+1):
        if a < min(b, c):
            a = a + b + c
        elif b < min(a, c):
            b = a + b + c
        else:
            c = a + b + c
    if a > max(b, c):
        return a
    elif b > max(a, c):
        return b
    else:
        return c


if __name__ == "__main__":
    storge = numpy.zeros(1000)
    storge[0] = 1
    x = int(input('Please input the number of stairs:'))
    print('---\nTotal', loop(x), 'ways to reach the extra stairs you have input. ')
