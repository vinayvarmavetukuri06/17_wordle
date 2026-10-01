def evaluate(target, guess):
    result = ["gray"] * len(guess)

    # Keep track of target letters that have not already
    # been used by an exact (green) match.
    remaining = list(target)

    # First pass: exact matches.
    for i, ch in enumerate(guess):
        if ch == target[i]:
            result[i] = "green"
            remaining[i] = None

    # Second pass: present but misplaced letters.
    for i, ch in enumerate(guess):
        if result[i] == "green":
            continue

        if ch in remaining:
            result[i] = "yellow"
            remaining[remaining.index(ch)] = None

    return result
