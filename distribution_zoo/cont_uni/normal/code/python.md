#### PDF

```python
import numpy as np
from scipy.stats import norm

x = np.linspace(start={{{range_start}}}, stop={{{range_end}}}, num=50)

mean = {{{mean}}}
std = {{{std}}}
norm.pdf(x=x, loc=mean, scale=std)
```


#### Log PDF

```python
import numpy as np
from scipy.stats import norm

x = np.linspace(start={{{range_start}}}, stop={{{range_end}}}, num=50)

mean = {{{mean}}}
std = {{{std}}}
norm.logpdf(x=x, loc=mean, scale=std)
```


#### Random sample of size n

```python
from scipy.stats import norm

n = 50
mean = {{{mean}}}
std = {{{std}}}
norm.rvs(loc=mean, scale=std, size=n)
```
