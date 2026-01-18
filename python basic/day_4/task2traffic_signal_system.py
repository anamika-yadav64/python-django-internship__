def traffic_action(color):
    if color == "red":
        return "Stop 🚫"
    elif color == "yellow":
        return "Ready ⚠️"
    elif color == "green":
        return "Go ✅"
    else:
        return "Invalid signal"