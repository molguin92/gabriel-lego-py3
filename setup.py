import setuptools

with open('./requirements.txt', 'r') as f:
    reqs = [line.strip() for line in f]

setuptools.setup(
    name="gabriel_lego",
    version="0.2.0",
    author="Manuel Olguin Munoz",
    author_email="molguin@kth.se",
    description="Gabriel LEGO Assembly cognitive engine.",
    long_description_content_type="text/markdown",
    url="https://github.com/molguin92/gabriel-lego-py3",
    packages=setuptools.find_packages(exclude=['gabriel-server*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.7',
    install_requires=reqs,
)
