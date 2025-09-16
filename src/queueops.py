from typing import List, Tuple

def take_next(queue: List[str]) -> Tuple[str | None, List[str]]:
    if not queue:
        return (None, [])
    return (queue[0], queue[1:])

def move_to_back(queue: List[str], name: str) -> List[str]:
    if name not in queue:
        return queue[:]
    q = queue[:]
    q.remove(name)
    q.append(name)
    return q

def interleave(q1: List[str], q2: List[str]) -> List[str]:
    result = []
    n = min(len(q1), len(q2))
    for i in range(n):
        result.append(q1[i])
        result.append(q2[i])
    result.extend(q1[n:])
    result.extend(q2[n:])
    return result
