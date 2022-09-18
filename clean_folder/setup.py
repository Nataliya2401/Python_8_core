from setuptools import setup, find_namespace_packages


setup(
    name='sort.py',
    version='1',
    description='Sortinf files, return exts',
    url='https://github.com/Nataliya2401/Python_8_core/blob/main/sort.py',
    author='Nataliya Feshchenko',
    author_email='sabotab2000@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': [
        'clean-folder= clean_folder.sort:main']}
)
