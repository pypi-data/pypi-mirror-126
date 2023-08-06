Usage

```python
from scrapers.mollerAuto import parse_moller_auto

if __name__ == '__main__':
    print(*flow(
        parse_moller_auto(),
        unwrap_or_failure,
    ), sep="\n")
```
