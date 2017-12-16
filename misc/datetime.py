#!/usr/bin/env python3

#datetime from string  ref. https://stackoverflow.com/a/466376/248616
from datetime import datetime
d = datetime.strptime('2017-12', '%Y-%m')
print(d)
