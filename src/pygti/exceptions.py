class GTIError(Exception):
    """An exception occured while using the GTI API."""

    def __init__(self, return_code, error_text, error_dev_info):
        self.return_code = return_code
        self.error_text = error_text
        self.error_dev_info = error_dev_info
