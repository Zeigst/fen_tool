from pydantic_settings import BaseSettings


class ChessvisionSettings(BaseSettings):
    chessvision_base_url: str

    class Config:
        env_file = ".env"
