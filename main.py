from models.gallery import ImageGallery
from models.image_types import AnimatedImage, RasterImage, VectorImage
from ui.terminal import Terminal


def main() -> None:
    """Точка входа в программу."""
    gallery = ImageGallery(
        [
            RasterImage("Закат", 1920, 1080, "jpg", 300),
            VectorImage("Логотип компании", 800, 600, "svg", 24),
            AnimatedImage("Анимация загрузки", 320, 240, 12, 24),
        ]
    )

    Terminal(gallery).run()


if __name__ == "__main__":
    main()