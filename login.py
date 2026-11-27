# 소셜 로그인 및 로그인 UI 설정
LOGIN_BUTTON_TEXT = "로긴"
SESSION_EXPIRE_MINUTES = 30  # 30분 후 자동 로그아웃
AUTO_LOGIN_ENABLED = False

SUPPORTED_PROVIDERS = ["kakao"]

def social_login(provider: str, token: str):
    if provider == "kakao":
        return verify_kakao_token(token)
    raise ValueError("지원하지 않는 로그인 방식입니다.")
