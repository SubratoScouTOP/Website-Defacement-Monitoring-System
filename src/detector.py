def detect_change(
    previous_hash,
    current_hash
):
    """
    Compare previous and current hash.
    """

    if previous_hash is None:
        return "FIRST_RUN"

    if previous_hash == current_hash:
        return "NO_CHANGE"

    return "CHANGED"


if __name__ == "__main__":

    result = detect_change(
        "old_hash",
        "new_hash"
    )

    print(
        f"Detection Result: {result}"
    )