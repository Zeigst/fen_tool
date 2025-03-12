from app.usecases import *
from di import init_di

init_di()

if __name__ == "__main__":
    # main_uc = FEN2PngExecUseCase()
    main_uc = ChessvisionUseCase()
    main_uc.execute()
