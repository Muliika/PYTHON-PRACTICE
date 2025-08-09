# In python, regular expressions (regex) are strings of characters that define a search pattern. These patterns can be used to find specific words, phrases, or patterns in text.
# An overview of regex syntax and patterns is as follows:
import re

# 1. Special characters:
#    - `.`: Matches any character except a newline.
#    - `^`: Matches the start of a string.
#    - `$`: Matches the end of a string.
#    - `*`: Matches 0 or more repetitions of the preceding element.
#    - `+`: Matches 1 or more repetitions of the preceding element.
#    - `?`: Matches 0 or 1 repetition of the preceding element.
#    - `[]`: Matches any single character within the brackets.
#    - `[^]`: Matches any single character that is not within the brackets.
#    - `|`: Acts as a logical OR between expressions.
#    - `()`: Groups expressions and captures the matched text.
# 2. Character classes:
#    - `\d`: Matches any digit (0-9).
#    - `\w`: Matches any word character (a-z, A-Z, 0-9, _).
#    - `\s`: Matches any whitespace character (space, tab, newline).
#    - `\b`: Matches a word boundary (between a word character and a non-word character).
# 3. Quantifiers:
#    - `{n}`: Matches exactly n repetitions of the preceding element.
#    - `{n,m}`: Matches between n and m repetitions of the preceding element.
# 4. Escape sequences:
#    - `\`: Escapes a special character, allowing it to be treated as a literal character.
# 5. Flags:
#    - `re.IGNORECASE`: Makes the pattern case-insensitive.
#    - `re.MULTILINE`: Allows `^` and `$` to match the start and end of each line, not just the start and end of the entire string.
# Example usage of regex in Python:
# Search for a pattern in a string
pattern = r"\bhello\b"
text = "Hello world! hello again."
matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)  # Output: ['hello', 'hello']
# Replace a pattern in a string
replacement = re.sub(pattern, "hi", text, flags=re.IGNORECASE)
print(replacement)  # Output: 'hi world! hi again.'
# Match a pattern at the start of a string
start_pattern = r"^Hello"
start_match = re.match(start_pattern, text, flags=re.IGNORECASE)
if start_match:
    print("Match found at the start of the string.")
else:
    print("No match found at the start of the string.")
# Match a pattern at the end of a string
end_pattern = r"again\.$"
end_match = re.search(end_pattern, text, flags=re.IGNORECASE)
if end_match:
    print("Match found at the end of the string.")
else:
    print("No match found at the end of the string.")
# Grouping and capturing matches
group_pattern = r"(\w+) (\w+)"
group_text = "Hello world"
group_matches = re.findall(group_pattern, group_text)
print(group_matches)  # Output: [('Hello', 'world')]
# Using character classes
char_class_pattern = r"[aeiou]"
char_class_text = "Hello world"
char_class_matches = re.findall(char_class_pattern, char_class_text)
print(char_class_matches)  # Output: ['e', 'o', 'o']
# Using quantifiers
quantifier_pattern = r"\d{2,4}"
quantifier_text = "Year 2023, 1999, and 20"
quantifier_matches = re.findall(quantifier_pattern, quantifier_text)
print(quantifier_matches)  # Output: ['2023', '1999', '20']
# Using escape sequences
escape_pattern = r"\d\.\d"
escape_text = "The price is 12.99 and 3.50."
escape_matches = re.findall(escape_pattern, escape_text)
print(escape_matches)  # Output: ['12.9', '3.5']
# Using flags for case-insensitive matching
case_insensitive_pattern = r"hello"
case_insensitive_text = "Hello world! hello again."
case_insensitive_matches = re.findall(
    case_insensitive_pattern, case_insensitive_text, flags=re.IGNORECASE
)
print(case_insensitive_matches)  # Output: ['Hello', 'hello']
# Using multiline flag
multiline_text = "First line\nSecond line\nThird line"
multiline_pattern = r"^\w+"
multiline_matches = re.findall(multiline_pattern, multiline_text, flags=re.MULTILINE)
print(multiline_matches)  # Output: ['First', 'Second', 'Third']
# Using logical OR
or_pattern = r"cat|dog"
or_text = "I have a cat and a dog."
or_matches = re.findall(or_pattern, or_text)
print(or_matches)  # Output: ['cat', 'dog']
# Using word boundaries
word_boundary_pattern = r"\bword\b"
word_boundary_text = "This is a word in a sentence."
word_boundary_matches = re.findall(word_boundary_pattern, word_boundary_text)
print(word_boundary_matches)  # Output: ['word']
# Using non-capturing groups
non_capturing_pattern = r"(?:\d{3})-(\d{2})-(\d{4})"
non_capturing_text = "My number is 123-45-6789."
non_capturing_matches = re.findall(non_capturing_pattern, non_capturing_text)
print(non_capturing_matches)  # Output: ['45', '6789']
# Using lookahead assertions
lookahead_pattern = r"\d+(?= dollars)"
lookahead_text = "I have 100 dollars and 50 cents."
lookahead_matches = re.findall(lookahead_pattern, lookahead_text)
print(lookahead_matches)  # Output: ['100']
# Using lookbehind assertions
lookbehind_pattern = r"(?<=\$)\d+"
lookbehind_text = "The price is $20 and $30."
lookbehind_matches = re.findall(lookbehind_pattern, lookbehind_text)
print(lookbehind_matches)  # Output: ['20', '30']
# Using named groups
named_group_pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
named_group_text = "The date is 2023-10-05."
named_group_matches = re.search(named_group_pattern, named_group_text)
if named_group_matches:
    print(named_group_matches.group("year"))  # Output: 2023
    print(named_group_matches.group("month"))  # Output: 10
    print(named_group_matches.group("day"))  # Output: 05
# Using verbose mode for complex patterns
verbose_pattern = r"""
(?P<year>\d{4})  # Match a 4-digit year
-(?P<month>\d{2})  # Match a 2-digit month
-(?P<day>\d{2})  # Match a 2-digit day  
"""
verbose_text = "The date is 2023-10-05."
verbose_matches = re.search(verbose_pattern, verbose_text, re.VERBOSE)
if verbose_matches:
    print(verbose_matches.group("year"))  # Output: 2023
    print(verbose_matches.group("month"))  # Output: 10
    print(verbose_matches.group("day"))  # Output: 05
# Using backreferences
backreference_pattern = r"(\w+) \1"
backreference_text = "hello hello world"
backreference_matches = re.findall(backreference_pattern, backreference_text)
print(backreference_matches)  # Output: ['hello']
# Backreferences allow you to refer to a previously captured group within the same regex pattern.
# This can be useful for matching repeated patterns or validating input formats.
# For example, the pattern r'(\w+) \1' matches a word followed by a space and the same word again.
# In this case, it captures the word 'hello' and matches it again, resulting in ['hello'].
# Using atomic groups
atomic_group_pattern = r"(?>\d{3})-(\d{2})-(\d{4})"
atomic_group_text = "My number is 123-45-6789."
atomic_group_matches = re.findall(atomic_group_pattern, atomic_group_text)
print(atomic_group_matches)  # Output: ['45', '6789']
# Atomic groups are used to prevent backtracking in regex patterns, which can improve performance for certain complex patterns.
# In this example, the pattern r'(?>\d{3})-(\d{2})-(\d{4})' matches a 3-digit number followed by a hyphen, a 2-digit number, another hyphen, and a 4-digit number.
# The atomic group (?>\d{3}) ensures that once the 3-digit number is matched, it cannot be backtracked, which can speed up the matching process in certain cases.
# Using possessive quantifiers
possessive_pattern = r"\d++"
possessive_text = "12345"
possessive_matches = re.findall(possessive_pattern, possessive_text)
print(possessive_matches)  # Output: ['12345']
# Possessive quantifiers are similar to greedy quantifiers but do not allow backtracking.
# In this example, the pattern r'\d++' matches one or more digits in a possessive manner, meaning once it matches '12345', it will not backtrack to find shorter matches.
# This can lead to performance improvements in certain scenarios, especially when dealing with large inputs or complex patterns.
# Using Unicode properties
unicode_property_pattern = r"\p{L}+"
unicode_property_text = "Hello, 世界!"
unicode_property_matches = re.findall(unicode_property_pattern, unicode_property_text)
print(unicode_property_matches)  # Output: ['Hello', '世界']
# Unicode properties allow you to match characters based on their properties, such as letter, digit, or category.
# In this example, the pattern r'\p{L}+' matches one or more Unicode letters, capturing 'Hello' and '世界' from the input text.
# Note: The `\p{L}` syntax is not directly supported in Python's `re` module. Instead, you can use the `regex` module for Unicode property support.
# Example using the `regex` module for Unicode properties (Python 3.9+):
try:
    import regex as re_unicode

    unicode_property_pattern = r"\p{L}+"
    unicode_property_text = "Hello, 世界!"
    unicode_property_matches = re_unicode.findall(
        unicode_property_pattern, unicode_property_text
    )
    print(unicode_property_matches)  # Output: ['Hello', '世界']
except ImportError:
    print(
        "The 'regex' module is not installed. Please install it to use Unicode properties."
    )
# Note: The `regex` module can be installed via pip: `pip install regex`
# Using the `regex` module allows for more advanced regex features, including Unicode properties, which can be useful for matching characters in different languages and scripts.
# Using the `regex` module for advanced regex features (Python 3.9+):
