from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        format = "%Y-%m-%d"
        return abs(datetime.strptime(date2, format) - datetime.strptime(date1, format)).days
