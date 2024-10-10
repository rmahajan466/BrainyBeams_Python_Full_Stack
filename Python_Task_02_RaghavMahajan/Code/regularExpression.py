import re

# Input string
text = input("Enter string: ")

# Regular expression pattern to find words containing exactly two 'a's
pattern = r'\b\w*a\w*a\w*\b'

# Find all matches
matches = re.findall(pattern, text)

# Print the matches
print("Words containing exactly two 'a's:", matches)

