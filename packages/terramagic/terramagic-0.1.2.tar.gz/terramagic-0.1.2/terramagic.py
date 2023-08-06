import click
import os
from pyfiglet import figlet_format
from colorama import init
from termcolor import cprint


files = [
    "main.tf",
    "variables.tf",
    "outputs.tf",
    "backend.tf",
    "main.tfvars",
    ".gitignore",
]

modules_folder = [
    "vpc",
    "cluster", 
    "instance"
]

modules_files = [
    "main.tf",
    "variables.tf",
    "outputs.tf",
]

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo("Version: 0.1.2")
    ctx.exit()

def modules():
    os.mkdir("modules")
    os.chdir("modules")
    for folder in modules_folder:
        os.mkdir(folder)
        os.chdir(folder)
        for file in modules_files:
            handler = open(file, "w+")
            handler.close()
        os.chdir("..")
    os.chdir("..")

@click.group()
@click.option("--version", "-v", is_flag=True, callback=print_version,expose_value=False,is_eager=True,help="Show version")
def main():
    pass

@main.command()
@click.option("--name", "-n", help="Name of the project")
@click.option("--env", "-e", help="Environment name(dev, test, prd)", multiple=True)
def create_project(name, env):
    try:
        os.mkdir(name)
        os.chdir(name)
        modules()
        if env:
            for e in env:
                os.mkdir(e)
                os.chdir(e)
                for file in files:
                    handler = open(file, "w+")
                    handler.close()
                os.chdir("..")
            click.secho(
                (f"Created project {name} successfully, You're ready move to ☁️ !!"),fg="green",)

        else:
            click.secho((f"Environment {env} not found"), fg="red")

    except FileExistsError:
        click.secho(("The directory already exists!"), bg="red")
        os.chdir("..")

main.add_command(create_project)

if __name__ == "__main__":
    main()
