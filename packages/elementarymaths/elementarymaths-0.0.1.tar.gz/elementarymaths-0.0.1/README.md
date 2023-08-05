# first_package

creating a simple program to make it available to everyone
* https://www.freecodecamp.org/news/build-your-first-python-package/

* run the following command in the same directory as first_package
** python setup.py sdist bdist_wheel
** create userid and password on https://pypi.org/manage/projects/
** pip install twine 
** twine upload dist/*