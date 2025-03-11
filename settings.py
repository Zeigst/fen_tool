from kink import di
from app.common.settings import *
from dotenv import load_dotenv


load_dotenv()

class Settings(
    FEN2PngSettings
):
    inputs_path: str
    outputs_path: str

    class Config:
        env_file = ".env"

cfg = Settings()
di["cfg"] = cfg
di[Settings] = cfg