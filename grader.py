def grade_easy(action, true):
    return 1.0 if action.get("type") == true["type"] else 0.0

def grade_medium(action, true):
    score = 0
    if action.get("type") == true["type"]:
        score += 0.5
    if action.get("priority") == true["priority"]:
        score += 0.5
    return score

def grade_hard(action, true):
    score = 0
    if action.get("type") == true["type"]:
        score += 0.4
    if action.get("priority") == true["priority"]:
        score += 0.3
    if action.get("route") == true["route"]:
        score += 0.3
    return score