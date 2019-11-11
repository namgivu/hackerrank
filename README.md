run code
```bash
cp .env-sample .env
: fill in .env the value fit for you
source .env; python main.py
```

to have .env loaded automatically, use python-dotenv ref. https://pypi.org/project/python-dotenv/
```bash
pipenv sync
pipenv run python main.py
```
