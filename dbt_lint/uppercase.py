"""Module to convert SQL keywords to uppercase.

    Returns:
        _type_: _description_
        
"""

import re

# List of SQL keywords to convert to uppercase
sql_keywords = ["SELECT", "FROM", "WHERE"]

# Regular expression pattern to match SQL keywords
pattern = re.compile(r"\b(" + "|".join(sql_keywords) + r")\b", re.IGNORECASE)


def convert_keywords_to_uppercase(sql_text):
    """
    Converts SQL keywords to uppercase.
    """

    # Function to convert matched keywords to uppercase
    def convert_to_upper(match):
        return match.group().upper()

    # Use the regular expression to replace keywords with their uppercase form
    return pattern.sub(convert_to_upper, sql_text)
