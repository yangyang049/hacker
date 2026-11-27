def withdraw_user(user_id: int, db):
    """회원 탈퇴 시 모든 데이터 즉시 영구 삭제"""
    db.hard_delete_user_data(user_id)
    db.hard_delete_user_logs(user_id)
    return {"message": "모든 데이터가 즉시 영구 삭제되었습니다.", "recoverable": False}
