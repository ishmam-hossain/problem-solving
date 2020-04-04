from datetime import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        _date = datetime.strptime(date, "%Y-%m-%d")
        return (_date - datetime(_date.year, 1, 1)).days + 1
