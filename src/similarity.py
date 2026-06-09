from difflib import SequenceMatcher


def calculate_similarity(
    old_content,
    new_content
):
    """
    Calculate similarity percentage
    between two DOM contents.
    """

    similarity = SequenceMatcher(
        None,
        old_content,
        new_content
    ).ratio()

    return round(
        similarity * 100,
        2
    )


if __name__ == "__main__":

    text1 = "Hello World"

    text2 = "Hello Secure World"

    score = calculate_similarity(
        text1,
        text2
    )

    print(
        f"Similarity: {score}%"
    )