# 데이터 심화1

# 데이터끼리의 관계가 매우 복잡해지는 문제를 해결
# *객채지향 프로그래밍*
# 관계가 있는 데이터 와 함수 끼리모아 하나의 객채로 만들어 관린한다

# 객채지향 프로그래밍 원칙
# 1. 추상화 : 객채 사용자가 클래스 내부를 알지 못해도 편리하게 사용할수 있도록 추상화한다
# 직관적으로 잘알수 있도록 가독성있게 작성
# 2. 캡슐화 : 속성을 감추고 메소드로 컨트롤 한다 (앞에__붙이면 감춰짐)
# 3. 상속 : 부모 클래스를 최대한 활용한다
# 4. 다형성 : 이름도 같고 파라미터도 같은데 로직이 다른 함수(오버라이딩)
# (오버로딩 : 이름은 같은데 파라미터는 다른 함수 , 파이썬은 안됌)

# 객채지향 프로그래밍 설계원칙
# 1. 단읽 책임 원칙
# 2. 개방 폐쇄 원칙
# 3. 리스코프 치환의 원칙(부모 객채를 자식 객채가 대신 할수 있다)
# 4. 인터페이스 분리 원칙
# 5. 의존 역전 원칙


# 객채 틀 : class
from abc import *


class User(metaclass=ABCMeta):  # ABCMeta 추상메서드 쓰기위해
    # 인스턴스 변수, 클래스 변수
    # 인스턴스 메소드, 클래스 메소드, 스태틱 메소드, 매직 메소드, 추상 메소드

    # 클래스 변수
    user_count = 0

    # 스태틱 메소드 클래스변수처럼 한번만 존재하는 클래스 자체적으로가지는 메소드
    @staticmethod
    def zzzZ():
        print("zzzzzzz")

    # 클래스 메소드 클래스 변수를 컨트롤
    @classmethod
    def plus_user_count(cls):
        cls.count += 1

    # 추상 메소드 : 빈 메소드 무조건 자식클래스에서 재정의해주어야함
    @abstractmethod
    def improducing(self):
        pass

    # 매직 메소드 : 특정 상황이 되면 자동으로 실행
    def __init__(self, user_id, user_password, is_student):  # 객채를 만들때 자동으로 실행 (self는 객채 자신을 가리킴)
        # 인스턴스 변수
        self.__User_id = user_id
        self.__User_password = user_password  # __ 붙이면 감춰짐 외부에서 접근 불가
        self.__is_student = is_student
        User.plus_user_count()

    # 인스턴스 메소드
    def get_user_id(self):
        return self.__User_id

    def set_user_id(self, new_id):
        self.__User_id = new_id

    def set_user_password(self, new_password):
        self.__User_password = new_password

    def if_student(self):
        if self.__is_student == True:
            print("학생임")
        else:
            print("학생아님")


class Influencer(User):  # 괄호안에 부모가되는 클래스
    def __init__(self, user_id, user_password, is_student, user_NickName):
        super.__init__(self, user_id, user_password, is_student) # super은 부모클래스
        # 부모 클래스위 생성자를 먼저 불러오고 거기에
        self.__user_nickName = user_NickName
        # 자식만의 생성자를 추가
        # 이 과정이 없으면 부모 클래스의 생성자를 자동으로 호출한다

    def improducing(self):
        print(self.get_user_id())

    def is_student(self): # 오버라이딩
        print("인플루언서임")


class Company(User):
    def improducing(self):
        print(self.get_user_id())

    def is_student(self): # 오버라이딩
        print("기업임")


user1 = User("aaa", 1111, True)
user2 = User("bbb", 2222, False)
user2 = User("ccc", 3333, False)
print(user1.User_id)
print(user2.User_password)
print(user2.is_student)


userA = Influencer("kkk", 321, False)
userB = Company("cam", 123, False)



#######################################################3

# 데이터 심화2

# 데이터의 양이 많아져서 발생하는 메모리상의 문제 해결
# 지연평가 : 프로그램이 실제로 요구하는 순간에만 데이터를 불러옴
