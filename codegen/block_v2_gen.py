import os
import sys
import json
import string
import types

INDENT = "    "

this_dir = os.path.dirname(os.path.realpath(__file__))
blocks = json.loads(open(os.path.join(this_dir, "block_metadata.json")).read())

target_definition_file = os.path.join(this_dir, "../mcgamedata/block_definition.py")
target_block_file = os.path.join(this_dir, "../mcgamedata/block.py")

block_definition_lines = [
    "from block_property import EnumProperty, IntegerProperty, BooleanProperty",
    "",
    "class BlockDefinition():",
    INDENT + "def __str__(self):",
    INDENT + INDENT + "return self.short_usage_str",
    ""
]

# {
#        "id": 145,
#        "name": "minecraft:anvil",
#        "properties": [
#            {
#                "type": "integer",
#                "name": "damage",
#                "value": 0,
#                "possible_values": [
#                    0,
#                    1,
#                    2
#                ]
#            },
#            {
#                "type": "enum",
#                "name": "facing",
#                "value": "north",
#                "possible_values": [
#                    "north",
#                    "south",
#                    "west",
#                    "east"
#                ]
#            }
#        ]
#    },

all_blocks = []

for block in blocks:
    block_id = block["id"]
    lowercase_block_name = block["name"].replace("minecraft:", "")
    uppercase_block_name = lowercase_block_name.upper()
    upper_camel_block_name = string.capwords(lowercase_block_name, "_").replace("_", "")

    all_blocks.append({'upper':uppercase_block_name, 'camel':upper_camel_block_name})

    block_definition_lines.extend([
        "",
        "class " + upper_camel_block_name + "(BlockDefinition):",
        INDENT + "def __init__(self):",
        INDENT + INDENT + "self.id = " + str(block_id),
        INDENT + INDENT + "self.name = '" + lowercase_block_name + "'",
        INDENT + INDENT + "self.short_usage_str = 'block." + uppercase_block_name + "'",
        "",
        INDENT + "ALL_PROPERTIES = []",
        ""
    ])

    for p in block["properties"]:
        lowercase_property_name = p["name"]
        uppercase_property_name = lowercase_property_name.upper()
        capitalized_type = string.capwords(p["type"])

        property_const = "PROPERTY_" + uppercase_property_name
        block_definition_lines.append(
            INDENT + property_const + " = " +
                capitalized_type + "Property('" + lowercase_property_name + "'); ALL_PROPERTIES.append(" + property_const + ")")

        property_value_lines = []
        max_property_value_name_length = 0

        for v in p["possible_values"]:
            uppercase_value = str(v).upper()
            const_name = uppercase_property_name + "_" + uppercase_value
            value = "PROPERTY_" + uppercase_property_name + ".value("
            if type(v) is types.StringType or type(v) is types.UnicodeType:
                value += "'" + v + "'"
            else:
                value += str(v)
            value += ", '" + const_name + "'"
            value += ")"
            property_value_lines.append([INDENT + const_name, value])
            if len(INDENT + const_name) > max_property_value_name_length:
                max_property_value_name_length = len(INDENT + const_name)

        for line in property_value_lines:
            value_line = line[0].ljust(max_property_value_name_length) + " = " + line[1]
            block_definition_lines.append(value_line)

        block_definition_lines.append("")

body = "\n".join(block_definition_lines) + "\n"
print body
f = open(target_definition_file, 'w')
f.write(body)
f.close()

block_lines = [
    "import block_definition",
    "",
    "ALL = []",
    ""
]

max_block_name_length = 0
for block in all_blocks:
    if len(block['upper']) > max_block_name_length:
        max_block_name_length = len(block['upper'])

for block in all_blocks:
    block_lines.append(block['upper'].ljust(max_block_name_length) + " = block_definition." + \
        block['camel'] + "(); ALL.append(" + block['upper'] + ")")

block_lines.extend([
    "",
    "for block_def in ALL:",
    INDENT + "for block_property in block_def.ALL_PROPERTIES:",
    INDENT + INDENT + "block_property.block_definition = block_def",
    ""
])

body = "\n".join(block_lines) + "\n"
print body
f = open(target_block_file, 'w')
f.write(body)
f.close()
