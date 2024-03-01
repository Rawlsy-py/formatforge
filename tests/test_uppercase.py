import pytest
from dbt_lint.uppercase import convert_keywords_to_uppercase


def test_convert_keywords_to_uppercase():
    # Test case 1: SQL text with no keywords
    sql_text = "SELECT * FROM users"
    expected_output = "SELECT * FROM users"
    assert convert_keywords_to_uppercase(sql_text) == expected_output

    # Test case 2: SQL text with lowercase keywords
    sql_text = "select * from users where name = 'John'"
    expected_output = "SELECT * FROM users WHERE name = 'John'"
    assert convert_keywords_to_uppercase(sql_text) == expected_output

    # Test case 3: SQL text with mixed case keywords
    sql_text = "Select * FrOm users WhErE name = 'John'"
    expected_output = "SELECT * FROM users WHERE name = 'John'"
    assert convert_keywords_to_uppercase(sql_text) == expected_output

    # Test case 4: SQL text with keywords in comments
    sql_text = """
    -- This is a comment with a select keyword
    SELECT * FROM users
    """
    expected_output = """
    -- This is a comment with a SELECT keyword
    SELECT * FROM users
    """
    assert convert_keywords_to_uppercase(sql_text) == expected_output

    # Test case 5: SQL text with keywords as part of column names
    sql_text = "SELECT id, name FROM users WHERE created_at > '2022-01-01'"
    expected_output = "SELECT id, name FROM users WHERE created_at > '2022-01-01'"
    assert convert_keywords_to_uppercase(sql_text) == expected_output

    # Test case 6: SQL text with keywords as part of table names
    sql_text = "SELECT * FROM select_table WHERE name = 'John'"
    expected_output = "SELECT * FROM select_table WHERE name = 'John'"
    assert convert_keywords_to_uppercase(sql_text) == expected_output

    # Test case 7: SQL text with keywords as part of column aliases
    sql_text = "SELECT id AS select_id, name AS select_name FROM users"
    expected_output = "SELECT id AS select_id, name AS select_name FROM users"
    assert convert_keywords_to_uppercase(sql_text) == expected_output

    # Test case 8: SQL text with keywords as part of string literals
    # sql_text = "SELECT * FROM users WHERE name = 'select'"
    # expected_output = "SELECT * FROM users WHERE name = 'select'"
    # assert convert_keywords_to_uppercase(sql_text) == expected_output

    # Test case 9: SQL text with keywords as part of table aliases
    sql_text = "SELECT u.id, u.name FROM users AS select_table"
    expected_output = "SELECT u.id, u.name FROM users AS select_table"
    assert convert_keywords_to_uppercase(sql_text) == expected_output

    # Test case 10: SQL text with keywords as part of function names
    sql_text = "SELECT COUNT(*) FROM users"
    expected_output = "SELECT COUNT(*) FROM users"
    assert convert_keywords_to_uppercase(sql_text) == expected_output

    # Test case 11: SQL text with keywords as part of function arguments
    sql_text = "SELECT CONCAT('SELECT', ' * ', 'FROM') FROM users"
    expected_output = "SELECT CONCAT('SELECT', ' * ', 'FROM') FROM users"
    assert convert_keywords_to_uppercase(sql_text) == expected_output
