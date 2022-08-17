from datetime import date


class Document:
    def __init__(self, authors=[], date=date.today()) -> None:
        self._authors = authors
        self._date = date
    def __str__(self) -> str:
        return f'Document: Authors: {self._authors}, Date: {self._date}'
    def get_authors(self) -> list:
        return self._authors
    def get_date(self) -> date:
        return self._date
    def add_author(self, author: str) -> None:
        self._authors.append(author)

class EMail(Document):
    def __init__(self, to, subject="", authors=[], date=date.today()) -> None:
        super().__init__(authors, date)
        self._to = to
        self._subject = subject
    def get_to(self) -> str:
        return self._to
    def get_subject(self) -> str:
        return self._subject
    
    def __str__(self) -> str:
        return f"Email: to: {self._to}, subject: {self._subject}, authors: {self._authors}, date: {self._date}"

class Book(Document):
    def __init__(self, title, authors=[], date=date.today()) -> None:
        super().__init__(authors, date)
        self._title = title
    def get_title(self) -> str:
        return self._title
    def __str__(self) -> str:
        return f'Book: Title: {self._title} - {super().__str__()}'
