def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())  # Remove spaces and punctuation, and convert to lowercase
    return s == s[::-1]