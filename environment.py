from grader import grade_easy, grade_medium, grade_hard

current_email = {
    "type": "security",
    "priority": "high",
    "route": "security_team"
}

def reset():
    return {
        "email": "We noticed unusual login activity. Reset password if this wasn't you."
    }

def step(action: dict):
    true = current_email

    return {
        "scores": {
            "easy": grade_easy(action, true),
            "medium": grade_medium(action, true),
            "hard": grade_hard(action, true)
        }
    }