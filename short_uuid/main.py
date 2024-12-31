import uvicorn

from snippet.asgi import app


uvicorn.run(app)
