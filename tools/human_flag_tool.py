def flag_for_human(user_id: str, message: str, reason: str):
    return{
        "user_id": user_id,
        "message": message, 
        "flagged": True,
        "reason": reason
    }