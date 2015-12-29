class BlockProperty():
    def __init__(self, property_name):
        self.all_values = []
        self.property_name = property_name
        self.block_definition = None # attached later

class IntegerProperty(BlockProperty):
    def value(self, i, usage_str):
        v = IntegerPropertyWithValue(self, i, usage_str)
        self.all_values.append(v)
        return v

    def get_value_by_str(self, str_value):
        for v in self.all_values:
            if v.value == int(str_value):
                return v


class EnumProperty(BlockProperty):
    def value(self, enum_name, usage_str):
        v = EnumPropertyWithValue(self, enum_name, usage_str)
        self.all_values.append(v)
        return v

    def get_value_by_str(self, str_value):
        for v in self.all_values:
            if v.value == str_value:
                return v

class BooleanProperty(BlockProperty):
    def value(self, b, usage_str):
        v = BooleanPropertyWithValue(self, b, usage_str)
        self.all_values.append(v)
        return v

    def get_value_by_str(self, str_value):
        for v in self.all_values:
            if 'false' == str_value and v.value == False:
                return v
            elif 'true' == str_value and v.value == True:
                return v


class PropertyWithValue():
    def __str__(self):
        return str(self.block_property.block_definition) + "." + self.value_str

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.value == other.value

class IntegerPropertyWithValue(PropertyWithValue):
    def __init__(self, block_property, value, value_str):
        self.block_property = block_property
        self.value = value
        self.value_str = value_str

    def add_to_dict(self, d):
        d[self.block_property.property_name] = str(self.value)

class BooleanPropertyWithValue(PropertyWithValue):
    def __init__(self, block_property, value, value_str):
        self.block_property = block_property
        self.value = value
        self.value_str = value_str

    def add_to_dict(self, d):
        if self.value == True:
            d[self.block_property.property_name] = "true"
        else:
            d[self.block_property.property_name] = "false"

class EnumPropertyWithValue(PropertyWithValue):
    def __init__(self, block_property, value, value_str):
        self.block_property = block_property
        self.value = value
        self.value_str = value_str

    def add_to_dict(self, d):
        d[self.block_property.property_name] = self.value
