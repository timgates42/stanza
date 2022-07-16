from collections import namedtuple
from enum import Enum

class XPOSType(Enum):
    XPOS     = 1
    WORD     = 2

XPOSDescription = namedtuple('XPOSDescription', ['xpos_type', 'sep'])

def build_xpos_vocab(description, data, shorthand):
    if description.xpos_type is XPOSType.WORD:
        return WordVocab(data, shorthand, idx=2, ignore=["_"])

    return XPOSVocab(data, shorthand, idx=2, sep=description.sep)
