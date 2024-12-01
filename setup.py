from setuptools import setup, find_packages

setup(
    name="kannada_lang",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "kannada=kannada.interpreter:execute_kannada_code",
        ]
    },
    description="A Kannada-based programming language interpreter",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourname/kannada_lang",
)
