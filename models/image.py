from abc import ABC, abstractmethod


class Image(ABC):
    """Базовый класс изображения.

    Хранит название и размеры изображения. Конкретные типы изображений
    наследуются от этого класса и реализуют метод display().
    """

    def __init__(self, title: str, width: int, height: int) -> None:
        """Инициализирует изображение.

        :param title: название изображения.
        :param width: ширина в пикселях/условных единицах.
        :param height: высота в пикселях/условных единицах.
        :raises ValueError: если название пустое или размеры не положительны.
        """
        if not title.strip():
            raise ValueError("Название изображения не может быть пустым.")
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными.")

        self._title = title.strip()
        self._width = width
        self._height = height

    @property
    def title(self) -> str:
        """Название изображения."""
        return self._title

    @property
    def width(self) -> int:
        """Ширина изображения."""
        return self._width

    @property
    def height(self) -> int:
        """Высота изображения."""
        return self._height

    @property
    def aspect_ratio(self) -> float:
        """Соотношение сторон изображения."""
        return self._width / self._height

    @abstractmethod
    def display(self) -> str:
        """Возвращает строку для «показа» изображения в консоли."""
        raise NotImplementedError

    def __str__(self) -> str:
        """Читаемое представление изображения."""
        return (
            f"{self.__class__.__name__}: «{self.title}», "
            f"{self.width}×{self.height}"
        )

    def __repr__(self) -> str:
        """Техническое представление изображения."""
        return (
            f"{self.__class__.__name__}("
            f"title={self.title!r}, width={self.width}, height={self.height})"
        )
