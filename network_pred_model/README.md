# this project tries to work on MLOPs packaging and generating a prediction
# model for network congestion. The data generated for the network congestion scenarios is
# hypothetical and for testing the MLOPs package modeling



## Virtual Environment
Install virtualenv

```python
python3 -m pip install virtualenv
```

Check version
```python
virtualenv --version
```

Create virtual environment

```python
virtualenv ml_package
```

Activate virtual environment

For Linux/Mac
```python
source ml_package/bin/activate
```
For Windows
```python
ml_package\Scripts\activate

Deactivate virtual environment

```python
deactivate
```

# Build the Package

1. Goto Project directory and install dependencies
`pip install -r requirements.txt`

2. Create Pickle file after training:
`python pred_model/training_pipeline.py`

3. Create source distribution and wheel
`python setup.py sdist bdist_wheel`

# Installation of Package

Go to project directory where `setup.py` file is located

1. To install it in editable or developer mode
```python
pip install -e .
```
```.``` refers to current directory

```-e``` refers to --editable mode

2. Normal installation
```python
pip install .
```
```.``` refers to current directory

3. Also can be installed from git as well after pushing to github

```
pip install git+https://github.com/prpa4901/network-congestion-mlops.git
```

# Testing the Package Working

1. Goto a separate location which is outside of package directory
2. Create a new virual environment using the commands mentioned above & activate it
3. Before installing, test whether you are able to import the package of `pred_model` - (you should not be able to do it)
4. Now in the new environment install the package from github
`pip install git+https://github.com/prpa4901/network-congestion-mlops.git`
5. Now try importing the prediction_model, you should be able to do it successfully
6. Extras : Run training pipeline using the package, and also conduct the test


