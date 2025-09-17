from typing import List, Tuple, Optional

def take_next(queue: List[str]) -> Tuple[Optional[str], List[str]]:
    if not queue:
        return None, []
    return queue[0], queue[1:]

def move_to_back(queue: List[str], name: str) -> List[str]:
    q = list(queue)
    if name in q:
        q.remove(name)
        q.append(name)
    return q

def interleave(q1: List[str], q2: List[str]) -> List[str]:
    out = []
    n = min(len(q1), len(q2))
    for i in range(n):
        out.append(q1[i])
        out.append(q2[i])
    out.extend(q1[n:])
    out.extend(q2[n:])
    return out
