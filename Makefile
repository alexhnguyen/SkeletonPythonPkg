install:
	python -m pip install setuptools wheel
	pip install -r requirements.txt

package:
	python setup.py sdist bdist_wheel

make pytest:
	python -m pytest

# publish:
# 	twine upload --verbise --repository 
