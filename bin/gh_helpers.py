import os
from pathlib import Path
from typing import Optional

from github import Github


def gh_token(token_path: Optional[os.PathLike] = None):
    try:
        with open(token_path or Path(__file__).parent.parent / 'github.token') as fh:
            token = fh.read().strip()
    except (IOError, ValueError):
        raise RuntimeError('No github token found or provided.  '
                           'Please make one with repo access')
    
    return token
