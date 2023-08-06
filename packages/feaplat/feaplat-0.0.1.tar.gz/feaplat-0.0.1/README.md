# pydict

Same as json.dumps or json.loads, pydict supprot pydict.dumps and pydict.loads

Example:

```python
>>> import pydict
>>> pydict.dumps({"a": True, "b": False, "c": [1, 2, 3]})
{
    "a": True,
    "b": False,
    "c": [
        1,
        2,
        3
    ]
}

>>> pydict.loads('{"a": True, "b": False, "c": [1, 2, 3]}')
{'a': True, 'b': False, 'c': [1, 2, 3]}
```