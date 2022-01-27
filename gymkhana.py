import argparse, os
from argparse import FileType
from helper.createapp import create_app

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
group.add_argument(
    "-a",
    "--app",
    type=str,
    nargs=1,
    help="create app of given name"
)
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
    type=str,
    nargs=1,
    help="reset database",
)
group.add_argument(
    "-s",
    "--start",
    help="start server",
    action="store_true",
)
args = parser.parse_args()

if args.freeze:
    os.system(f"pip freeze --exclude-editable > {args.freeze[0].name}")

if args.app:
    create_app(args.app[0])

if args.migrate:
    os.system(f'alembic revision --autogenerate -m "{args.migrate[0]}"')
    os.system("alembic upgrade heads")

if args.reset:
    os.system("alembic downgrade base")
    os.system("alembic upgrade heads")

if args.start:
    os.system("uvicorn main:app --reload")