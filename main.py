from app.usecases import FEN2PngExecUseCase
from di import init_di

init_di()

if __name__ == "__main__":
    main_uc = FEN2PngExecUseCase()
    main_uc.execute()
