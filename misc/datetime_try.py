#!/usr/bin/env python3
from datetime import datetime
from dateutil.relativedelta import relativedelta

#simple datetime calculator
d = datetime.strptime('2017-01-04', '%Y-%m-%d')
d = d + relativedelta(months=2, days=27)
print(d)

#datetime from string  ref. https://stackoverflow.com/a/466376/248616
d = datetime.strptime('2017-12', '%Y-%m')
print(d)

#add/minus month(s) to datetime
d2 = d - relativedelta(months=3)
print(d2)

#diff. in month(s)
d3 = datetime.today()
d4 = d3 - relativedelta(months=6)
diff = relativedelta(d3, d4)
print(diff)
print(diff.months)
