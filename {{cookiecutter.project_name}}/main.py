from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from dotenv import load_dotenv

__version__ = "{{cookiecutter.project_version}}"


load_dotenv()

async def homepage(request) -> JSONResponse:
    return JSONResponse({"hello": "world"})


app = Starlette(debug=True, routes=[Route("/", homepage)])