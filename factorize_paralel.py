from time import time
from multiprocessing import Pool, cpu_count


cores = cpu_count()

def devision_check(number: int) -> list:
    """
    Returns list of numbers division abilities.
    """
    dev = 1
    dev_list = []
    while dev <= number:
        if number % dev == 0:
            dev_list.append(dev)
        dev += 1
    return dev_list


def factorize(*numbers) -> list:
    '''    
    Counts the result in paralel processes.
    '''
        
    start = time()
    with Pool(cores) as pool:
        results = pool.map(devision_check, numbers)
    print(f"The parelel function worked {time() - start} seconds.")
    return results

if __name__ == '__main__':
    
    a, b, c, d  = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

  
