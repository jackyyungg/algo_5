import sys
import time
import matplotlib.pyplot as plt

# Algorithm 1: Brute-Force Algorithm
def matrix_chain_mult_brute_force(p, i, j):
    if i == j:
        return 0
    
    min_mult = sys.maxsize

    for k in range(i, j):
        mult = matrix_chain_mult_brute_force(p, i, k) + matrix_chain_mult_brute_force(p, k + 1, j) + p[i - 1] * p[k] * p[j]
        if mult < min_mult:
            min_mult = mult
    
    return min_mult

# Algorithm 2: Dynamic Programming Algorithm
def matrix_chain_mult_dynamic(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]
    
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = sys.maxsize
            
            for k in range(i, j):
                temp_cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if temp_cost < m[i][j]:
                    m[i][j] = temp_cost
                    s[i][j] = k
    
    return m[1][n], s

# Test the algorithms and measure their running times
input_sizes = [1,2,7,9,10,11,12,13,14,15]
brute_force_times = []
dynamic_times = []



for size in input_sizes:
    dimensions = [size] * (size + 1)
    
    # Measure the running time of the brute-force algorithm
    start_time = time.time()
    k = matrix_chain_mult_brute_force(dimensions, 1, size)
    end_time = time.time()
    brute_force_times.append(end_time - start_time)
    t = end_time - start_time

    # Measure the running time of the dynamic programming algorithm
    start_time = time.time()
    m,s = matrix_chain_mult_dynamic(dimensions)
    end_time = time.time()
    dynamic_times.append(end_time - start_time)
    print(f'input size: {size}')
    print( f'brute_force: {t}')
    print(f'dynamic: {end_time - start_time}')

# Plot the running times
plt.plot(input_sizes, brute_force_times, label='Brute Force')
plt.plot(input_sizes, dynamic_times, label='Dynamic Programming')
plt.xlabel('Input Size')
plt.ylabel('Running Time (seconds)')
plt.legend()
plt.show()