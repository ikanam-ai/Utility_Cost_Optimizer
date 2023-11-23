from collections import namedtuple

from .default import main as default

Page = namedtuple("Page", "title method")

pages: dict[str, Page] = {
    'archive': Page(title="База", method=default),
}
