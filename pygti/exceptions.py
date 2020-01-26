class GTIError(Exception):
    """An exception occured while using the GTI API."""

    def __init__(self, return_code, error_text, error_dev_info):
        self.return_code = return_code
        self.error_text = error_text
        self.error_dev_info = error_dev_info


class CannotConnect(Exception):
    """Exception raised if connection could not be established to host."""

    pass


class InvalidAuth(GTIError):
    """Exception raised if credentials are incorrent."""

    pass


class CheckNameTooMany(GTIError):
    """Check Name returned too many hits.

    Precise search term."""

    pass


class CommunicationError(GTIError):
    """Error while connecting to backend."""

    pass


class RouteError(GTIError):
    """Route could not be calculated."""

    pass
