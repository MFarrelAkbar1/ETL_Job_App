import re

def checkTitleLevel(title: str):
    if "Junior" in title:
        return 1
    elif "Mid" in title:
        return 2
    elif "Senior" in title or "Manager" in title:  # Corrected condition
        return 3
    elif "Executive" in title or "Head" in title:  # Corrected condition
        return 4
    else:
        return 2  # Optional: handle cases where no title level is found


def contains_remote(descriptions):
    # Regular expression to check if the word 'remote' exists in any description (case-insensitive)
    pattern = r'\bremote\b'

    # Check each description for the word 'remote'
    for description in descriptions:
        if re.search(pattern, description, re.IGNORECASE):  # re.IGNORECASE makes it case-insensitive
            return True  # Return True if 'remote' is found in any description

    return False  # Return False if no description contains 'remote'


def check_job_type(descriptions):
    # Regular expression to check if 'full time' or 'part time' exists in any description (case-insensitive)
    pattern = r'\b(full\s?time|part\s?time)\b'

    # Check each description for 'part time'
    for description in descriptions:
        if re.search(r'\bpart\s?time\b', description, re.IGNORECASE):  # Looking specifically for 'part time'
            return "part time"  # Return 'part time' if found

    # If no 'part time' is found, return 'full time' by default
    return "full time"