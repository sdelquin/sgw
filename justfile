dev:
    pip install -e .
build:
    python setup.py bdist
upload-test: build
    twine upload --repository testpypi dist/*
upload: build
    twine upload dist/*
