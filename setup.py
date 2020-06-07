from setuptools import setup

with open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="eth2fastspec",
    description="Optimized version of eth2spec",
    version="0.0.1",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="protolambda",
    author_email="proto+pip@protolambda.com",
    url="https://github.com/protolambda/eth2fastspec",
    python_requires=">=3.8, <4",
    license="MIT",
    packages=[],
    py_modules=["eth2fastspec"],
    tests_require=[],
    install_requires=[
        "eth2spec>=0.11.3,<0.12",
        "remerkleable==0.1.16",
        "milagro_bls_binding==1.0.2",  # Old milagro bindings, to use spec 0.11 BLS
    ],
    include_package_data=False,
    keywords=["eth2", "pyspec", "eth2spec"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
)
