def solution(s):
    answer = []
    
    # title함수는 무조건 첫번째로 나오는 알파벳을 대문자로
    # capitalize함수는 첫번째 글자만 대문자로! (숫자는 해당x)
    words = s.split(' ')
    
    for word in words:
        answer.append(word.capitalize())
    
    # join 함수 암기! join앞에 띄워서 배열을 연결.
    # 리스트 -> 문자열 변환하는게 join함수
    return ' '.join(answer)