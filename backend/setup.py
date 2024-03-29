from setuptools import setup, find_packages

setup(
    name='backend',
    version='0.1',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        "fastapi~=0.90.0",
        "uvicorn",
        "redis",
        "psycopg2-binary",
        "sqlalchemy~=1.4.35",
        "requests",
        "multipledispatch",
        "sqlmodel~=0.0.8",
        "pyjwt~=2.6.0",
        "python-multipart",
        "python-dotenv~=0.21.1",
        "pip~=22.0.4",
        "wheel~=0.37.1",
        "setuptools~=65.5.0",
        "packaging~=21.3",
        "pyparsing~=3.0.8",
        "starlette~=0.23.0",
        "pydantic~=1.10.4"
    ],
    authors='Akrom Amirov',
    license='MIT',
)
