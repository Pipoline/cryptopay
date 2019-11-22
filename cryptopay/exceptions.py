
class ApiException(Exception):
    type = None
    code = None
    param = None


class Unauthorized(ApiException):
    pass


class BadRequest(ApiException):
    pass


class RequestFailed(ApiException):
    pass


class NotFound(ApiException):
    pass


class Conflict(ApiException):
    pass


class TooManyRequests(ApiException):
    pass


class UnknownError(ApiException):
    pass
