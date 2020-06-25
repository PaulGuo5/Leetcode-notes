class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minu_angle = minutes * 6 if minutes != 60 else 0
        hour_angle = hour * 30 if hour != 12 else 0
        hour_angle += minutes / 60 * (360//12)
        res = abs(hour_angle-minu_angle)
        return res if res <=180 else 360-res
