from setuptools import setup, find_packages
from server.config import settings

setup(
    name="gymkhana_server",
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    author=settings.NAME,
    author_email=settings.EMAIL,
    url=settings.FRONTEND_URL,
    license=settings.LICENSE_NAME,
    packages=find_packages(),
)
