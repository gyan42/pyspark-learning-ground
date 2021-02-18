PySpark Test Driven Development Setup

1. Sample data with matching schema as that of production data
2. Business logic as testable components
3. PySpark test modules 
   - https://pypi.org/project/pyspark-test/
   - https://pypi.org/project/pytest-spark/ 
    
`pytest -s --spark_home=$SPARK_HOME test/unit/dataquality/management/`

**Ensure that you have Python 3, xcode installed and that your PIP3 installation points to it**

To install the required modules:

```
$ make install
Or
pip3 install -r requirements.txt
```

To run the (failing) test:

```
$ make test
or
PYSPARK_PYTHON=python3 PYSPARK_DRIVER_PYTHON=python3 py.test
```

To uninstall the required modules:

```
$ make uninstall
or
pip3 uninstall -y -r requirements.txt
```

