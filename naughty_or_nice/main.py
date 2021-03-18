from typing import List

NAUGHTY = -1
NICE = 1
NEITHER = 0


def is_naughty_or_nice(action: str):
    if action.startswith("g") or action.startswith("n") or action.startswith("s"):
        return NICE
    if action.startswith("b") or action.startswith("f") or action.startswith("k"):
        return NAUGHTY
    else:
        return NEITHER


def naughty_or_nice(actions: List[str]):
    action_morality = [is_naughty_or_nice(action) for action in actions]

    nice_actions = sum(1 for action in action_morality if action == NICE)
    naughty_actions = sum(1 for action in action_morality if action == NAUGHTY)

    if nice_actions > naughty_actions:
        return NICE
    elif naughty_actions > nice_actions:
        return NAUGHTY
    else:
        return NEITHER
