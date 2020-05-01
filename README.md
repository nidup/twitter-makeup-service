# Twitter Make Up Service

Twitter Make Up Service 🚀

## Build container and start them




## Publish the library

[Publish your library](https://medium.com/@thucnc/how-to-publish-your-own-python-package-to-pypi-4318868210f9)

Generate distribution archives

Make sure you have the latest versions of setuptools and wheel installed:
```
python3.6 -m pip install --user --upgrade setuptools wheel
```

Now run this command from the same directory where setup.py is located:
```
python3.6 setup.py sdist bdist_wheel
```

Uploading the distribution archives. To do this, you can use twine. First, install it using pip:
```
python3.6 -m pip install --user --upgrade twine
```

Then upload all the archives to PyPi:
```
python3.6 -m twine upload dist/*
```

Enter your PyPi username and password.

