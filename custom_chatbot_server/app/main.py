from server.app import app


if __name__ == "__main__":
    import uvicorn

    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    #docker使用時には以下に変更
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)

