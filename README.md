# callable-enum
Callable Enum for Python

## installation

```bash
pip install git+git://github.com/ukyo-su/callable-enum@master
```

## CallableEnum & member & member_with_value(value)

```python
from callable_enum import CallableEnum, member, member_with_value

class Operator(CallableEnum):
    @member
    def ADD(self, x, y):
        return x + y
    
    @member
    def SUB(self, x, y):
        return x - y


Operator.ADD(1, 2)
# 3
Operator.SUB(2, 1)
# 1

# you can set values of CallableEnum's

class AddSubValue(CallableEnum):
    @member_with_value(1)
    def ADD1(self, x):
        return x + self.value

    @member_with_value(2)
    def SUB2(self, x):
        return x - self.value

AddSubValue.ADD1(2)
# 3
AddSubValue.SUB2(3)
# 1
```

