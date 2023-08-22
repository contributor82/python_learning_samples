"""Module for Date time """
from datetime import date, datetime, timezone
import time

class DateTimeClass:
    """Date time class """
    current_date : date

    def __init__(self) -> None:
        """Initialize class members """
        self.current_date = date.today()

    def current_date_dtls(self) -> None:
        """Getting current date details method """
        print('Current Date: ', self.current_date)
        print('Current Day: ', self.current_date.day)
        print('Current Day: ', self.current_date.month)
        print('Current Day: ', self.current_date.year)

    def current_time_dtls(self) -> None:
        """Getting current time details method """

        date_time = datetime(self.current_date.year,
                             self.current_date.month,
                             self.current_date.day,
                             self.current_date.timetuple().tm_hour,
                             tzinfo=timezone.utc)
        print('Current time: ', time.strftime('%H:%M:%S %p'))
        print('Time by Zone UTC: ', date_time.now(timezone.utc).time())

    def date_time_data_concatenation(self) -> None:
        """Date time data concatenaton method """
        current_time: str = time.strftime('%H:%M:%S %p')

        logging_strings: list[str] = ['DateTime file executed at ',
                                      str(self.current_date) ,
                                      current_time ]

        # Created an empty array
        process_strings: list[str] = ['']

        # Running a loop to append list with specifier
        for log_str in logging_strings:
            process_strings.append(log_str)
            process_strings.append(' ')

        # Using join to concatenate at one go to generate final string.
        logging_msg: str = ''.join(process_strings)

        print(logging_msg)

if __name__ == '__main__':
    dt_instance = DateTimeClass()
    dt_instance.current_date_dtls()
    dt_instance.current_time_dtls()
    dt_instance.date_time_data_concatenation()

# ZERO = timedelta(0)
# HOUR = timedelta(hours=1)
# SECOND = timedelta(seconds=1)

# # A class capturing the platform's idea of local time.
# # (May result in wrong values on historical times in
# #  timezones where UTC offset and/or the DST rules had
# #  changed in the past.)
# import time as _time

# STDOFFSET = timedelta(seconds = -_time.timezone)
# if _time.daylight:
#     DSTOFFSET = timedelta(seconds = -_time.altzone)
# else:
#     DSTOFFSET = STDOFFSET

# DSTDIFF = DSTOFFSET - STDOFFSET

# class LocalTimezone(tzinfo):

#     def fromutc(self, dt):
#         assert dt.tzinfo is self
#         stamp = (dt - datetime(1970, 1, 1, tzinfo=self)) // SECOND
#         args = _time.localtime(stamp)[:6]
#         dst_diff = DSTDIFF // SECOND
#         # Detect fold
#         fold = (args == _time.localtime(stamp - dst_diff))
#         return datetime(*args, microsecond=dt.microsecond,
#                         tzinfo=self, fold=fold)

#     def utcoffset(self, dt):
#         if self._isdst(dt):
#             return DSTOFFSET
#         else:
#             return STDOFFSET

#     def dst(self, dt):
#         if self._isdst(dt):
#             return DSTDIFF
#         else:
#             return ZERO

#     def tzname(self, dt):
#         return _time.tzname[self._isdst(dt)]

#     def _isdst(self, dt):
#         tt = (dt.year, dt.month, dt.day,
#               dt.hour, dt.minute, dt.second,
#               dt.weekday(), 0, 0)
#         stamp = _time.mktime(tt)
#         tt = _time.localtime(stamp)
#         return tt.tm_isdst > 0

# Local = LocalTimezone()
# print(Local.tzname(datetime))
