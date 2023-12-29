# https://fastapi.tiangolo.com/ko/tutorial/first-steps/ 를 참조한 기본 예제

from fastapi import  FastAPI

app = FastAPI()

'''
데코레이터를 정의한 것이다. index() 함수가 'app.get("/") 데이레이터'를 통해 실행됨을 의미한다.
여기서 app 은 위의 app = FastAPI() 에 의한 FastAPI 의 인스턴스이다.

@app.get("/")은 FastAPI에게 바로 아래에 있는 함수가 다음으로 이동하는 요청(경로 /, get 동작 사용)을 처리한다는 것을 알려줍니다.
이 데코레이터는 FastAPI에게 아래 함수가 경로 /에 해당하는 get 동작하라고 알려줍니다.
이것이 "path operation decorator(경로 동작 데코레이터)" 입니다.

다른 동작도 쓸 수 있습니다:
@app.post()
@app.put()
@app.delete()
@app.options()
@app.head()
@app.patch()
@app.trace()

다시 정리하면,
http://127.0.0.1:8000/ 로 접속하면 @app.get("/") 데코레이터 정의에 의해서 index 가 실행될것이다.
index()함수가 @app.get("/") 데코레이터를 통해서 실행된다는 의미임으로.
get을 post로 변경하면 당연히 http://127.0.0.1:8000/ 로 접속하면 "Method Not Allowed" 오류가 발생한다.   
'''
@app.get("/")
def index():                            # GET 동작을 사용하여 URL "/"에 대한 요청을 받을 때마다 FastAPI에 의해 호출됩니다.
    return {"index": "FastAPI 안녕"}

@app.get("/math/sum")
def math_sum(number_1: int, number_2: int):
    return {"result": number_1 + number_2}

@app.get("/math/mul")
def math_mul(number_1: int, number_2: int = 3):
    return {"result": number_1 * number_2}
