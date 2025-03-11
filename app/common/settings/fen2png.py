from pydantic_settings import BaseSettings


class FEN2PngSettings(BaseSettings):
    fen2png_base_url: str

    class Config:
        env_file = ".env"
