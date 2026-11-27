def get_user_profile(user_id: int, db):
    user = db.find_user(user_id)
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "created_at": user.created_at,
    }
