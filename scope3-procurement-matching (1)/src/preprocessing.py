import re

def clean_text(text):
    # Convert the input into a string.
    text = str(text)

    # Convert all characters to lowercase.
    text = text.lower()

    # Remove leading and trailing spaces.
    text = text.strip()

    # Replace punctuation with spaces, preserving letters and numbers.
    text = re.sub(r"[^\w\s]", " ", text)

    # Replace multiple consecutive spaces with a single space.
    text = re.sub(r"\s+", " ", text)

    # Return the cleaned description.
    return text 
