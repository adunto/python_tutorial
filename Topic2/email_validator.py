# 3) 질문: 입력된 이메일 주소가 유효한지 검사하세요. (조건: @와 . 포함)
#         (형식: "user@example.com")
#     파일명: email_validator.py
#     실행: python email_validator.py
#     결과: 이메일 주소: user@example.com
#                 유효함
#                 이메일 주소: user@example
#                 유효하지 않음


def validate_email(email):
    print(f"이메일 주소: {email}")
    
    if str(email).find('@') < 0:
        print(f"유효하지 않음 : '@'문자 없음 ({email})")
        return 
    
    id, domain = email.split('@')
    
    if str(domain).find('.') < 0:
        print(f"유효하지 않음 : '.'문자 없음 ({email})")
        return 
    
    platform, domain = domain.split('.')
    
    if len(id) <= 0 or len(domain) <= 0 or len(platform) <= 0:
        print(f"유효하지 않음 : 형식 오류 ({email})")
        return
    
    print("유효함")
    
    
validate_email("user@example.com")
validate_email("user@example")