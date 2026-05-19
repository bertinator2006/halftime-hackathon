class ServerException(Exception):
    """Base class for server exceptions."""
    def __init__(self, error_code: int, message: str):
        super().__init__(message)
        self.error_code = error_code

class SessionNotFoundException(ServerException):
    """Exception raised when a session is not found."""
    def __init__(self, session_id: str):
        message = f"No session found with ID: {session_id}"
        super().__init__(error_code=400, message=message)

class NotFoundException(ServerException):
    """Exception raised when an item is not found."""
    def __init__(self, item_id: str):
        message = f"No item found with ID: {item_id}"
        super().__init__(error_code=401, message=message)

class InvalidInputException(ServerException):
    """Exception raised when invalid input is provided."""
    def __init__(self, message: str):
        super().__init__(error_code=402, message=message)
    