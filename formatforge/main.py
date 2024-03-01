import typer
from formatforge.uppercase import convert_keywords_to_uppercase

app = typer.Typer()


@app.callback()
def callback():
    """
    formatforge is a linter for dbt projects.
    """


@app.command()
def hello():
    """
    Say hello.
    """
    print("Hello")


@app.command()
def uppercase(sql_file: str):
    """
    Lints a SQL file to ensure all keywords are uppercase.
    """
    convert_keywords_to_uppercase(sql_file)
    return f"Converted {sql_file} to uppercase."
