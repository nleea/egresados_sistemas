def readeable_hour(hours: str) -> str:
    valid, gst = hours.split(" ")
    middle = 12

    if gst == "PM":
        hour, minute = valid.split(":")
        middle += int(hour)

        if len(minute) == 1:
            minute = f"0{minute}"

        return ":".join([str(middle), minute])

    elif gst == "AM":
        hour, minute = valid.split(":")

        if len(minute) == 1:
            minute = f"0{minute}"

        return ":".join([str(hour), minute])

    return ""
