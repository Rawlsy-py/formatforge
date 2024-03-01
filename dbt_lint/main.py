import typer

app = typer.Typer()


@app.callback()
def callback():
    """
    dbt-lint is a linter for dbt projects.
    """


@app.command()
def hello():
    """
    Say hello.
    """
    print("Hello")
