# modules-name-from-code

Get modules name from your python code

## How to install?

PYPI : https://pypi.org/project/modules-name-from-code/1.0.0/

```
pip install modules-name-from-code
```

## Example

/home/mycode.py :
```python
import module1
import module2, module3
from module4 import module 

...
```

```python
import getmodules

print(getmodules.get_modules("/home/mycode.py"))
```
Result :
```python
['module2', 'module1', 'module4', 'module3']
```
Or
```python
import getmodules

print(getmodules.get_modules("/home/mycode.py", sort=True))
```
Result :
```python
['module1', 'module2', 'module3', 'module4']
```