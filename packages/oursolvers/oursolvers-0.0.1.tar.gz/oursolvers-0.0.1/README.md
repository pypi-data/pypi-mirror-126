# Solver Wrappers
This is a simple lib to wrap different solvers. 

```python

import numpy as np
import solvers.ilp as ilp

status, solution = ilp.solve_boolean_lp(
        obj=np.array([1,2,3]),
        aub=np.array([
            [-1,1,0],
            [0,0,1],
        ]),
        bub=np.array([0,1]),
        minimize=True,
    )

assert status == 'optimal'
assert solution.tolist() == [0,0,1]

```
Status is either 'optimal', 'feasible' or 'undefined', where
'optimal' or 'feasible' yields a numpy vector as solution.
