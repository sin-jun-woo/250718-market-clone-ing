# /Users/shin-junwoo/슈퍼코딩/코드 설명/250716/mission.py

# FastAPI 관련 클래스와 함수들을 가져옵니다.
# FastAPI: API 서버의 핵심 인스턴스를 생성합니다.
# Response: HTTP 응답 객체로, 쿠키 설정 등에 사용됩니다.
# Request: HTTP 요청 객체로, 쿠키나 헤더 정보에 접근할 때 사용됩니다.
# Depends: 의존성 주입 시스템으로, 특정 함수를 먼저 실행하고 그 결과를 받아오게 합니다.
from fastapi import FastAPI, Response, Request, Depends

# JSON Web Token(JWT)을 생성하고 검증하기 위한 라이브러리를 가져옵니다.
import jwt

# FastAPI 애플리케이션 인스턴스를 생성합니다.
app = FastAPI()

# '/login' 경로로 POST 요청이 왔을 때 실행될 함수를 정의합니다.
# 사용자가 로그인 정보를 보내면 이 경로에서 처리합니다.
@app.post("/login")
async def login(response: Response):
    # --- 실제 애플리케이션에서는 이 부분에 사용자 인증 로직이 필요합니다. ---
    # 예를 들어, 데이터베이스에서 사용자 아이디와 비밀번호를 확인하고,
    # 인증에 성공하면 해당 사용자의 고유 ID(user_id)를 가져옵니다.
    # 이 예제에서는 user_id와 SECRET_KEY가 이미 정의되어 있다고 가정합니다.
    user_id = "testuser"
    SECRET_KEY = "your-secret-key" # 🚨 실제 서비스에서는 절대 코드에 직접 작성하면 안 됩니다!

    # JWT를 생성합니다.
    # payload: 토큰에 담을 정보 (여기서는 user_id)
    # SECRET_KEY: 토큰을 암호화하고 서명할 때 사용하는 비밀 키
    # algorithm: 사용할 암호화 알고리즘
    token = jwt.encode({"user_id": user_id}, SECRET_KEY, algorithm="HS256")

    # 생성된 토큰을 'access_token'이라는 이름의 쿠키로 클라이언트(브라우저)에 설정합니다.
    # 이 쿠키는 앞으로 서버에 요청을 보낼 때마다 함께 전송됩니다.
    response.set_cookie(key="access_token", value=token)
    
    # 로그인 성공 메시지를 JSON 형태로 반환합니다.
    return {"message": "로그인 성공"}

# 의존성 주입에 사용될 함수입니다.
# 요청(Request) 객체에서 쿠키를 읽어 'access_token' 값을 반환합니다.
async def get_token(request: Request):
    return request.cookies.get("access_token")

# '/protected' 경로로 GET 요청이 왔을 때 실행될 함수를 정의합니다.
# 이 경로는 로그인이 필요한, 보호된 자원에 접근하는 경로입니다.
@app.get("/protected")
# 'Depends(get_token)'을 통해 이 경로에 접근하기 전에 항상 get_token 함수가 먼저 실행됩니다.
# get_token 함수가 반환한 값(쿠키에서 읽어온 토큰)이 'token' 매개변수에 전달됩니다.
async def protected_route(token: str = Depends(get_token)):
    # --- 토큰 검증 및 인증 로직이 필요한 부분입니다. ---
    # 1. token이 존재하는지 확인합니다. (없다면 로그인되지 않은 사용자)
    # 2. jwt.decode()를 사용하여 토큰이 유효한지(SECRET_KEY로 서명되었는지, 만료되지는 않았는지 등) 검증합니다.
    # 3. 토큰 검증에 실패하면 에러(예: 401 Unauthorized)를 반환합니다.
    # 4. 검증에 성공하면 보호된 데이터를 반환합니다.
    if token:
        # 이 예제에서는 단순히 토큰이 있다는 것만 확인하고 성공 메시지를 보냅니다.
        return {"message": "보호된 라우트에 접근 성공!", "token": token}
    else:
        return {"message": "토큰이 없어 접근할 수 없습니다."}

