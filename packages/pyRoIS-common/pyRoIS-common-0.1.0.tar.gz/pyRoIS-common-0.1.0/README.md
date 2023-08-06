# pyrois-common

This software is an implementation of HRI Engine on RoIS framework.
This software is released under the MIT License, see LICENSE.

## Overview

pyrois-common is an implementation of HRI Engine on RoIS framework with python3.
pyrois-common underlies pyrois, which is an implementation of RoIS framework.

## References

1. RoIS Framework
1. pyrois


## Unit test

### venv and pip install

generate a virtual environment and install pyrois

```
python3 -m venv env
source env/bin/activate
(env) pip install pyrois==0.0.6
```

### run unit tests

run all unit tests

```
(env) python3 -m unittest discover tests -p "unittest*.py"
```

run each unit test

```
(env) python3 -m unittest tests.unittest_execute_branch
```

```
(env) python3 -m unittest tests.unittest_execute_branch_error
```

```
(env) python3 -m unittest tests.unittest_execute_multi_commands
```

```
(env) python3 -m unittest tests.unittest_execute_multi_components
```
