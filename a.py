from multiprocessing import Pool, cpu_count
x = 2
def random_calculation(x):
    while True:
        x = x * x
        print(x)

p = Pool(processes=cpu_count())
p.map(random_calculation(x), range(cpu_count()))