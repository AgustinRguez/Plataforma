import enum

class UserEnum(str, enum.Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"