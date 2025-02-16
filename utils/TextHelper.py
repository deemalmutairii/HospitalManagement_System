def capitalize_words(text):
    """Capitalize the first letter of each word in the given text."""
    return " ".join(word.capitalize() for word in text.split())


def truncate_text(text, length=50):
    """Truncate the text to the specified length with ellipsis if it exceeds the length."""
    if len(text) > length:
        return text[:length] + "..."
    return text


def remove_special_characters(text):
    """Remove special characters from the text."""
    import re
    return re.sub(r'[^A-Za-z0-9 ]+', '', text)
