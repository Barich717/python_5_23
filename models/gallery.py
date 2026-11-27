import time
from collections.abc import Iterator

from .image import Image


class ImageGallery:
    """Контейнер для изображений с поддержкой циклического показа."""

    def __init__(self, images: list[Image] | None = None) -> None:
        """Создаёт галерею.

        :param images: необязательный начальный список изображений.
        """
        self._images: list[Image] = []
        self._current_index = 0

        if images:
            for image in images:
                self.add_image(image)

    def add_image(self, image: Image) -> None:
        """Добавляет изображение в галерею."""
        if not isinstance(image, Image):
            raise TypeError("В галерею можно добавлять только объекты Image.")
        self._images.append(image)
        if len(self._images) == 1:
            self._current_index = 0

    def remove_at(self, index: int) -> Image:
        """Удаляет изображение по индексу и возвращает его."""
        if not self._images:
            raise ValueError("Галерея пуста.")
        if index < 0 or index >= len(self._images):
            raise IndexError("Некорректный индекс изображения.")

        removed = self._images.pop(index)

        if not self._images:
            self._current_index = 0
        elif self._current_index >= len(self._images):
            self._current_index = 0
        elif index < self._current_index:
            self._current_index -= 1

        return removed

    def clear(self) -> None:
        """Очищает галерею."""
        self._images.clear()
        self._current_index = 0

    def reset(self) -> None:
        """Сбрасывает текущую позицию показа на начало."""
        self._current_index = 0

    def current_image(self) -> Image:
        """Возвращает текущее изображение."""
        if not self._images:
            raise ValueError("Галерея пуста.")
        return self._images[self._current_index]

    def next_image(self) -> Image:
        """Переходит к следующему изображению по кругу и возвращает его."""
        if not self._images:
            raise ValueError("Галерея пуста.")

        self._current_index = (self._current_index + 1) % len(self._images)
        return self._images[self._current_index]

    def cycle_show(
        self,
        steps: int | None = None,
        delay: float = 0.0,
        output=print,
    ) -> int:
        """Выполняет циклический показ изображений.

        :param steps: количество показов. Если None — один полный круг.
        :param delay: задержка между показами в секундах.
        :param output: функция вывода.
        :return: фактическое количество показов.
        """
        if not self._images:
            raise ValueError("Галерея пуста.")
        if steps is None:
            steps = len(self._images)
        if steps < 0:
            raise ValueError("Количество шагов не может быть отрицательным.")

        for step in range(steps):
            image = self._images[self._current_index]
            output(image.display())
            self._current_index = (self._current_index + 1) % len(self._images)

            if delay > 0 and step < steps - 1:
                time.sleep(delay)

        return steps

    def __len__(self) -> int:
        """Количество изображений в галерее."""
        return len(self._images)

    def __iter__(self) -> Iterator[Image]:
        """Итератор по изображениям."""
        return iter(self._images)

    def __getitem__(self, index: int | slice) -> Image | list[Image]:
        """Индексация и срез для галереи."""
        return self._images[index]

    def __str__(self) -> str:
        """Строковое представление галереи."""
        if not self._images:
            return "Галерея пуста."

        lines = ["Галерея изображений:"]
        for i, image in enumerate(self._images, start=1):
            lines.append(f"{i}. {image}")
        return "\n".join(lines)
