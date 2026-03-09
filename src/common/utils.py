def pretty_exception(message: str, exception: Exception) -> str:
    return f'{message}: <{exception.__class__.__name__}>: {exception}'