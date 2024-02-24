# tests/test_uppercase.py
"""Test the uppercase module."""

import pytest
from dbt_lint.uppercase import (
    convert_keywords_to_uppercase,
)  # Adjust the import path as necessary


@pytest.mark.parametrize(
    "input_sql, expected_output",
    [
        ("select * from table where id = 1;", "SELECT * FROM table WHERE id = 1;"),
        ("SELECT already uppercase;", "SELECT already uppercase;"),
        ("Mixed CaSe SeLeCt;", "Mixed CaSe SELECT;"),
        ("select select from where where;", "SELECT SELECT FROM WHERE WHERE;"),
        ("no keywords here;", "no keywords here;"),
        (
            "select case(when 1 > myfield then 1 else null) from mytable where myfield like '%'",
            "SELECT CASE(WHEN 1 > myfield THEN 1 ELSE null) FROM mytable WHERE myfield LIKE '%'",
        ),
    ],
)
def test_convert_keywords_to_uppercase(input_sql, expected_output):
    """
    Test that SQL keywords are converted to uppercase.
    """
    result = convert_keywords_to_uppercase(input_sql)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
