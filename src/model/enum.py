import enum

class UserEnum(str, enum.Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

class TypeEnum(str, enum.Enum):
    A = "A"
    B = "B"
    C = "C"
    M = "M"
    E = "E"
    T = "T"

class StatusEnum(str, enum.Enum):
    completed = "complete"
    cancel = "cancelled"
    in_process = "in process"