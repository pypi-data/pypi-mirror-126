# modcall
Create callable modules

## Usage
**lib.py**
```python
import modcall

def hello(name: str) -> None:
    print(f'Hello, {name}!')

modcall(__name__, hello)
```

**app.py**
```python
import lib

lib('World')
```
