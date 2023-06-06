def get_seconds(hours, minutes, seconds):
    seconds_in_min = 60 * minutes
    seconds_in_hours = 60 * 60 * hours
    return seconds_in_hours + seconds_in_min + seconds

total = get_seconds(2, 30, 5)
print(total)

total = get_seconds(1, 16, 47)
print(total)
