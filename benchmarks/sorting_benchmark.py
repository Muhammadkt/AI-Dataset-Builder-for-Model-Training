import timeit

setup_code = """
from curated_code.sorting import quicksort
import random
arr = [random.randint(0, 1000) for _ in range(1000)]
"""

test_code = "quicksort(arr)"

execution_time = timeit.timeit(stmt=test_code, setup=setup_code, number=100)
print(f"Execution Time: {execution_time:.4f} seconds")

