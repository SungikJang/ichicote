##################################################################
# 대충 코드의 흐름만
##################################################################


import threading
import logging
import time
import random


def thread_func(name):
    logging.info("나는 자식 쓰레드. 작업 시작")
    time.sleep(random.randint(1,2))
    print(name)
    time.sleep(random.randint(1,2))
    logging.info("나는 자식 쓰레드. 작업 종료")

def main():
    logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("나는 메인 쓰레드. 작업 시작")
    thread_pool = []
    for i in range(1,10):
        child_thread = threading.Thread(target=thread_func, args=(str(i),), daemon=True)
        logging.info("나는 메인쓰레드. 자식 쓰레드 생성했다")
        thread_pool.append(child_thread)

    for child_thread in thread_pool:
        child_thread.start()
        child_thread.join() # 자식스레드가 종료되길 기다린다

    logging.info("나는 메인스레드 작업 종료")



if __name__ == "__main__":
    main()