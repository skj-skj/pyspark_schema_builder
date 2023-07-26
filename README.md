# pyspark_schema_builder
Pyspark Schema Generation


# Json Syntax
```json
{
    "field_name": "field_type",
    "non_nullable_field!": "field_type",
    "array_field": "field_type[]",
    "struct_field": {
        "field_name": "field_type"
    },
    "struct_array_field": [{
        "field_name": "field_type"
    }]
}
```

# Field Types:
```
"str" = StringType()
"int" = IntergerType()
"bool" = BooleanType()
```

Example:
```json
{
    "foo": "str",
    "bar!": "int",
    "veggies": "str[]",
    "area": {
        "height": "str",
        "width": "str"
    },
    "graphPlot": [{
        "x": "int",
        "y": "int"
    }]
}
```

in the above example:<br>
1. `foo` is field of `StringType()`
2. `bar` is non nullable field of `IntergerType()`, to make any field non nullable add `!` (Bang) at the end of field name
3. `veggies` is field of `ArrayType(StringType())`, to make field ArrayType add `[]` at the end (except for StructType)
4. `area` is field of `StructType()`, to make any field StructType add it again as a json/dict
5. `graphPlot` is field of `ArrayType(StructType())`, to make ArrayType of StructType enclose the json/dict structure of StructType with `[` `]` Square Brackets.

# TODO: Better Docs
