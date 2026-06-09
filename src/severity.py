def get_severity(similarity_score):
    """
    Determine severity level
    based on similarity percentage.
    """

    if similarity_score >= 95:
        return "LOW"

    elif similarity_score >= 70:
        return "MEDIUM"

    elif similarity_score >= 40:
        return "HIGH"

    else:
        return "CRITICAL"


if __name__ == "__main__":

    test_scores = [
        98,
        85,
        55,
        20
    ]

    for score in test_scores:

        severity = get_severity(score)

        print(
            f"Similarity: {score}% -> Severity: {severity}"
        )