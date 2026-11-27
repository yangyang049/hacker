LEGAL_RETENTION_YEARS = 5

def archive_withdrawn_user(user_id: int, db):
    """법적 의무에 따라 탈퇴 회원 데이터를 5년간 분리 보관 (복구 불가)"""
    user = db.find_user(user_id)
    db.move_to_legal_archive(user, years=LEGAL_RETENTION_YEARS)
    db.block_rejoin(user.email)
    return {
        "message": "법령에 따라 5년간 분리 보관되며 계정 복구는 불가능합니다.",
        "retention_years": LEGAL_RETENTION_YEARS,
        "recoverable": False,
    }
