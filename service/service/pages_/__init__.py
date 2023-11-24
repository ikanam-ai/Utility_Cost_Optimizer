from collections import namedtuple
from .dashboard import main as dashboard

Page = namedtuple("Page", "title method")

pages: dict[str, Page] = {
    'dashboard': Page(title="Предсказание", method=dashboard),
}
