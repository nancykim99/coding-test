'''
BOJ26150 : Identify, Sort, Index, Solve (S5)

해결 방법 : 전부 입력 받고, sorting 후, 각 단어에서 인덱스 - 1의 문자를 꺼내기
'''

n = int(input())
arr =[]
ans_arr = []

for i in range(n):
    word, num, rank = input().split()
    arr.append((int(num), word, int(rank)))

arr.sort()

for i in range(n):
    rank = arr[i][2]
    temp = arr[i][1][rank-1]
    if type(temp) is str:
        temp = temp.upper()
    ans_arr.append(temp)

print(''.join(ans_arr))