import os
from PIL import Image
from loguru import logger


class ImageTool:

    @staticmethod
    def turn_caption(image_path: str, turn: str) -> None:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image Not Found: {image_path}")
        turn_paths = {
            "w": "app/common/assets/white_to_play.png",
            "b": "app/common/assets/black_to_play.png",
        }
        turn_image = Image.open(turn_paths[turn])
        image = Image.open(image_path)

        img_width, img_height = image.size
        turn_width, turn_height = turn_image.size

        new_width = img_width
        new_height = img_height + turn_width + 12

        new_image = Image.new("RGBA", (new_width, new_height), (255, 255, 255, 0))

        new_image.paste(image, (0, turn_height + 12))
        new_image.paste(turn_image, (img_width - 12 - turn_width, 0))

        new_image.save(image_path)

    @staticmethod
    def image_crop(image_path: str) -> None:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image Not Found: {image_path}")
        image = Image.open(image_path)
        img_width, img_height = image.size
        image = image.crop((24, 24, img_width - 24, img_height - 24 - 48))
        image.save(image_path)
