# INFO-B-211-Assignment-1
# Password Generator Project

## Purpose
This project generates secure passwords in two formats:
1. Memorable passwords using real English words
2. Random passwords using various character types

Each generated password is saved along with the date and time it was created.

---

## Password Types

### 1. Memorable Password
- Uses `n` random English nouns
- Adds a random single-digit number to each word
- Concatenates words using hyphens (-)
- Supports lowercase, uppercase, or title case

**Example:**
apple3-forest7-moon1

---

### 2. Random Password
- Uses a mix of:
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Optional punctuation
- Supports excluding specific characters

**Example:**
A9$fQ2!xM

---

## Input
- Password type (`memorable` or `random`)
- Parameters depending on password type:
  - Memorable: number of words, case option
  - Random: length, punctuation inclusion, excluded characters

---

## Output
- Generated password printed or returned
- Password + timestamp appended to:
  - `Memorable/Generated_Passwords.txt`
  - `Random/Generated_Passwords.txt`

---

## File Structure
