# 소셜 로그인 및 로그인 UI 설정
LOGIN_BUTTON_TEXT = "로긴"

SUPPORTED_PROVIDERS = []

def social_login(provider: str, token: str):
    # 카카오 로그인 제거됨 (유지보수 부담 및 낮은 사용률)
    raise ValueError("현재 소셜 로그인을 지원하지 않습니다.")
