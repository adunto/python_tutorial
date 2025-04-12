# 2) 질문: 주민등록번호 "901212-1234567"에서 생년월일을 추출하세요. 
#         (형식: "1990년 12월 12일")
#     파일명: id_number_parser.py
#     실행: python id_number_parser.py
#     결과: 1990년 12월 12일

id_number = "901212-1234567"

# 2000년 이전 출생자 : 남자(1) 여자(2) <== 뒷자리 첫 번째 숫자
# 2000년 이후 출생자 : 남자(3) 여자(4) <== 뒷자리 첫 번째 숫자

front_line, end_line = id_number.split('-')

year_prefix = "19" if end_line[0] in "12" else "20"
year = year_prefix + front_line[:2]
month = front_line[2:4]
day = front_line[-2:]

print(f"{year}년 {month}월 {day}일")