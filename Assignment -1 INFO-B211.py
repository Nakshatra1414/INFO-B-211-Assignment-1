import random
import string
import os
from datetime import datetime


# ---------------------------
# Helper Functions
# ---------------------------
file_path = "/Users/khush/Downloads/top_english_nouns_lower_100000.txt"
def load_words(file_path):
    """Load words from a text file into a list."""
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]


def ensure_directory(directory):
    """Create directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)


def log_password(directory, password):
    """Append generated password and timestamp to a file."""
    ensure_directory(directory)
    file_path = os.path.join(directory, "Generated_Passwords.txt")

    timestamp = datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file:
        file.write(f"{password} | Created on: {timestamp}\n")


# ---------------------------
# Password Generators
# ---------------------------

def generate_memorable_password(num_words, case_option, word_list):
    """
    Generate a memorable password.
    case_option: 'lower', 'upper', or 'title'
    """
    words = random.sample(word_list, num_words)
    password_parts = []

    for word in words:
        number = str(random.randint(0, 9))

        if case_option == "upper":
            word = word.upper()
        elif case_option == "title":
            word = word.title()

        password_parts.append(word + number)

    password = "-".join(password_parts)
    log_password("Memorable", password)
    return password


def generate_random_password(length, include_punctuation, excluded_chars):
    """Generate a random password."""
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

    if include_punctuation:
        characters += string.punctuation

    # Remove excluded characters
    characters = "".join(c for c in characters if c not in excluded_chars)

    password = "".join(random.choice(characters) for _ in range(length))
    log_password("Random", password)
    return password


# ---------------------------
# Main Generator
# ---------------------------

def password_generator(password_type, **kwargs):
    """Generate either a memorable or random password."""
    if password_type == "memorable":
        return generate_memorable_password(
            kwargs["num_words"],
            kwargs["case_option"],
            kwargs["word_list"]
        )

    elif password_type == "random":
        return generate_random_password(
            kwargs["length"],
            kwargs["include_punctuation"],
            kwargs["excluded_chars"]
        )

    else:
        raise ValueError("Invalid password type selected.")


# ---------------------------
# Confirmation Test: Generate 1000 Passwords
# ---------------------------

if __name__ == "__main__":
    word_file = "/Users/khush/Downloads/top_english_nouns_lower_100000.txt"
    words = load_words(word_file)

    for _ in range(1000):
        chosen_type = random.choice(["memorable", "random"])

        if chosen_type == "memorable":
            password_generator(
                "memorable",
                num_words=random.randint(2, 4),
                case_option=random.choice(["lower", "upper", "title"]),
                word_list=words
            )

        else:
            password_generator(
                "random",
                length=random.randint(8, 16),
                include_punctuation=random.choice([True, False]),
                excluded_chars="Il1O0"
            )

    print("1000 passwords generated and logged successfully.")
