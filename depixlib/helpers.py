import os
import argparse

from typing import cast
from typing import Optional

def check_file(s: str) -> str:
    if os.path.isfile(s):
        return s
    else:
        raise argparse.ArgumentTypeError("%s is not a file." % repr(s))


#def check_color(s: str | None) -> tuple[int, int, int] | None:
def check_color(s: Optional[str]) -> Optional[tuple[int, int, int]]:
    if s is None:
        return None
    ss = s.split(",")
    if len(ss) != 3:
        raise argparse.ArgumentTypeError("Given colors must be formatted as 'r,g,b'.")
    else:
        try:
            return cast(tuple[int, int, int], tuple([int(i) for i in ss]))
        except ValueError:
            raise argparse.ArgumentTypeError(
                "Maybe %s is not '<int>,<int>,<int>'." % repr(s)
            )

