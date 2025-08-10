# Crafting efficient and maintainable regular expressions patterns requires following certain best practices t ensure clarity, performance, and ease of understanding. Here are some best practices for writing regex patterns in Python:

import re

# 1. Use raw strings:
#    Always use raw strings (prefix with `r`) for regex patterns to avoid issues with escape sequences.
char_class_matches = re.findall(char_class_pattern, char_class_text)

# 2. Use comments:
#    Use the `re.VERBOSE` flag to write multi-line regex patterns with comments for better readability.
verbose_pattern = r"""
(?x)  # Enable verbose mode
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
#    This allows you to break down complex patterns and add explanations.
# 3. Use character classes:
#    Use character classes to match specific sets of characters, which can make patterns more readable.
char_class_pattern = r"[a-zA-Z0-9]"
char_class_text = "Sample text with numbers 123 and letters abc."
char_class_matches = re.findall(char_class_pattern, char_class_text)
print(
    char_class_matches
)  # Output: ['S', 'a', 'm', 'p', 'l', 'e', ' ', 't', 'e', 'x', 't', ' ', 'w', 'i', 't', 'h', ' ', 'n', 'u', 'm', 'b', 'e', 'r', 's', ' ', '1', '2', '3', ' ', 'a', 'n', 'd', ' ', 'l', 'e', 't', 't', 'e', 'r', 's', ' ', 'a', 'b', 'c']
# 4. Use non-capturing groups:
#    Use non-capturing groups `(?:...)` when you don't need to capture a group for back-referencing, which can improve performance.
non_capturing_pattern = r"(?:\d{3})-(\d{2})-(\d{4})"
non_capturing_text = "My number is 123-45-6789."
non_capturing_matches = re.findall(non_capturing_pattern, non_capturing_text)
print(non_capturing_matches)  # Output: ['45', '6789']
# 5. Use anchors:
#    Use anchors (`^` for start, `$` for end) to specify the position of the match, which can help avoid unnecessary matches.
anchor_pattern = r"^\d{3}-\d{2}-\d{4}$"
anchor_text = "123-45-6789"
anchor_matches = re.findall(anchor_pattern, anchor_text)
print(anchor_matches)  # Output: ['123-45-6789']
# 6. Use flags for case sensitivity:
#    Use flags like `re.IGNORECASE` to perform case-insensitive matching when necessary.
case_insensitive_pattern = r"hello"
case_insensitive_text = "Hello world! hello again."
case_insensitive_matches = re.findall(
    case_insensitive_pattern, case_insensitive_text, flags=re.IGNORECASE
)
print(case_insensitive_matches)  # Output: ['Hello', 'hello']
# 7. Use flags for multiline matching:
multiline_text = "First line\nSecond line\nThird line"
multiline_pattern = r"^\w+"
multiline_matches = re.findall(multiline_pattern, multiline_text, flags=re.MULTILINE)
print(multiline_matches)  # Output: ['First', 'Second', 'Third']
# 8. Use flags for logical OR matching:
or_pattern = r"cat|dog"
or_text = "I have a cat and a dog."
or_matches = re.findall(or_pattern, or_text)
print(or_matches)  # Output: ['cat', 'dog']
# 9. Use flags for word boundaries:
word_boundary_pattern = r"\bword\b"
word_boundary_text = "This is a word in a sentence."
word_boundary_matches = re.findall(word_boundary_pattern, word_boundary_text)
print(word_boundary_matches)  # Output: ['word']
# use raw strings to avoid issues with escape sequences
# for example, use `r"\d"` instead of `"\d"`.
# Compile regex pattersns:
#    Compile regex patterns using `re.compile()` for better performance, especially if the pattern is used multiple times.
compiled_pattern = re.compile(r"\d{3}-\d{2}-\d{4}")
compiled_text = "My number is 123-45-6789."
compiled_matches = compiled_pattern.findall(compiled_text)
print(compiled_matches)  # Output: ['123-45-6789']
# 10 document your regex patterns:
#    Add comments to explain complex regex patterns, making it easier for others (and yourself) to understand their purpose and functionality.
# 11 keep patterns simple:
#    Avoid overly complex patterns that are hard to read and maintain. Break them down into simpler components if necessary.
# 12 Use character classes:
#    Use character classes to match specific sets of characters, which can make patterns more readable.
# 13 Be mindfull of performance:
#    Be mindful of performance, especially with large texts. Avoid patterns that can lead to excessive backtracking, such as nested quantifiers.
# 14 optimize quantifiers:
#    Use quantifiers wisely to avoid excessive backtracking. For example, prefer `*?` over `*` when you want to match zero or one occurrence, and use `{min,max}` to specify a range of occurrences.
# 15 escape special characters:
#    Use escape sequences for special characters (like `.` or `*`) when you want to match them literally. For example, use `r"\." to match a literal dot.
# 16 Test your regex patterns:
#    Test your regex patterns with various inputs to ensure they behave as expected. Use online regex testers or unit tests in your code.
# 17 Use tools and resources:
#    Utilize regex testing tools and resources to validate and debug your patterns. Websites like regex101.com provide interactive environments for testing regex patterns with explanations.
# 18 Profile your code:
#    Profile your code to identify performance bottlenecks related to regex matching, especially in large texts. Use tools like `cProfile` to analyze the performance of your regex operations.
# know when not to use regex:
#    Recognize when regex is not the best tool for the job. For simple string operations like splitting or replacing, consider using built-in string methods like `str.split()` or `str.replace()`, which are often more efficient and easier to read.
# Learn and improve:
#    Regular expressions can be complex, so continuously learn and improve your regex skills. Practice with different patterns and scenarios to become more proficient in crafting efficient and maintainable regex expressions.
