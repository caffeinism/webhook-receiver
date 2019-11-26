import enum

class Event(enum.Enum):
    # COMMON
    PUSH = enum.auto(),
    ISSUE = enum.auto(),
    PULL_REQ = enum.auto(),
    CREATE = enum.auto(),
    WIKI = enum.auto(),

    # GITHUB
    FORK = enum.auto(),
    PING = enum.auto(),

    # GITLAB
    COMMENT = enum.auto(),
    PIPELINE = enum.auto(),