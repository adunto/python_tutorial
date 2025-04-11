# 3) 질문: 12345초를 시간, 분, 초로 변환하세요. 
#    (공식: 시 = 총초 //3600, 나머지초 = 총초 % 3600, 분 = 나머지초 // 60,  초 = 나머지초 % 60)
# 파일명: time_converter.py
# 실행: python time_converter.py
# 결과: 12345초는 3시간 25분 45초입니다.


total_time = 12345

def convert_time(total_time):
    hours = total_time // 3600
    remain_time = total_time % 3600
    minutes = remain_time // 60
    seconds = remain_time % 60
    return hours, minutes, seconds

hours, minutes, seconds = convert_time(total_time)
print(f"총 {total_time}초는 {hours}시간 {minutes}분 {seconds}초입니다.")