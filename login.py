"""Run this once to pick the name that shows up on the leaderboard.

    python login.py                 # asks for a name
    python login.py "Ada L."        # or pass it directly

Your name is tied to your IP address, so run it from the same network you'll
be submitting from. Run it again to change your name. Needs only the standard library.
"""
import sys
import urllib.error
import urllib.parse
import urllib.request

from optimization_wrapper import SERVER


def login(name):
    url = f"{SERVER}/login?name={urllib.parse.quote(name)}"
    try:
        with urllib.request.urlopen(url, timeout=15) as r:
            return True, r.read().decode().strip()
    except urllib.error.HTTPError as e:
        return False, e.read().decode().strip()
    except urllib.error.URLError as e:
        return False, f"Could not reach the server at {SERVER} ({e.reason})."


if __name__ == "__main__":
    name = " ".join(sys.argv[1:]) or input("Choose a name for the leaderboard: ")
    ok, msg = login(name)
    print(msg)
    sys.exit(0 if ok else 1)
