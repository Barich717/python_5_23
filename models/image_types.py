from .image import Image


class RasterImage(Image):
    """Растровое изображение."""

    def __init__(
        self,
        title: str,
        width: int,
        height: int,
        extension: str = "png",
        dpi: int = 72,
    ) -> None:
        """Создаёт растровое изображение.

        :param title: название.
        :param width: ширина.
        :param height: высота.
        :param extension: расширение файла, например png/jpg.
        :param dpi: разрешение.
        """
        super().__init__(title, width, height)
        if not extension.strip():
            raise ValueError("Расширение растрового изображения не может быть пустым.")
        if dpi <= 0:
            raise ValueError("DPI должен быть положительным.")

        self._extension = extension.strip().lower()
        self._dpi = dpi

    @property
    def extension(self) -> str:
        """Расширение файла."""
        return self._extension

    @property
    def dpi(self) -> int:
        """Разрешение изображения."""
        return self._dpi

    def display(self) -> str:
        """Имитирует показ растрового изображения."""
        return (
            f"[Растровое изображение] «{self.title}», "
            f"{self.width}×{self.height}, формат {self.extension.upper()}, "
            f"{self.dpi} dpi"
        )

    def __str__(self) -> str:
        return (
            f"{super().__str__()}, формат {self.extension.upper()}, "
            f"{self.dpi} dpi"
        )


class VectorImage(Image):
    """Векторное изображение."""

    def __init__(
        self,
        title: str,
        width: int,
        height: int,
        vector_format: str = "svg",
        elements_count: int = 0,
    ) -> None:
        """Создаёт векторное изображение.

        :param title: название.
        :param width: ширина.
        :param height: высота.
        :param vector_format: формат.
        :param elements_count: количество графических элементов.
        """
        super().__init__(title, width, height)
        if not vector_format.strip():
            raise ValueError("Формат векторного изображения не может быть пустым.")
        if elements_count < 0:
            raise ValueError("Количество элементов не может быть отрицательным.")

        self._vector_format = vector_format.strip().lower()
        self._elements_count = elements_count

    @property
    def vector_format(self) -> str:
        """Формат векторного изображения."""
        return self._vector_format

    @property
    def elements_count(self) -> int:
        """Количество графических элементов."""
        return self._elements_count

    def display(self) -> str:
        """Имитирует показ векторного изображения."""
        return (
            f"[Векторное изображение] «{self.title}», "
            f"{self.width}×{self.height}, формат {self.vector_format.upper()}, "
            f"элементов: {self.elements_count}"
        )

    def __str__(self) -> str:
        return (
            f"{super().__str__()}, формат {self.vector_format.upper()}, "
            f"элементов: {self.elements_count}"
        )


class AnimatedImage(Image):
    """Анимированное изображение."""

    def __init__(
        self,
        title: str,
        width: int,
        height: int,
        frames: int,
        fps: int = 24,
    ) -> None:
        """Создаёт анимированное изображение.

        :param title: название.
        :param width: ширина.
        :param height: высота.
        :param frames: количество кадров.
        :param fps: частота кадров в секунду.
        """
        super().__init__(title, width, height)
        if frames <= 0:
            raise ValueError("Количество кадров должно быть положительным.")
        if fps <= 0:
            raise ValueError("FPS должен быть положительным.")

        self._frames = frames
        self._fps = fps

    @property
    def frames(self) -> int:
        """Количество кадров."""
        return self._frames

    @property
    def fps(self) -> int:
        """Частота кадров в секунду."""
        return self._fps

    @property
    def duration(self) -> float:
        """Длительность анимации в секундах."""
        return self._frames / self._fps

    def display(self) -> str:
        """Имитирует показ анимированного изображения."""
        return (
            f"[Анимированное изображение] «{self.title}», "
            f"{self.width}×{self.height}, кадров: {self.frames}, "
            f"{self.fps} fps, длительность: {self.duration:.2f} с"
        )

    def __str__(self) -> str:
        return (
            f"{super().__str__()}, кадров: {self.frames}, "
            f"{self.fps} fps, длительность: {self.duration:.2f} с"
        )