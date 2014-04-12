class SendGridError(Exception):
    pass


class SendGridClientError(SendGridError):
    pass


class SendGridServerError(SendGridError):
    pass
