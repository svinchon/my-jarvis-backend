from rapidfuzz import fuzz, process


def is_nickname(text, nickname, threshold=80):
    """
    Checks if a given text contains a string that is similar to the provided nickname.
    Args:
        text (str): The text to search within.
        nickname (str): The nickname to search for.
        threshold (int, optional): The minimum similarity score (0-100) to consider a match. Defaults to 80.
    Returns:
        bool: True if a similar string is found, False otherwise.
    """
    # process.extractOne returns a tuple of (best_match, score, index)
    # We only care about the score here.
    result = process.extractOne(nickname, text.split(), scorer=fuzz.WRatio)
    if result:
        score = result[1]
        return score >= threshold
    return False
