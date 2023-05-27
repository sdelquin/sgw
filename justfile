dev:
    pip install -e .
build: clean
    python setup.py bdist
upload-test: build
    twine upload --repository testpypi dist/*
upload: build
    twine upload dist/*
clean:
    rm -fr build dist *egg* *cache*
