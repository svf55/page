from concurrent.futures import ThreadPoolExecutor
import requests
import time
import random


def measure_api_pages(n=1000, w=10, pages=(1, 2, 3)):
    def worker(page):
        t1 = time.time()
        r = requests.get('http://localhost:8000/api/v1/pages/{}/'.format(page))
        assert r.status_code == 200
        t2 = time.time() - t1
        print('time in miliseconds: {}'.format(t2 * 1000))
        return t2

    executor = ThreadPoolExecutor(max_workers=w)
    pool = executor.map(worker, [random.choice(pages) for _ in range(n)])
    res = sum(pool)
    print('requests compleated: {}'.format(n))
    print('average time in miliseconds: {}'.format(res*1000/n))


if __name__ == '__main__':
    measure_api_pages(pages=[1])

