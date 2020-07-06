from enum import Enum

class Nodes(Enum):
    (#vars
     LOADNAME,
     LOADATTR,
     STOREATTR,
     STORENAME,
     #literals
     BUILDTUPLE,
     BUILDMAP,
     BUILDSET,
     BUILDLIST,
     LOADCONST,
     #pop
     POPLAST,
     #function
     CALLFUNC,
     #operations
     OP,
     CMP,
    ) = range(13)
