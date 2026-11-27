from models.gallery import ImageGallery
from models.image_types import AnimatedImage, RasterImage, VectorImage


class Terminal:
    """Консольный интерфейс для работы с галереей изображений."""

    def __init__(self, gallery: ImageGallery) -> None:
        """Создаёт терминал для указанной галереи."""
        self.gallery = gallery

    def run(self) -> None:
        """Запускает зацикленное меню."""
        while True:
            self._print_menu()
            command = input("Пункт меню: ").strip()

            if command == "0":
                print("Выход из программы.")
                break

            try:
                if command == "1":
                    self._add_raster()
                elif command == "2":
                    self._add_vector()
                elif command == "3":
                    self._add_animated()
                elif command == "4":
                    self._show_all()
                elif command == "5":
                    self._show_next()
                elif command == "6":
                    self._cycle_show()
                elif command == "7":
                    self._remove_image()
                elif command == "8":
                    self._clear_gallery()
                else:
                    print("Неверный пункт меню.")
            except (ValueError, IndexError, TypeError) as exc:
                print(f"Ошибка: {exc}")

            input("\nНажмите Enter для продолжения...")

    @staticmethod
    def _print_menu() -> None:
        """Выводит меню."""
        print("\n=== Управление показом изображений ===")
        print("1. Добавить растровое изображение")
        print("2. Добавить векторное изображение")
        print("3. Добавить анимированное изображение")
        print("4. Показать все изображения")
        print("5. Показать следующее изображение")
        print("6. Циклический показ")
        print("7. Удалить изображение")
        print("8. Очистить галерею")
        print("0. Выход")

    @staticmethod
    def _read_int(prompt: str, default: int | None = None) -> int:
        """Читает целое число."""
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            return default
        return int(raw)

    @staticmethod
    def _read_float(prompt: str, default: float) -> float:
        """Читает число с плавающей точкой."""
        raw = input(prompt).strip()
        if raw == "":
            return default
        return float(raw)

    def _add_raster(self) -> None:
        """Добавляет растровое изображение."""
        title = input("Название: ")
        width = self._read_int("Ширина: ")
        height = self._read_int("Высота: ")
        extension = input("Расширение (по умолчанию png): ").strip() or "png"
        dpi = self._read_int("DPI (по умолчанию 72): ", default=72)

        image = RasterImage(title, width, height, extension, dpi)
        self.gallery.add_image(image)
        print(f"Добавлено: {image}")

    def _add_vector(self) -> None:
        """Добавляет векторное изображение."""
        title = input("Название: ")
        width = self._read_int("Ширина: ")
        height = self._read_int("Высота: ")
        vector_format = input("Формат (по умолчанию svg): ").strip() or "svg"
        elements_count = self._read_int(
            "Количество элементов (по умолчанию 0): ", default=0
        )

        image = VectorImage(
            title, width, height, vector_format, elements_count
        )
        self.gallery.add_image(image)
        print(f"Добавлено: {image}")

    def _add_animated(self) -> None:
        """Добавляет анимированное изображение."""
        title = input("Название: ")
        width = self._read_int("Ширина: ")
        height = self._read_int("Высота: ")
        frames = self._read_int("Количество кадров: ")
        fps = self._read_int("FPS (по умолчанию 24): ", default=24)

        image = AnimatedImage(title, width, height, frames, fps)
        self.gallery.add_image(image)
        print(f"Добавлено: {image}")

    def _show_all(self) -> None:
        """Показывает список всех изображений."""
        print(self.gallery)

    def _show_next(self) -> None:
        """Показывает следующее изображение по кругу."""
        image = self.gallery.next_image()
        print(image.display())

    def _cycle_show(self) -> None:
        """Запускает циклический показ изображений."""
        if len(self.gallery) == 0:
            print("Галерея пуста.")
            return

        steps = self._read_int(
            "Количество шагов (Enter = полный круг): ",
            default=len(self.gallery),
        )
        delay = self._read_float(
            "Задержка между кадрами, сек (Enter = 0.5): ",
            default=0.5,
        )

        print("\nЦиклический показ:")
        self.gallery.cycle_show(steps=steps, delay=delay)
        print("Показ завершён.")

    def _remove_image(self) -> None:
        """Удаляет изображение по номеру."""
        if len(self.gallery) == 0:
            print("Галерея пуста.")
            return

        print(self.gallery)
        number = self._read_int("Номер изображения для удаления: ")
        removed = self.gallery.remove_at(number - 1)
        print(f"Удалено: {removed}")

    def _clear_gallery(self) -> None:
        """Очищает галерею после подтверждения."""
        if len(self.gallery) == 0:
            print("Галерея уже пуста.")
            return

        answer = input("Очистить галерею? (да/нет): ").strip().lower()
        if answer in {"да", "д", "yes", "y"}:
            self.gallery.clear()
            print("Галерея очищена.")
        else:
            print("Очистка отменена.")
