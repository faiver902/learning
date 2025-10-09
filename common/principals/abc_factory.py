from __future__ import annotations

from abc import ABC, abstractmethod


# ───────── 1. Абстрактные продукты ─────────
class Button(ABC):
    @abstractmethod
    def render(self) -> str: ...


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str: ...


# ───────── 2. Конкретные продукты ─────────
class DarkButton(Button):
    def render(self) -> str:
        return "🖤 Dark Button"


class LightButton(Button):
    def render(self) -> str:
        return "🤍 Light Button"


class DarkCheckbox(Checkbox):
    def render(self) -> str:
        return "⬛ Dark Checkbox"


class LightCheckbox(Checkbox):
    def render(self) -> str:
        return "⬜ Light Checkbox"


# ───────── 3. Абстрактная фабрика ─────────
class ThemeFactory(ABC):
    @abstractmethod
    def make_button(self) -> Button: ...

    @abstractmethod
    def make_checkbox(self) -> Checkbox: ...


# ───────── 4. Конкретные фабрики ─────────
class DarkThemeFactory(ThemeFactory):
    def make_button(self) -> Button:
        return DarkButton()

    def make_checkbox(self) -> Checkbox:
        return DarkCheckbox()


class LightThemeFactory(ThemeFactory):
    def make_button(self) -> Button:
        return LightButton()

    def make_checkbox(self) -> Checkbox:
        return LightCheckbox()


# ───────── 5. Клиентский код ─────────
def draw_ui(factory: ThemeFactory) -> None:
    btn = factory.make_button()
    chk = factory.make_checkbox()
    print(btn.render(), "|", chk.render())


# ───────── 6. Выбор семейства ─────────
theme_name = "dark"  # ← источник: env, settings, тест
factory: ThemeFactory = (
    DarkThemeFactory() if theme_name == "dark" else LightThemeFactory()
)

draw_ui(factory)
