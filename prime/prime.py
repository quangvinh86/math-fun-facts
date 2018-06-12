"""
@author: vinh.nguyenquang
@email: quangvinh19862003@gmail.com

"""
import math


def is_prime_normal_solution(number):
    if number <= 1:
        return False
    max_range = int(math.sqrt(number)) + 1
    for counter in range(2, max_range):
        if not number % counter:
            return False
    return True


def is_prime_advance_solution(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif not number % 2:
        return False
    max_range = int(math.sqrt(number)) + 1
    for counter in range(3, max_range, 2):
        if not number % counter:
            return False
    return True


if __name__ == "__main__":
    import time
    number = 9999999111111112
    print("is_prime_normal_solution: {} ".format(number), end=' ')
    start = time.time()
    print(is_prime_normal_solution(number), end=' ')
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))

    print("is_prime_advance_solution: {} ".format(number), end=' ')
    start = time.time()
    print(is_prime_advance_solution(number), end=' ')
    done = time.time()
    elapsed = done - start
    print("elapsed time: {}s".format(elapsed))
