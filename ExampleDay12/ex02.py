'''
! 가변인자
- 입력값이 여러 개일 때 사용하면 됨 (몇개의 값을 받을지 모를때)
- 만약에 매개변수의 숫자가 많아진다는 가정하에 굉장히 비효율적으로 작업하는 것을 단순하게 처리
- 가변인자 함수는 말 그대로 함수의 매개변수 숫자를 모를 때 사용하는 방식
- 함수의 매개변수를 몇개를 입력하든 함수 내에서 튜플로 인식
- (*args) 가변인자는 다른 변수명으로 바꿀 수 있지만,
    가독성을 위해서 args(=arguments) 그대로 사용하는걸 권장

형식)
def a(*args):
     코드 ...
'''

def a(*args):
    print(args);
    print(type(args)); # tuple
a(1,2,3,4,5,6,7,8,9,10);