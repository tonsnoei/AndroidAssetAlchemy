import os
from PIL import Image
from enum import Enum

from services.image.models.size import Size


class ImageFormat(Enum):
    PNG = "PNG"
    # SVG = "SVG"
    WEBP = "WEBP"

class ImageConverter:
    def __init__(self):
        pass

    def convert(self, file_name: str, format: ImageFormat):
        output_file_name: str = self._get_output_file_name(file_name, format)
        self._open_file(file_name).save(output_file_name)

    def resize(self, in_file_name: str, out_file_name: str, size: Size):
        image = self._open_file(in_file_name)
        resized_image = self._resize_image(image, size)
        resized_image.save(out_file_name)

    def _resize_image(self, image: Image, size: Size) -> Image:
        resized_image = image.resize(size.to_tuple())
        return resized_image

    def _open_file(self, file_name: str) -> Image:
        return Image.open(file_name)

    def _get_output_file_name(self, file_name: str, format: ImageFormat):
        base_name, ext = os.path.splitext(file_name)
        new_file_name = f"{base_name}.{format.value}"
        return new_file_name

    def is_supported(self, file_name: str) -> bool:
        return file_name.lower().endswith(".png") or file_name.lower().endswith(".webp")

    def get_size(self, file) -> Size:
        image: Image = self._open_file(file)
        return Size(image.width, image.height)
