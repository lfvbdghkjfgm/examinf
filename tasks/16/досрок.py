from functools import lru_cache
from tqdm import tqdm


@lru_cache(1000)
def f(n):
    if n < 10:
        return 3
    return (n + 4) * f(n - 5)


for i in tqdm(range(257500)):
    f(i)
print((f(257487) // 683 + f(257477) // 67) / f(257472))
