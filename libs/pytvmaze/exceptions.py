import sys

class BaseError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if sys.version_info > (3,):
            return self.value
        else:
            return unicode(self.value).encode('utf-8')


class ShowNotFound(BaseError):
    pass


class IDNotFound(BaseError):
    pass


class ScheduleNotFound(BaseError):
    pass


class EpisodeNotFound(BaseError):
    pass


class NoEpisodesForAirdate(BaseError):
    pass


class CastNotFound(BaseError):
    pass


class ShowIndexError(BaseError):
    pass


class PersonNotFound(BaseError):
    pass


class CreditsNotFound(BaseError):
    pass


class UpdateNotFound(BaseError):
    pass


class AKASNotFound(BaseError):
    pass


class SeasonNotFound(BaseError):
    pass


class GeneralError(BaseError):
    pass


class MissingParameters(BaseError):
    pass


class SeasonNotFound(BaseError):
    pass


class IllegalAirDate(BaseError):
    pass


class ConnectionError(BaseError):
    pass


class BadRequest(BaseError):
    pass
