__all__ = ("UserIsLoggedInError", "PlayerNotFoundError")


class UserIsLoggedInError(Exception):
    pass


class PlayerNotFoundError(Exception):
    pass
