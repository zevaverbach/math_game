# coding: utf-8
def see_how_fast_this_computer_counts_per_second():
    start = time.time()
    for i in range(1_000_000):
        print(i)
    end = time.time()
    took_seconds = end - start
    return 1_000_000 / took_seconds
    
