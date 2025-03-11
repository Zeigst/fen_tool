# Dependancies Injections
from kink import di
from app.common.settings import *
from settings import Settings

from app.common.utils.fen_tool import FenTool

def init_di():
    cfg = Settings()
    di["cfg"] = cfg
    di[Settings] = cfg
    di[FEN2PngSettings] = cfg

    di[FenTool] = FenTool
