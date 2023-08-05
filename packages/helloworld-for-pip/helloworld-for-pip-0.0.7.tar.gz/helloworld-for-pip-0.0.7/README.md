# helloworld-for-pip

Example package uploaded to PyPI: https://pypi.org/project/helloworld-for-pip/


### How to upload the package to PyPI by `twine`
```bash
cd helloworld-for-pip
rm -r dist
python setup.py sdist bdist_wheel
twine upload dist/*
```
In order to upload a new version of the package, you must edit `VERSION` in the file `setup.py`.


### How to download the package from PyPI and install it by `pip`
```bash
pip install helloworld-for-pip
```
In order to upgrade the package to the latest version (if already installed), add the option `--upgrade`.


### How to use the package
```python
from helloworld.hello import print_hello

print_hello()
```
