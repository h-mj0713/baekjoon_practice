n = int(input())
file_names = [input() for _ in range(n)]

result = ""

for i in range(len(file_names[0])):#어차피 입력 문자열 개수 동일하다고 주어짐.
    char = file_names[0][i]
    for j in range(1,n):
        if file_names[j][i] != char:
            char = '?' #char 초기화
            break #if문 탈출
    result += char 

print(result)