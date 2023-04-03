import sys

def myInput():
    return sys.stdin.readline().rstrip()
    
def solution(n, student_list, main, sub):
    answer = 0
    
    for student in student_list:
        answer += 1
        student = student - main if student - main >= 0 else 0
        
        mok, left = divmod(student, sub)
        
        answer += mok if left == 0 else mok + 1
    
    return answer


n = myInput()
student_list = list(map(int, myInput().split()))
main, sub = map(int, myInput().split())

print(solution(n, student_list, main, sub))