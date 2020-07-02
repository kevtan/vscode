import datetime
from unittest import mock

# create a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

# after creating test days, mock the datetime module
datetime = mock.Mock()


def is_weekday() -> bool:
    today = datetime.datetime.today()
    return 0 <= today.weekday() < 5


datetime.datetime.today.return_value = tuesday
assert is_weekday()
datetime.datetime.today.return_value = saturday
assert not is_weekday()
