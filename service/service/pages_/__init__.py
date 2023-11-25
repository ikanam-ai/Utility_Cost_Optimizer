from collections import namedtuple
from typing import TypedDict
from .map import main as map_
from .x_to_y import main as x_2_y
from .emissions import main as emission
from .about import main as about
from .main import main as default
from .history import main as history

Page = namedtuple("Page", "title method")


class Pages(TypedDict):
    main: Page
    main_with_children: Page
    map: Page
    emission: Page
    x_to_y: Page
    about: Page
    history: Page


pages: Pages = {
    "main": Page(title="Главная", method=default),
    "main_with_children": Page(title="Главная", method=None),
    "x_to_y": Page(title="Анализ зависимости", method=x_2_y),
    "map": Page(title="Карта", method=map_),
    "emission": Page(title="Выбросы", method=emission),
    "about": Page(title="Решение", method=about),
    "history": Page(title="История отчетов", method=history)
}
