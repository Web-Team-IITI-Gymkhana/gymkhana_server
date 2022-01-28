import argparse, os
from argparse import FileType
from helper.create_app import create_app
from helper.create_env import create_env
from helper.activate_venv import activate_venv

parser = argparse.ArgumentParser(
    prog="gymkhana",
    usage="%(prog)s [options] ...",
    description="CLI for helping contributors",
    epilog="Refer CONTRIBUTING.md for more!",
)
group = parser.add_mutually_exclusive_group()

group.add_argument(
    "-f",
    "--freeze",
    type=FileType("w"),
    nargs=1,
    help="freeze pip packages into given file",
)
group.add_argument(
    "-v",
    "--version",
    action="version",
    help="print version",
    version="%(prog)s 1.0.0",
)
group.add_argument("-a", "--app", type=str, nargs=1, help="create app of given name")
group.add_argument(
    "-m",
    "--migrate",
    type=str,
    nargs=1,
    help="migrate database",
)
group.add_argument(
    "-r",
    "--reset",
    action="store_true",
    help="reset database",
)
group.add_argument(
    "-s",
    "--start",
    action="store_true",
    help="start server",
)
group.add_argument(
    "-i",
    "--install",
    action="store_true",
    help="install required packages",
)
args = parser.parse_args()

if args.freeze:
    os.system(f"pip freeze --exclude-editable > {args.freeze[0].name}")
    print(f"Installed Packages written into {args.freeze[0].name}")

if args.app:
    create_app(args.app[0])
    print(f"{args.app[0]} folder created!")

if args.migrate:
    os.system(f'alembic revision --autogenerate -m "{args.migrate[0]}"')
    os.system("alembic upgrade heads")
    print("Database Schema updated")

if args.reset:
    os.system("alembic downgrade base")
    os.system("alembic upgrade heads")
    print("Database has been reset")

if args.start:
    print("Starting server...")
    os.system("uvicorn main:app --reload")

if args.install:
    create_env()
    os.system("pip install virtualenv")
    os.system("virtualenv venv")
    activate_venv()
    if os.name == "posix":
        os.system("pip install -r requirements.txt")
    else:
        os.system("pip install -r windows_requirements.txt")
    
    print("Fill credentials in .env file")
    print("Don't forget to activate venv before working!")
