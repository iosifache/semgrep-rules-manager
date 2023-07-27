class SemgrepRulesManagerException(Exception):
    """Generic semgrep-rules-manager exception"""

    message: str

    def __init__(self) -> None:
        if self.__doc__:
            message = self.__doc__
        else:
            message = None

        super().__init__(message)
