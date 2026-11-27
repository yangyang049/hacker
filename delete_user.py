def withdraw_user(user_id: int, db):
    """회원 탈퇴 기본 처리"""
    user = db.find_user(user_id)
    user.status = "WITHDRAWN"
    db.save(user)
    return {"message": "탈퇴 요청이 접수되었습니다."}
