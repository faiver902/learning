import asyncio
import json
import time

import httpx

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b"
    "2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ3OTAxOTI1LC"
    "JpYXQiOjE3NDc4MTU1MjUsImp0aSI6IjljNDQzZDliNTRkODQ"
    "0YjM5NzVkZTc0YzQ0MGQ0ZjQyIiwidXNlcl9pZCI6MX0.Q2t4"
    "5ToWy8HSXZ-13rQv7VGuB1N71X_eYS2XMKXbIxE",
    "user-agent": "my-app/0.0.1",
}
res = httpx.get("http://127.0.0.1:8000/api/users/4/articles", headers=headers)
with httpx.stream("GET", "http://127.0.0.1:8000/api/users/4/articles") as r:
    for text in r.iter_bytes():
        print(text)

with httpx.Client(headers=headers) as client:
    try:
        param = {"y": 8}
        response = client.get(
            "http://127.0.0.1:8000/api/users/4/articles", params=param
        )
        print(response.request.headers["user-agent"])
        print(response.request.headers)
        print(json.dumps(dict(response.headers), ensure_ascii=False, indent=4))
        # response.status_code = httpx.codes.GONE
    except Exception as e:
        print(e)

with httpx.Client(auth=("tom", "mot123")) as client:
    r = client.get(
        "http://127.0.0.1:8000/api/users/4/articles", auth=("alice", "ecila123")
    )

_, _, auth = r.request.headers["Authorization"].partition(" ")
print(auth)
import base64

print(base64.b64decode(auth))
# b'alice:ecila123'

from httpx import Response

url_1 = "http://127.0.0.1:8000/api/users/4/articles"

url_2 = "http://127.0.0.1:800/"
max_retry = 4
delay = 2

for attempt in range(1, max_retry + 1):
    try:
        if attempt == 4:
            response = httpx.get(url_1)
            print("response 4", response.status_code)
        else:
            response = httpx.get(url_2)
        print("response", response.status_code)
    except (httpx.HTTPError, httpx.RequestError) as e:
        print("httpx error ", e)
        if attempt < max_retry:
            time.sleep(delay)
        else:
            print("try is over")

url = "http://httpbin.org/get"


async def main():
    async with httpx.AsyncClient() as client:
        tasks = [asyncio.create_task(client.get(url)) for _ in range(10)]
        result, _ = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        if result:
            for i in tasks:
                if not i.done():
                    i.cancel()
        return result


result: list[Response] = asyncio.run(main())
print(result)
