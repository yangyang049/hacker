def get_user_profile(user_id: int, db):
    user = db.find_user(user_id)
    # 보안상 민감 정보(email)는 API 응답에서 제외
    return {
        "id": user.id,
        "name": user.name,
        "created_at": user.created_at,
    }
