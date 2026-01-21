from fastapi import FastAPI
import uvicorn
from routers import auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Calculator App",
    description="FastAPI backend for Calculator application",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router)

@app.get("/")
def home():
    return {"message": "Welcome to Calculator Fast API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

# from fastapi import FastAPI
# import uvicorn
# from routers import region


# app = FastAPI(
#     title="GenOt API",
#     description="FastAPI backend for GenOt application",
#     version="1.0.0"
# )


# # Include routers
# app.include_router(region.router)


# @app.get("/", tags=["Root"])
# def home():
#     return {"message": "Welcome to Demo GenSharp Fast API"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8080)