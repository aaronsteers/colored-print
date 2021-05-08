Colored Print
-----------------------
[![PyPI](https://img.shields.io/pypi/v/mix-mavis)](https://pypi.org/project/colored-print/)
[![Python Versions](https://img.shields.io/pypi/pyversions/wfuzz)](https://pypi.org/project/colored-print/)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/etingof/pysnmp/master/LICENSE.rst)

A lightweight python library in order to print in different colors and save them into a file optionally.


## Setup

```bash
pip install colored-print 
```

## Usage

```python
from colored_print.colored-print import ColoredPrint


log = ColoredPrint()

log.success("Hello", 123, "Bye").store()
log.info("Hello", 123, "Bye")
log.warn("Hello", 123, "Bye")
log.err("Hello", 123, "Bye").store()
log.pink("Hello", 123, "Bye")

```
