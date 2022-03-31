##################################################################
# 대충 코드의 흐름만
##################################################################


from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.request
import logging

URLS = ["https://www.naver.com/",
        "https://www.nate.com/",
        "https://www.daum.com/",
        "https://www.youtube.com/",
        "https://www.google.com/"]

def load_data(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

def main():
    logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("나는 메인 쓰레드 작업 시작")
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(load_data, url, 60): url for url in URLS}
        for future in as_completed(future_to_url):
            try:
                data = future.result()
                url = future_to_url[future]
                print("%r page is %d bytes" % (url, len(data)))
            except Exception as e:
                print("%r generated an exception: %s" % (url,e))
    logging.info("나는 메인쓰레드 작업 종료")


if __name__ == "__main__":
    main()