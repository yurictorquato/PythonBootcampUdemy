class Question:
    def __init__(self, text: str, answer: bool) -> None:
        self._text = text
        self._answer = answer

    @property
    def text(self) -> str:
        return self._text

    @property
    def answer(self) -> bool:
        return self._answer
