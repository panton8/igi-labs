import inspect
from lab3.serializers.consts import nonetype, moduletype, codetype, celltype, \
                                    functype, bldinfunctype, \
                                    mapproxytype, wrapdesctype, metdesctype, getsetdesctype, \
                                    CODE_PROPS, UNIQUE_TYPES


class PackingTool:
    TYPE_KW = "type"
    SOURCE_KW = "source"

    CODE_KW = "__code__"
    GLOBALS_KW = functype.__globals__.__name__
    NAME_KW = "__name__"
    DEFAULTS_KW = "__defaults__"
    CLOSURE_KW = functype.__closure__.__name__

    BASES_KW = "__bases__"
    DICT_KW = "__dict__"

    CLASS_KW = "__class__"

    OBJECT_KW = "object"

