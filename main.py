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
    for field_name, field_type in schema_info.items():
        if isinstance(field_type, str):
            temp_type = re.fullmatch(r"!*(\w+)\[?\]?", field_type).group(1)
            if temp_type in ['str', 'int', 'bool']:
                sql_type = sql_type_map[temp_type]
                correct_type = ArrayType(sql_type) if "[]" in field_type else sql_type
        elif isinstance(field_type, dict) or isinstance(field_type, list):
            correct_type = ArrayType(schema_builder(field_type[0])) if isinstance(field_type, list) else schema_builder(field_type)

        fields.append(
            StructField(
                field_name,
                correct_type,
                field_name[-1] != "!"
            )
        )
    return StructType(fields)