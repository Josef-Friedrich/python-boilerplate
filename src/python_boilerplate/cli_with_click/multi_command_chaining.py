import click

# https://click.palletsprojects.com/en/stable/commands/#command-chaining


@click.group(chain=True)
def cli() -> None:
    pass


@cli.command("sdist")
def sdist() -> None:
    click.echo("sdist called")


@cli.command("bdist_wheel")
def bdist_wheel() -> None:
    click.echo("bdist_wheel called")
