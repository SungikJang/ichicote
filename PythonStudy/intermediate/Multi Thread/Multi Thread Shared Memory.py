##################################################################
# 대충 코드의 흐름만
##################################################################


from concurrent.futures import ThreadPoolExecutor
import threading

class DataStore:
    def __init__(self):
        self.value = 0  # 이 데이터 자체에 락을 거는것이 아니다
        self.lock = threading.Lock

    def increas(self): # 공유 데이터에 접근하는 부분에 락을 건다
        self.lock.acquire()
        self.value += 1
        self.lock.release()

    def decreas(self):
        self.lock.acquire()
        self.value -= 1
        self.lock.release()

def main():
    store = DataStore()

    with ThreadPoolExecutor(max_workers=5) as executor:
        for _ in range(100):
            try:
                executor.submit(store.increas())
                executor.submit(store.decreas())
            except Exception as e:
                print(e)

    print(store.value)


if __name__ == "__main__":
    main()