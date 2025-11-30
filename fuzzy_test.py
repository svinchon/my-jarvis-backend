from rapidfuzz import process, fuzz

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

# Example Usage
text1 = "Hey Jarvis, can you set a timer for 5 minutes?"
text2 = "Hey Marvin, what's the weather like?"
text3 = "I'm not talking to you."

nickname = "Jarvis"

print(f"'{text1}' contains nickname '{nickname}': {is_nickname(text1, nickname)}")
print(f"'{text2}' contains nickname '{nickname}': {is_nickname(text2, nickname)}")
print(f"'{text3}' contains nickname '{nickname}': {is_nickname(text3, nickname)}")
