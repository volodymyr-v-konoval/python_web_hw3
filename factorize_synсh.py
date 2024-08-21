from time import time

def factorize(*numbers) -> list:
    '''
    Returns list of numbers division abilities.
    '''
    start = time()
    result = []
    for number in numbers:
        dev = 1
        dev_list = []
        while dev <= number:
            if number % dev == 0:
                dev_list.append(dev)
            dev += 1
        result.append(dev_list)
    print(f"The row function worked {time() - start} seconds.")
    return result

if __name__ == '__main__':
    a, b, c, d  = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
