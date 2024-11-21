import datetime
import click
from objects import Router

@click.group()
def commandline():
    pass

@click.command()
@click.option("-c", "--count", default=1, show_default=True, help="How many lines should be printed")
@click.argument("input_string")
def print_input(count, input_string):
    for i in range(count):
        click.echo(f"{input_string} - {i}")

@click.command()
def establish_connection():
    click.echo("Let me establish connection to Network Device")

@click.command()
@click.option("-d", "--days", default=0, type=int, help="How many days to add to datetime.now")
def get_date(days):
    now = datetime.datetime.now()
    print(now + datetime.timedelta(days = days))

@click.command()
@click.argument("router_name")
@click.argument("router_ip")
@click.option("-v", "--version", is_flag=True, help="When provided, Router's version will be displayed")
def create_router(router_name, router_ip, version):
    router = Router(router_name, router_ip)
    print(router)
    if version:
        print(router.show_version())

def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()

@click.command()
@click.argument("router_name")
@click.argument("router_ip")
@click.argument("command")
@click.confirmation_option(prompt="Are you sure?")
def execute_command(router_name, router_ip, command):
    router = Router(router_name, router_ip)
    print(f"Executing command on: {router}...")
    print(f"Result of command: {command}")
    print(router.cmd(command))

commandline.add_command(print_input)
commandline.add_command(establish_connection)
commandline.add_command(get_date)
commandline.add_command(create_router)
commandline.add_command(execute_command)

if __name__ == "__main__":
    commandline()