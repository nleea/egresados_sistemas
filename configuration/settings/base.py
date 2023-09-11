import environ
import os
from pathlib import Path

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR.parent, ".env"), overwrite=True)

try:

    if env.bool("DEBUG"):
        from configuration.settings.dev import *
    else:
        from configuration.settings.prod import *
except Exception as e:
    print(e.args)
