import typer
from formatforge.uppercase import convert_keywords_to_uppercase
import pkg_resources

version = pkg_resources.get_distribution("formatforge").version

app = typer.Typer()


@app.callback()
def callback():
    """
    formatforge is a linter for dbt projects.
    """


@app.command()
def version(
    version: str = typer.Option(
        version, "--version", "-v", help="The version of the program."
    )
):
    """
    Display formatforge's current version.
    """
    print(f"The current version of formatforge is {version}.")


@app.command()
def uppercase(sql_file: str):
    """
    Formats a SQL file to ensure all keywords are uppercase.
    """
    convert_keywords_to_uppercase(sql_file)
    return f"Converted {sql_file} to uppercase."
