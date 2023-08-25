import uvicorn

if __name__ == "__main__":
    uvicorn.run("config:app", host="127.0.0.1", port=4000 ,reload=True)