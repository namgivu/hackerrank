"""
**goal**
demo reading .env via os.environ dict

**run it**
               python src/main.py  # no .env var be loaded
SOME_VAR1=1222 python src/main.py  # only SOME_VAR1 available
source .env;   python src/main.py  # all vars defined in .env available
pipenv run     python src/main.py  # pipenv run will load .env automatically
"""

from dotenv import load_dotenv; load_dotenv() # Load .env automatically for this code - this may be done already if run by pipenv run

import os
env_key='SOME_VAR1';    v=os.environ.get(env_key);      print(v)
env_key='SOME_VAR22';   v=os.environ.get(env_key);      print(v)
