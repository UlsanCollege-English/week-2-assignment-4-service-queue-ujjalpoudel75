"""Service Queue — Starter

Simulate a simple customer queue with pure functions.
Implement without mutating inputs.
"""
from typing import List, Tuple


def take_next(queue: List[str]) -> Tuple[str | None, List[str]]:
    """Return (next_name, remaining_queue).

    If queue is empty, return (None, []).
    """
    raise NotImplementedError


def move_to_back(queue: List[str], name: str) -> List[str]:
    """Return a new queue where the first occurrence of `name` is moved to the back.

    If `name` is not present, return the queue unchanged (new list).
    """
    raise NotImplementedError


def interleave(q1: List[str], q2: List[str]) -> List[str]:
    """Return an interleaved queue: q1[0], q2[0], q1[1], q2[1], ...

    After the shorter queue runs out, append the rest.
    """
    raise NotImplementedError