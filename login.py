# 소셜 로그인 및 로그인 UI 설정
LOGIN_BUTTON_TEXT = "로긴"

SUPPORTED_PROVIDERS = ["kakao", "naver", "google"]

def social_login(provider: str, token: str):
    if provider == "kakao":
        return verify_kakao_token(token)
    elif provider == "naver":
        return verify_naver_token(token)
    elif provider == "google":
        return verify_google_token(token)
    raise ValueError("지원하지 않는 로그인 방식입니다.")
