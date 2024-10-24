# Task 1
# Objective: Modify the script that extracts to exlude certain domains

# Import the regular expression module
import re

# Text to be searched
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

# Extract all emails
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(emails)

# Extract all emails excluding exclude.com
exclude_emails = re.findall(r'\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(exclude_emails)