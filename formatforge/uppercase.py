"""Convert all SQL keywords to uppercase."""

import re

# List of SQL keywords to convert to uppercase
sql_keywords = [
    "ADD",
    "ADD CONSTRAINT",
    "ALL",
    "ALTER",
    "ALTER COLUMN",
    "ALTER TABLE",
    "AND",
    "ANY",
    "AS",
    "ASC",
    "BACKUP DATABASE",
    "BETWEEN",
    "CASE",
    "CHECK",
    "COLUMN",
    "CONSTRAINT",
    "CREATE",
    "CREATE DATABASE",
    "CREATE INDEX",
    "CREATE OR REPLACE VIEW",
    "CREATE TABLE",
    "CREATE PROCEDURE",
    "CREATE UNIQUE INDEX",
    "CREATE VIEW",
    "DATABASE",
    "DEFAULT",
    "DELETE",
    "DESC",
    "DISTINCT",
    "DROP",
    "DROP COLUMN",
    "DROP CONSTRAINT",
    "DROP DATABASE",
    "DROP DEFAULT",
    "DROP INDEX",
    "DROP TABLE",
    "DROP VIEW",
    "EXEC",
    "EXISTS",
    "FOREIGN KEY",
    "FROM",
    "FULL OUTER JOIN",
    "GROUP BY",
    "HAVING",
    "IN",
    "INDEX",
    "INNER JOIN",
    "INSERT INTO",
    "INSERT INTO SELECT",
    "IS NULL",
    "IS NOT NULL",
    "JOIN",
    "LEFT JOIN",
    "LIKE",
    "LIMIT",
    "NOT",
    "NOT NULL",
    "OR",
    "ORDER BY",
    "OUTER JOIN",
    "PRIMARY KEY",
    "PROCEDURE",
    "RIGHT JOIN",
    "ROWNUM",
    "SELECT",
    "SELECT DISTINCT",
    "SELECT INTO",
    "SELECT TOP",
    "SET",
    "TABLE",
    "TOP",
    "TRUNCATE TABLE",
    "UNION",
    "UNION ALL",
    "UNIQUE",
    "UPDATE",
    "VALUES",
    "VIEW",
    "WHERE",
]


# Regular expression pattern to match SQL keywords
pattern = re.compile(r"\b(" + "|".join(sql_keywords) + r")\b", re.IGNORECASE)


def convert_keywords_to_uppercase(sql_text):
    """Convert all SQL keywords to uppercase.

    Args:
        sql_text (file): A file containing SQL code.

    Returns:
        file: Updated file with all SQL keywords converted to uppercase.
    """

    # Function to convert matched keywords to uppercase
    def convert_to_upper(match):
        return match.group().upper()

    # Use the regular expression to replace keywords with their uppercase form
    return pattern.sub(convert_to_upper, sql_text)
