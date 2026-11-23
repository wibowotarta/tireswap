# === Stage 14: Постраничный вывод ===
# Project: TireSwap
"""Pagination helper for the TireSwap kit list."""

from typing import Iterator, List, Sequence, Tuple


class Page:
    """A single page of kit records with navigation metadata."""

    def __init__(self, kits: Sequence, page_number: int, page_size: int,
                 total: int):
        self.kits = list(kits)
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    @property
    def total_pages(self) -> int:
        if self.page_size <= 0:
            return 0
        return (self.total + self.page_size - 1) // self.page_size

    @property
    def has_next(self) -> bool:
        return self.page_number < self.total_pages

    @property
    def has_previous(self) -> bool:
        return self.page_number > 1

    def __repr__(self) -> str:
        return (f"Page(page_number={self.page_number}, page_size={self.page_size}, "
                f"total={self.total}, total_pages={self.total_pages})")


def paginate(kits: Sequence, page_number: int = 1, page_size: int = 10) -> Page:
    """Return a Page for the given kit collection."""
    page_size = max(1, page_size)
    total = len(kits)
    total_pages = max(1, (total + page_size - 1) // page_size)
    page_number = max(1, min(page_number, total_pages))
    start = (page_number - 1) * page_size
    end = start + page_size
    return Page(kits[start:end], page_number, page_size, total)


def paginated_iter(kits: Sequence, page_size: int = 10) -> Iterator[Page]:
    """Yield every page of the kit collection."""
    total_pages = max(1, (len(kits) + page_size - 1) // page_size)
    for number in range(1, total_pages + 1):
        yield paginate(kits, number, page_size)


def page_range(page_number: int, page_size: int) -> Tuple[int, int, int, int]:
    """Compute the inclusive index slice for a page."""
    page_size = max(1, page_size)
    total_pages = max(1, (page_number * page_size + page_size - 1) // page_size)
    clamped = max(1, min(page_number, total_pages))
    start = (clamped - 1) * page_size
    end = start + page_size
    return start, end, clamped, total_pages


def format_summary(page: Page) -> str:
    """Return a human-readable pagination summary."""
    return (f"Page {page.page_number} of {page.total_pages} "
            f"({page.page_size} of {page.total} kits)")
