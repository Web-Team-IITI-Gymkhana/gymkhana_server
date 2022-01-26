import os, sys

directory = sys.argv[1]
path = os.path.join(os.getcwd(), directory)
os.mkdir(path)

with open(os.path.join(path, "__init__.py"), "w") as f:
    pass

with open(os.path.join(path, "models.py"), "w") as f:
    f.write("from server.connection import Base\n")
    f.write("# Add the above Base to migrations/env.py\n\n")

with open(os.path.join(path, "schemas.py"), "w") as f:
    f.write("from pydantic import BaseModel\n\n")

with open(os.path.join(path, "router.py"), "w") as f:
    f.write("# Add this router to main.py\n\n")

with open(os.path.join(path, "tests.py"), "w") as f:
    pass

print(directory, "App created!")

# This file can be deleted after the project is completed.