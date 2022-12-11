from pytz import timezone

from datetime import datetime

# time_format = "%a-%d/%m/%y %H:%S"
# time_format = "%A %d %B %Y %H:%S"
time_format = "%a %x %H:%S"

now = datetime.now().strftime(time_format)

print(now)