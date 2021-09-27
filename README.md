# Binarized Method
Binarized image segmentation method

- To use this code, go to your terminal and paste:

```console
git clone clone https://github.com/dsandovalc/Binarized-Method.git
```
- Now, paste:

```console
pip install -r requirements.txt
```

- Find where /pyhton3.9/site-packages/goto.py is installed and change line 53 to:

```python
    return code.replace(co_code=codestring)
```

- Also change line 175 in goto.py to:

```python
    return _make_code(code, buf.tobytes())
```

- Now you are able to use this code using:

```console
$ python3 matrix_operations.py
```
