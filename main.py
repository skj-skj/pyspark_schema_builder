from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType, ArrayType, BooleanType
)
import json
import re

sql_type_map = {
    'str': StringType(),
    'int': IntegerType(),
    'bool': BooleanType()
}

def schema_builder(schema_info: dict):
    fields = []
    correct_type = None
    correct_name = None
    for field_name, field_type in schema_info.items():
        try:
            correct_name = re.fullmatch(r'(\w+)!*', field_name).group(1)
        except AttributeError as err:
            raise ValueError(f"Something Wrong With the Field Name: {field_name}")
        if isinstance(field_type, str):
            temp_type = re.fullmatch(r'(\w+)\[?\]?', field_type).group(1)
            if temp_type in sql_type_map.keys():
                sql_type = sql_type_map[temp_type]
                correct_type = ArrayType(sql_type) if "[]" in field_type else sql_type
        elif isinstance(field_type, dict) or isinstance(field_type, list):
            correct_type = ArrayType(schema_builder(field_type[0])) if isinstance(field_type, list) else schema_builder(field_type)
        if correct_type == None:
            raise ValueError(f"Given type is not supported yet:\n Field Name: {field_name}, Field Type: {field_type}")
        fields.append(
            StructField(
                correct_name,
                correct_type,
                field_name[-1] != "!"
            )
        )
    return StructType(fields)