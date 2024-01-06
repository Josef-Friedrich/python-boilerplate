import click

# https://click.palletsprojects.com/en/8.1.x/commands/#multi-command-chaining


@click.group(chain=True)
def cli():
    pass


@cli.command("sdist")
def sdist():
    click.echo("sdist called")


@cli.command("bdist_wheel")
def bdist_wheel():
    click.echo("bdist_wheel called")
