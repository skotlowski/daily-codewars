def format_duration(seconds):
    result = ""
    minutes = False
    hours = False
    if seconds == 0:
        return 'now'
    else:
        if seconds // 31536000 >= 1:
            year = seconds // 31536000
            seconds = seconds - (year * 31536000)

            if year == 1:
                result += f'{year} year'
            else:
                result += f'{year} years'

        if seconds // 86400 >= 1:
            day = seconds // 86400
            seconds = seconds - (day * 86400)

            if day == 1:
                if len(result) == 0:
                    result += f'{day} day'
                else:
                    result += f', {day} day'
            else:
                if len(result) == 0:
                    result += f'{day} days'
                else:
                    result += f', {day} days'

        if seconds // 3600 >= 1:
            hour = seconds // 3600
            seconds = seconds - (hour * 3600)

            if hour == 1:
                if len(result) == 0:
                    result += f'{hour} hour'
                else:
                    result += f', {hour} hour'
            else:
                if len(result) == 0:
                    result += f'{hour} hours'
                else:
                    result += f', {hour} hours'
            hours = True

        if seconds // 60 >= 1:
            minute = seconds // 60
            seconds = seconds - (minute * 60)

            if minute == 1:
                if len(result) == 0:
                    result += f'{minute} minute'
                else:
                    result += f', {minute} minute'

            elif seconds == 0 and hours:
                if minute == 1:
                    result += f' and {minute} minute'
                else:
                    result += f' and {minute} minutes'

            else:
                if len(result) == 0:
                    result += f'{minute} minutes'
                else:
                    result += f', {minute} minutes'

            minutes = True

        if seconds > 0:
            if minutes or hours:
                if seconds == 1:
                    result += f' and {seconds} second'
                else:
                    result += f' and {seconds} seconds'
            else:
                if seconds == 1:
                    if len(result) == 0:
                        result += f'{seconds} second'
                    else:
                        result += f', {seconds} second'
                else:
                    if len(result) == 0:
                        result += f'{seconds} seconds'
                    else:
                        result += f', {seconds} seconds'

        return result
