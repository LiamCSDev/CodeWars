def format_duration(seconds):
    formatted_duration = []
    if seconds == 0: 
        formatted_duration.append('now')
        formatted_duration = ''.join(formatted_duration)
    else: 
        years = int(seconds / 31536000)
        days = int((seconds - years * 31536000) / 86400)
        hours = int((seconds - (years * 31536000 + days * 86400)) / 3600)
        minutes = int((seconds - (years * 31536000 + days * 86400 + hours * 3600)) / 60)
        second = int(seconds - (years * 31536000 + days * 86400 + hours * 3600 + minutes * 60))

        if years > 0:
            if years > 1:
                formatted_duration.append(str(years) + ' years')
            else: 
                formatted_duration.append(str(years) + ' year')
        if days > 0:
            if days > 1:
                formatted_duration.append(str(days) + ' days')
            else: 
                formatted_duration.append(str(days) + ' day')
        if hours > 0:
            if hours > 1:
                formatted_duration.append(str(hours) + ' hours')
            else: 
                formatted_duration.append(str(hours) + ' hour')
        if minutes > 0:
            if minutes > 1:
                formatted_duration.append(str(minutes) + ' minutes')
            else: 
                formatted_duration.append(str(minutes) + ' minute')
        if second > 0:
            if second > 1:
                formatted_duration.append(str(second) + ' seconds')
            else: 
                formatted_duration.append(str(second) + ' second')
        formatted_duration = ", ".join(formatted_duration)
        formatted_duration = ' and '.join(formatted_duration.rsplit(', ', 1))

    return formatted_duration

print(format_duration(1) == "1 second")
print(format_duration(62) == "1 minute and 2 seconds")
print(format_duration(120) ==  "2 minutes")
print(format_duration(3600)== "1 hour")
print(format_duration(3662)== "1 hour, 1 minute and 2 seconds")
print(format_duration(62) == "1 minute and 2 seconds")
print(format_duration(120) == "2 minutes")
print(format_duration(3600) == "1 hour")
print(format_duration(3662) == "1 hour, 1 minute and 2 seconds")
print(format_duration(0))