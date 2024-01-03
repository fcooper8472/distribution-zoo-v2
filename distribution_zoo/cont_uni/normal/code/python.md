#### PDF

```python
import numpy as np
from scipy.stats import norm

x = np.linspace(start={{{range_start}}}, stop={{{range_end}}}, num=50)

mean = {{{mean}}}
std = {{{std}}}
y = norm.pdf(x=x, loc=mean, scale=std)

for x_i, y_i in zip(x, y):
    print(f'{x_i},{y_i}')
```


#### Log PDF

```python
import numpy as np
from scipy.stats import norm

x = np.linspace(start={{{range_start}}}, stop={{{range_end}}}, num=50)

mean = {{{mean}}}
std = {{{std}}}
y = norm.logpdf(x=x, loc=mean, scale=std)

for x_i, y_i in zip(x, y):
    print(f'{x_i},{y_i}')
```


#### Random sample of size n

```python
from scipy.stats import norm

n = 100
mean = {{{mean}}}
std = {{{std}}}
rvs = norm.rvs(loc=mean, scale=std, size=n)

for rv in rvs:
    print(rv)
```
