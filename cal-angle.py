###
# 16-01-2021
# Hi, here's your problem today. This problem was recently asked by Microsoft:
#
# Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.
###

###
# SOLUTION
# This is primarily breaking down the problem into a formula.
# It is more tricky than algorithmically difficult, but you might encounter questions like this as warmups.
#
# The key is to understand that the hour-hand makes a full rotation in 12 hours,
# or 12 * 60 minutes. The minute hand makes a full rotation in 60 minutes.
#
# So, that gives us a factor of 360 degree / (12 * 60) for the hour hand,
# and 360 degree / 60 for the minute hand. Then we can use this to compute the angle:
###

def calc_angle(h, m):
    if h < 0 or m < 0 or h > 12 or m > 60:
        print('Wrong input')
    if h == 12:
        h = 0
    if m == 60:
        m = 0

    hour_angle = (360 / (12.0 * 60)) * (h * 60 + m)
    minute_angle = (360 / 60.0) * m
    angle = abs(hour_angle - minute_angle)
    angle = min(360 - angle, angle)
    return angle


print(calc_angle(3, 30))