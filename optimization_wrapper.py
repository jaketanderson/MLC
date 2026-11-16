"""
Plug `f` into scipy.optimize, your own optimizer, etc. It sleeps and retries
automatically if you hit the rate limit.
"""
import time
import urllib.error
import urllib.request

SERVER = "http://jaketanderson.com:8000"


def f(x, y):
    url = f"{SERVER}/?x={float(x)!r}&y={float(y)!r}"
    while True:
        try:
            with urllib.request.urlopen(url, timeout=15) as r:
                return float(r.read())
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise ValueError(e.read().decode()) from None
            time.sleep(float(e.headers.get("Retry-After", 2)))
