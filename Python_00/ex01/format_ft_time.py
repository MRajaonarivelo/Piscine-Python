import time
import datetime as dt

seconds = time.time()
date = dt.datetime.fromtimestamp(seconds)

print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")
print(dt.datetime.strftime(date, "%b %d %Y"))