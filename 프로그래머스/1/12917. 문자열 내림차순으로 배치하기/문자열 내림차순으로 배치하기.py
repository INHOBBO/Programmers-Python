def solution(s):
    # sorted()는 문자열을 글자 단위로 쪼개서 리스트로 만든 뒤 정렬
    answer = sorted(s, reverse=True) # ["g","f","e","d","c","b","Z"] 출력
    
    # 리스트 형태인 결과물을 ''.join()을 사용해 다시 문자열로 합치기!
    return ''.join(answer) 