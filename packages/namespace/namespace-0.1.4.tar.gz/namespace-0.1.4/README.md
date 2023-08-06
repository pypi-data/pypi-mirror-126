# namespace
Simple namespaces

## Usage
```python
>>> import namespace
>>>
>>> functions = namespace()
>>>
>>> @functions
>>> def foo(): pass
>>>
>>> functions
Namespace(foo=<function foo at 0x7fd5d249d1f0>)
>>>
>>> functions.foo
<function foo at 0x7fd5d249d1f0>
```
