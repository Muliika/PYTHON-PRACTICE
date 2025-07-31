# Regular expressions in Python are a powerful tool for matching patterns in text. They provide a concise and flexible way to search for strings that match certain criteria.
# Example 1: Basic Regular Expression
import re

# This example demonstrates how to use a regular expression to find all occurrences of a pattern in a string.
text = "The rain in Spain falls mainly in the plain."
pattern = r"\bain\b"  # Matches the word 'ain'
matches = re.findall(pattern, text)
print("Matches found:", matches)  # Output: Matches found: ['ain', 'ain']
# Example 2: Using Regular Expressions for Validation
# Regular expressions can also be used to validate input formats, such as email addresses or phone numbers.
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
phone_number_pattern = r"\b\d{3}-\d{3}-\d{4}\b"
email = "test@example.com"
phone_number = "123-456-7890"
if re.match(email_pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")
if re.match(phone_number_pattern, phone_number):
    print("Valid phone number")
else:
    print("Invalid phone number")


# Output:
# Valid email address
# Valid phone number
# Example 3: Substituting Text with Regular Expressions
def substitute_text(text, pattern, replacement):
    return re.sub(pattern, replacement, text)


# This function replaces all occurrences of a pattern in the text with a specified replacement string.
text_to_modify = "The rain in Spain falls mainly in the plain."
replacement_text = "sunshine"
modified_text = substitute_text(text_to_modify, r"\bain\b", replacement_text)
print(
    "Modified text:", modified_text
)  # Output: Modified text: The sunshine in sunshine falls mainly in the sunshine.


# Example 4: Splitting Strings with Regular Expressions
def split_text(text, pattern):
    return re.split(pattern, text)


# This function splits a string into a list based on a regular expression pattern.
text_to_split = "apple, banana; orange: grape"
split_characters = [",", ";"]
split_pattern = r"[;,\s]+"  # Matches commas, semicolons, or whitespace
split_result = split_text(text_to_split, split_pattern)
print(
    "Split result:", split_result
)  # Output: Split result: ['apple', 'banana', 'orange', 'grape']
# Example 5: Using Regular Expressions for Complex Patterns
# Regular expressions can also be used to match complex patterns, such as matching HTML tags or URLs.
html_text = "<div>Hello, <b>world</b>!</div>"
html_pattern = r"<(\w+)>.*?</\1>"  # Matches HTML tags
html_matches = re.findall(html_pattern, html_text)
print("HTML tags found:", html_matches)  # Output: HTML tags found: ['div', 'b']
# Example 6: Regular Expressions with Flags
# Regular expressions can be modified with flags to change their behavior, such as making them case-insensitive.
case_insensitive_pattern = r"(?i)rain"  # Case-insensitive match for "rain"
case_insensitive_text = "The Rain in Spain"
case_insensitive_matches = re.findall(case_insensitive_pattern, case_insensitive_text)
print(
    "Case-insensitive matches found:", case_insensitive_matches
)  # Output: Case-insensitive matches found: ['Rain', 'rain']
# Example 7: Using Regular Expressions to Extract Data
# Regular expressions can be used to extract specific data from strings, such as dates or version numbers.
date_text = "Today's date is 2023-10-01."
date_pattern = r"\d{4}-\d{2}-\d{2}"  # Matches dates in YYYY-MM-DD format
date_matches = re.findall(date_pattern, date_text)
print("Date matches found:", date_matches)  # Output: Date matches found: ['2023-10-01']


# Example 8: Regular Expressions for Replacing Multiple Patterns
# You can use regular expressions to replace multiple patterns in a single pass.
def replace_multiple_patterns(text, replacements):
    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text)
    return text


replacements = {r"\bain\b": "sunshine", r"\bthe\b": "a", r"\bworld\b": "place"}
text_to_replace = "The rain in Spain falls mainly in the world."
modified_text_multiple = replace_multiple_patterns(text_to_replace, replacements)
print(
    "Modified text with multiple replacements:", modified_text_multiple
)  # Output: Modified text with multiple replacements: a sunshine in Spain falls mainly in a place.
