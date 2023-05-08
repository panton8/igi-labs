from lab3.serializers.serializer_json import Json
from lab3.serializers.serializer_xml import Xml


class Factory:
    @staticmethod
    def create_serializer(format):
        if format == ".json":
            return Json()
        elif format == ".xml":
            return Xml()
        else:
            raise Exception("Incorrect type of serialization")
