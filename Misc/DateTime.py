from datetime import date, tzinfo, timedelta, datetime, timezone
import time

class DateTimeClass: 

    def current_date_dtls(self): 
        print('Current Date: ', date.today())
        print('Current Day: ', date.today().day)
        print('Current Day: ', date.today().month)
        print('Current Day: ', date.today().year)

    def current_time_dtls(self): 
        now = date.today()
        dateTime = datetime(now.year, now.month, now.day,now.timetuple().tm_hour, tzinfo=timezone.utc)
        print('Current time: ', time.strftime('%H:%M:%S %p'))
        print('Time by Zone UTC: ', datetime.now(timezone.utc).time())

    def date_time_data_concatenation(self): 
        currentDate = date.today().__str__()
        currentTime = time.strftime('%H:%M:%S %p').__str__()

        logging_strings = ['DateTime file executed at ', currentDate , currentTime ]

        # Created an empty array
        process_strings = []

        # Running a loop to append list with specifier 
        for str in logging_strings: 
            process_strings.append(str)
            process_strings.append(" ")

        # Using join to concatenate at one go to generate final string. 
        loggingMessage = ''.join(process_strings)

        print(loggingMessage)



dtInstance = DateTimeClass()
dtInstance.current_date_dtls()
dtInstance.current_time_dtls()
dtInstance.date_time_data_concatenation()

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

