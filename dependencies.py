from typing import Optional

from services.image.image_converter import ImageConverter


class Dependencies:
    _instance: Optional['Dependencies'] = None

    def __init__(self):
        self._image_converter: Optional[ImageConverter] = None
        pass

    @staticmethod
    def instance() -> 'Dependencies':
        if not Dependencies._instance:
            Dependencies._instance = Dependencies()
        return Dependencies._instance

    @property
    def image_converter(self) -> ImageConverter:
        if not self._image_converter:
            self._image_converter = ImageConverter()
        return self._image_converter

