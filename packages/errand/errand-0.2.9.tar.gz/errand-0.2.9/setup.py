"errand setup module."

def main():

    from setuptools import setup, find_packages
    from errand.context import Errand as erd

    install_requires = ["numpy"]

    setup(
        name="errand",
        version="0.2.9",
        description="pythonic excellerator interface",
        long_description="pythonic excellerator interface",
        author="Youngsung Kim",
        author_email="youngsung.kim.act2@gmail.com",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Science/Research",
            "Topic :: Scientific/Engineering",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        keywords="errand",
        packages=find_packages(exclude=["tests"]),
        include_package_data=True,
        install_requires=install_requires,
        project_urls={
            "Bug Reports": "https://github.com/grnydawn/errand/issues",
            "Source": "https://github.com/grnydawn/errand",
        }
    )

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()
