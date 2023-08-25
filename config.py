from fastapi import FastAPI,status,Request, staticfiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dependencies.exception import EmailNotValid
from routers import users,salestable,news,auth
from routers.categories import theater,screening,artandexprience,comedytheater,childrenstheater

app = FastAPI()

app.mount("/uploads/salestable", staticfiles.StaticFiles(directory="uploads/salestable"), name="uploads")
app.mount("/uploads/news", staticfiles.StaticFiles(directory="uploads/news"), name="uploads")
app.mount("/uploads/theater", staticfiles.StaticFiles(directory="uploads/theater"), name="uploads")
app.mount("/uploads/screening", staticfiles.StaticFiles(directory="uploads/screening"), name="uploads")
app.mount("/uploads/artandexprience", staticfiles.StaticFiles(directory="uploads/artandexprience"), name="uploads")
app.mount("/uploads/comedytheater", staticfiles.StaticFiles(directory="uploads/comedytheater"), name="uploads")
app.mount("/uploads/childrenstheater", staticfiles.StaticFiles(directory="uploads/childrenstheater"), name="uploads")

app.include_router(users.router, tags=["users"])
app.include_router(auth.router, tags=["authentication"])
app.include_router(theater.router, tags=["theaters"])
app.include_router(screening.router, tags=["screenings"])
app.include_router(artandexprience.router, tags=["artandexpriences"])
app.include_router(comedytheater.router, tags=["comedytheaters"])
app.include_router(childrenstheater.router, tags=["childrenstheaters"])
app.include_router(salestable.router, tags=["salestable"])
app.include_router(news.router, tags=["news"])


@app.exception_handler(EmailNotValid)
def email_not_valid(request:Request, exc:EmailNotValid):
    return JSONResponse(content=str(exc), status_code=status.HTTP_400_BAD_REQUEST)


origins = ["http://localhost:3000","http://127.0.0.1:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
    )