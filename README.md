run code
```bash
cp .env-sample .env
: fill in .env the value fit for you
source .env; python src/main.py
```

to have .env loaded automatically, use python-dotenv ref. https://pypi.org/project/python-dotenv/
```bash
pipenv sync
pipenv run python src/main.py
```
