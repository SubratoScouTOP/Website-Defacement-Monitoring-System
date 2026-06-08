def detect_change(previous_hash, current_hash):
    """
    Compare previous and current hash.
    """

    if previous_hash is None:
        return "FIRST_RUN"

    if previous_hash == current_hash:
        return "NO_CHANGE"

    return "CHANGED"