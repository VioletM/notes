## Multiprocessing of MAC M1 with python

```
cannot pickle '_thread.lock' object
```
could be solved with:
```
from multiprocessing import set_start_method
set_start_method("fork")
```
