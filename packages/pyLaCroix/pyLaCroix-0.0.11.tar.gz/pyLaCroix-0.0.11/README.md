# ![pyLaCroixLogo](docs/images/pyLaCroix.logo.svg)

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pyLaCroix.svg)](https://pypi.python.org/pypi/pyLaCroix/)
[![PyPI version](https://badge.fury.io/py/pyLaCroix.svg)](https://badge.fury.io/py/pyLaCroix)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A python color palette for those that love sparkled beverages.

```
pip install pyLaCroix
```

### Interface

```python
# example use-case
from pyLaCroix import pyLaCroix

palette = pyLaCroix(n_points=5)
palette.apricot
```

* Create a gradient with a flexible number of colors with any choice of beverage via the [colour](https://github.com/colour-science/colour) package (the only dependency). 

### Notes
---
* Inspired by the [R implementation](https://github.com/johannesbjork/LaCroixColoR).
* Color choices a la [LaCroix Flavors](https://www.lacroixwater.com/flavors/)
