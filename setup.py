from setuptools import setup, find_packages

setup(
    name="comp0034-cw2-g-team-22-1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
        "flask-wtf",
        "flask-sqlalchemy",
        "Flask-WTF",
        "flask-marshmallow",
        "marshmallow-sqlalchemy",
        "pandas",
        "requests",
        "scikit-learn",
    ],
)
