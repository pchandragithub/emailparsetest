# parse_email.py

import re

def parse_email(file_path):
    with open(file_path, 'r') as file:
        email_content = file.read()

    # Extract values using regular expressions
    param1_match = re.search(r'Param1: (.+)', email_content)
    param2_match = re.search(r'Param2: (.+)', email_content)

    if param1_match and param2_match:
        param1 = param1_match.group(1)
        param2 = param2_match.group(1)
        return param1, param2
    else:
        return None, None

if __name__ == "__main__":
    param1, param2 = parse_email('email.txt')
    print(f"Param1: {param1}")
    print(f"Param2: {param2}")
