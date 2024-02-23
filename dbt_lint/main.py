"""Main module for the dbt-lint CLI."""

import typer
from uppercase import convert_keywords_to_uppercase

app = typer.Typer()


@app.command()
def format_sql(
    file_path: str = typer.Argument(
        ..., help="The path to the SQL file to be formatted"
    ),
    uppercase: bool = typer.Option(True, help="Convert SQL keywords to uppercase"),
    leading_comma: bool = typer.Option(True, help="Use leading commas in SQL lists"),
):
    """
    Formats a given SQL file according to specified style guidelines.
    """
    try:
        with open(file_path, "r") as file:
            sql_content = file.read()

        formatted_content = sql_content

        if uppercase:
            # Convert SQL keywords to uppercase using the function from uppercase.py
            formatted_content = convert_keywords_to_uppercase(formatted_content)

        if leading_comma:
            # Placeholder for leading comma logic
            pass

        # Write the formatted content back to the file
        with open(file_path, "w") as file:
            file.write(formatted_content)

        typer.echo(
            f"Formatted file {file_path} with uppercase={uppercase} and leading_comma={leading_comma}"
        )

    except FileNotFoundError:
        typer.echo(f"File not found: '{file_path}'", err=True)
    except Exception as e:
        typer.echo(f"An error occurred: {e}", err=True)


if __name__ == "__main__":
    app()
