from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict

__version__ = "{{cookiecutter.project_version}}"


# Settings are powered by pydantic
# https://pydantic-docs.helpmanual.io/usage/settings/
class Settings(BaseSettings):
    debug: bool = True

    # Project file system
    root_dir: Path
    src_dir: Path

    model_config = SettingsConfigDict(env_nested_delimiter="__", env_file=".env", extra="ignore")


# Learn about lifespan: https://fastapi.tiangolo.com/advanced/events/
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Expensive operation that should be exec'd once before app starts receiving requests.
    yield
    # Cleanup that happens when the app is shutting down. Also exec'd once after
    # all requests have been handled. For example, release resources like memory or a GPU.


# Define the root path
# --------------------------------------
ROOT_PATH = Path(__file__).parent

# ======================================
# Load settings
# ======================================
settings = Settings(
    # NOTE: We would like to hard-code the root and applications directories
    #       to avoid overriding via environment variables
    root_dir=ROOT_PATH,
    src_dir=ROOT_PATH / "src",
)

app = FastAPI(
    debug=settings.debug,
    lifespan=lifespan,
)


@app.get("/")
async def homepage() -> dict:
    return {"hello": "world"}
