import multiprocessing as mp
x = 2
def random_calculation(x):
    while True:
        x = x * 2  
        print(x)

p = mp.Pool(processes=mp.cpu_count())
p.map(random_calculation(x), range(mp.cpu_count()))