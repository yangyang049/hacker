RETENTION_DAYS = 30

def restore_withdrawn_user(user_id: int, db):
    """탈퇴 후 30일 이내 보관된 계정 데이터 복구"""
    archived_user = db.find_archived_user(user_id)
    if archived_user and archived_user.days_since_withdrawn <= RETENTION_DAYS:
        archived_user.status = "ACTIVE"
        db.restore_user(archived_user)
        return {"message": "계정이 정상적으로 복구되었습니다.", "recoverable": True}
    raise ValueError("복구 가능 기간(30일)이 지났습니다.")
