#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames should only begin with letters
    if not re.match('^[a-zA-Z].*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    return True



