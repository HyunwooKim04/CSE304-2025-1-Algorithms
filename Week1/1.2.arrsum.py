from typing import List

def arrsum(n: int, S: List[int]) -> int:
    total = 0
    for i in range(n):
        total += S[i]
    return total
