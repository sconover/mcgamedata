from block_property import EnumProperty, IntegerProperty, BooleanProperty

class BlockDefinition():
    def __str__(self):
        return self.short_usage_str


class AcaciaDoor(BlockDefinition):
    def __init__(self):
        self.id = 196
        self.name = 'acacia_door'
        self.short_usage_str = 'block.ACACIA_DOOR'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_UPPER = PROPERTY_HALF.value('upper', 'HALF_UPPER')
    HALF_LOWER = PROPERTY_HALF.value('lower', 'HALF_LOWER')

    PROPERTY_HINGE = EnumProperty('hinge'); ALL_PROPERTIES.append(PROPERTY_HINGE)
    HINGE_LEFT  = PROPERTY_HINGE.value('left', 'HINGE_LEFT')
    HINGE_RIGHT = PROPERTY_HINGE.value('right', 'HINGE_RIGHT')

    PROPERTY_OPEN = BooleanProperty('open'); ALL_PROPERTIES.append(PROPERTY_OPEN)
    OPEN_TRUE  = PROPERTY_OPEN.value(True, 'OPEN_TRUE')
    OPEN_FALSE = PROPERTY_OPEN.value(False, 'OPEN_FALSE')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class AcaciaFence(BlockDefinition):
    def __init__(self):
        self.id = 192
        self.name = 'acacia_fence'
        self.short_usage_str = 'block.ACACIA_FENCE'

    ALL_PROPERTIES = []

    PROPERTY_EAST = BooleanProperty('east'); ALL_PROPERTIES.append(PROPERTY_EAST)
    EAST_TRUE  = PROPERTY_EAST.value(True, 'EAST_TRUE')
    EAST_FALSE = PROPERTY_EAST.value(False, 'EAST_FALSE')

    PROPERTY_NORTH = BooleanProperty('north'); ALL_PROPERTIES.append(PROPERTY_NORTH)
    NORTH_TRUE  = PROPERTY_NORTH.value(True, 'NORTH_TRUE')
    NORTH_FALSE = PROPERTY_NORTH.value(False, 'NORTH_FALSE')

    PROPERTY_SOUTH = BooleanProperty('south'); ALL_PROPERTIES.append(PROPERTY_SOUTH)
    SOUTH_TRUE  = PROPERTY_SOUTH.value(True, 'SOUTH_TRUE')
    SOUTH_FALSE = PROPERTY_SOUTH.value(False, 'SOUTH_FALSE')

    PROPERTY_WEST = BooleanProperty('west'); ALL_PROPERTIES.append(PROPERTY_WEST)
    WEST_TRUE  = PROPERTY_WEST.value(True, 'WEST_TRUE')
    WEST_FALSE = PROPERTY_WEST.value(False, 'WEST_FALSE')


class AcaciaFenceGate(BlockDefinition):
    def __init__(self):
        self.id = 187
        self.name = 'acacia_fence_gate'
        self.short_usage_str = 'block.ACACIA_FENCE_GATE'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_IN_WALL = BooleanProperty('in_wall'); ALL_PROPERTIES.append(PROPERTY_IN_WALL)
    IN_WALL_TRUE  = PROPERTY_IN_WALL.value(True, 'IN_WALL_TRUE')
    IN_WALL_FALSE = PROPERTY_IN_WALL.value(False, 'IN_WALL_FALSE')

    PROPERTY_OPEN = BooleanProperty('open'); ALL_PROPERTIES.append(PROPERTY_OPEN)
    OPEN_TRUE  = PROPERTY_OPEN.value(True, 'OPEN_TRUE')
    OPEN_FALSE = PROPERTY_OPEN.value(False, 'OPEN_FALSE')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class AcaciaStairs(BlockDefinition):
    def __init__(self):
        self.id = 163
        self.name = 'acacia_stairs'
        self.short_usage_str = 'block.ACACIA_STAIRS'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_SHAPE = EnumProperty('shape'); ALL_PROPERTIES.append(PROPERTY_SHAPE)
    SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight', 'SHAPE_STRAIGHT')
    SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left', 'SHAPE_INNER_LEFT')
    SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right', 'SHAPE_INNER_RIGHT')
    SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left', 'SHAPE_OUTER_LEFT')
    SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right', 'SHAPE_OUTER_RIGHT')


class ActivatorRail(BlockDefinition):
    def __init__(self):
        self.id = 157
        self.name = 'activator_rail'
        self.short_usage_str = 'block.ACTIVATOR_RAIL'

    ALL_PROPERTIES = []

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')

    PROPERTY_SHAPE = EnumProperty('shape'); ALL_PROPERTIES.append(PROPERTY_SHAPE)
    SHAPE_NORTH_SOUTH     = PROPERTY_SHAPE.value('north_south', 'SHAPE_NORTH_SOUTH')
    SHAPE_EAST_WEST       = PROPERTY_SHAPE.value('east_west', 'SHAPE_EAST_WEST')
    SHAPE_ASCENDING_EAST  = PROPERTY_SHAPE.value('ascending_east', 'SHAPE_ASCENDING_EAST')
    SHAPE_ASCENDING_WEST  = PROPERTY_SHAPE.value('ascending_west', 'SHAPE_ASCENDING_WEST')
    SHAPE_ASCENDING_NORTH = PROPERTY_SHAPE.value('ascending_north', 'SHAPE_ASCENDING_NORTH')
    SHAPE_ASCENDING_SOUTH = PROPERTY_SHAPE.value('ascending_south', 'SHAPE_ASCENDING_SOUTH')


class Air(BlockDefinition):
    def __init__(self):
        self.id = 0
        self.name = 'air'
        self.short_usage_str = 'block.AIR'

    ALL_PROPERTIES = []


class Anvil(BlockDefinition):
    def __init__(self):
        self.id = 145
        self.name = 'anvil'
        self.short_usage_str = 'block.ANVIL'

    ALL_PROPERTIES = []

    PROPERTY_DAMAGE = IntegerProperty('damage'); ALL_PROPERTIES.append(PROPERTY_DAMAGE)
    DAMAGE_0 = PROPERTY_DAMAGE.value(0, 'DAMAGE_0')
    DAMAGE_1 = PROPERTY_DAMAGE.value(1, 'DAMAGE_1')
    DAMAGE_2 = PROPERTY_DAMAGE.value(2, 'DAMAGE_2')

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class Barrier(BlockDefinition):
    def __init__(self):
        self.id = 166
        self.name = 'barrier'
        self.short_usage_str = 'block.BARRIER'

    ALL_PROPERTIES = []


class Beacon(BlockDefinition):
    def __init__(self):
        self.id = 138
        self.name = 'beacon'
        self.short_usage_str = 'block.BEACON'

    ALL_PROPERTIES = []


class Bed(BlockDefinition):
    def __init__(self):
        self.id = 26
        self.name = 'bed'
        self.short_usage_str = 'block.BED'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_OCCUPIED = BooleanProperty('occupied'); ALL_PROPERTIES.append(PROPERTY_OCCUPIED)
    OCCUPIED_TRUE  = PROPERTY_OCCUPIED.value(True, 'OCCUPIED_TRUE')
    OCCUPIED_FALSE = PROPERTY_OCCUPIED.value(False, 'OCCUPIED_FALSE')

    PROPERTY_PART = EnumProperty('part'); ALL_PROPERTIES.append(PROPERTY_PART)
    PART_HEAD = PROPERTY_PART.value('head', 'PART_HEAD')
    PART_FOOT = PROPERTY_PART.value('foot', 'PART_FOOT')


class Bedrock(BlockDefinition):
    def __init__(self):
        self.id = 7
        self.name = 'bedrock'
        self.short_usage_str = 'block.BEDROCK'

    ALL_PROPERTIES = []


class BirchDoor(BlockDefinition):
    def __init__(self):
        self.id = 194
        self.name = 'birch_door'
        self.short_usage_str = 'block.BIRCH_DOOR'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_UPPER = PROPERTY_HALF.value('upper', 'HALF_UPPER')
    HALF_LOWER = PROPERTY_HALF.value('lower', 'HALF_LOWER')

    PROPERTY_HINGE = EnumProperty('hinge'); ALL_PROPERTIES.append(PROPERTY_HINGE)
    HINGE_LEFT  = PROPERTY_HINGE.value('left', 'HINGE_LEFT')
    HINGE_RIGHT = PROPERTY_HINGE.value('right', 'HINGE_RIGHT')

    PROPERTY_OPEN = BooleanProperty('open'); ALL_PROPERTIES.append(PROPERTY_OPEN)
    OPEN_TRUE  = PROPERTY_OPEN.value(True, 'OPEN_TRUE')
    OPEN_FALSE = PROPERTY_OPEN.value(False, 'OPEN_FALSE')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class BirchFence(BlockDefinition):
    def __init__(self):
        self.id = 189
        self.name = 'birch_fence'
        self.short_usage_str = 'block.BIRCH_FENCE'

    ALL_PROPERTIES = []

    PROPERTY_EAST = BooleanProperty('east'); ALL_PROPERTIES.append(PROPERTY_EAST)
    EAST_TRUE  = PROPERTY_EAST.value(True, 'EAST_TRUE')
    EAST_FALSE = PROPERTY_EAST.value(False, 'EAST_FALSE')

    PROPERTY_NORTH = BooleanProperty('north'); ALL_PROPERTIES.append(PROPERTY_NORTH)
    NORTH_TRUE  = PROPERTY_NORTH.value(True, 'NORTH_TRUE')
    NORTH_FALSE = PROPERTY_NORTH.value(False, 'NORTH_FALSE')

    PROPERTY_SOUTH = BooleanProperty('south'); ALL_PROPERTIES.append(PROPERTY_SOUTH)
    SOUTH_TRUE  = PROPERTY_SOUTH.value(True, 'SOUTH_TRUE')
    SOUTH_FALSE = PROPERTY_SOUTH.value(False, 'SOUTH_FALSE')

    PROPERTY_WEST = BooleanProperty('west'); ALL_PROPERTIES.append(PROPERTY_WEST)
    WEST_TRUE  = PROPERTY_WEST.value(True, 'WEST_TRUE')
    WEST_FALSE = PROPERTY_WEST.value(False, 'WEST_FALSE')


class BirchFenceGate(BlockDefinition):
    def __init__(self):
        self.id = 184
        self.name = 'birch_fence_gate'
        self.short_usage_str = 'block.BIRCH_FENCE_GATE'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_IN_WALL = BooleanProperty('in_wall'); ALL_PROPERTIES.append(PROPERTY_IN_WALL)
    IN_WALL_TRUE  = PROPERTY_IN_WALL.value(True, 'IN_WALL_TRUE')
    IN_WALL_FALSE = PROPERTY_IN_WALL.value(False, 'IN_WALL_FALSE')

    PROPERTY_OPEN = BooleanProperty('open'); ALL_PROPERTIES.append(PROPERTY_OPEN)
    OPEN_TRUE  = PROPERTY_OPEN.value(True, 'OPEN_TRUE')
    OPEN_FALSE = PROPERTY_OPEN.value(False, 'OPEN_FALSE')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class BirchStairs(BlockDefinition):
    def __init__(self):
        self.id = 135
        self.name = 'birch_stairs'
        self.short_usage_str = 'block.BIRCH_STAIRS'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_SHAPE = EnumProperty('shape'); ALL_PROPERTIES.append(PROPERTY_SHAPE)
    SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight', 'SHAPE_STRAIGHT')
    SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left', 'SHAPE_INNER_LEFT')
    SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right', 'SHAPE_INNER_RIGHT')
    SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left', 'SHAPE_OUTER_LEFT')
    SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right', 'SHAPE_OUTER_RIGHT')


class Bookshelf(BlockDefinition):
    def __init__(self):
        self.id = 47
        self.name = 'bookshelf'
        self.short_usage_str = 'block.BOOKSHELF'

    ALL_PROPERTIES = []


class BrewingStand(BlockDefinition):
    def __init__(self):
        self.id = 117
        self.name = 'brewing_stand'
        self.short_usage_str = 'block.BREWING_STAND'

    ALL_PROPERTIES = []

    PROPERTY_HAS_BOTTLE_0 = BooleanProperty('has_bottle_0'); ALL_PROPERTIES.append(PROPERTY_HAS_BOTTLE_0)
    HAS_BOTTLE_0_TRUE  = PROPERTY_HAS_BOTTLE_0.value(True, 'HAS_BOTTLE_0_TRUE')
    HAS_BOTTLE_0_FALSE = PROPERTY_HAS_BOTTLE_0.value(False, 'HAS_BOTTLE_0_FALSE')

    PROPERTY_HAS_BOTTLE_1 = BooleanProperty('has_bottle_1'); ALL_PROPERTIES.append(PROPERTY_HAS_BOTTLE_1)
    HAS_BOTTLE_1_TRUE  = PROPERTY_HAS_BOTTLE_1.value(True, 'HAS_BOTTLE_1_TRUE')
    HAS_BOTTLE_1_FALSE = PROPERTY_HAS_BOTTLE_1.value(False, 'HAS_BOTTLE_1_FALSE')

    PROPERTY_HAS_BOTTLE_2 = BooleanProperty('has_bottle_2'); ALL_PROPERTIES.append(PROPERTY_HAS_BOTTLE_2)
    HAS_BOTTLE_2_TRUE  = PROPERTY_HAS_BOTTLE_2.value(True, 'HAS_BOTTLE_2_TRUE')
    HAS_BOTTLE_2_FALSE = PROPERTY_HAS_BOTTLE_2.value(False, 'HAS_BOTTLE_2_FALSE')


class BrickBlock(BlockDefinition):
    def __init__(self):
        self.id = 45
        self.name = 'brick_block'
        self.short_usage_str = 'block.BRICK_BLOCK'

    ALL_PROPERTIES = []


class BrickStairs(BlockDefinition):
    def __init__(self):
        self.id = 108
        self.name = 'brick_stairs'
        self.short_usage_str = 'block.BRICK_STAIRS'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_SHAPE = EnumProperty('shape'); ALL_PROPERTIES.append(PROPERTY_SHAPE)
    SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight', 'SHAPE_STRAIGHT')
    SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left', 'SHAPE_INNER_LEFT')
    SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right', 'SHAPE_INNER_RIGHT')
    SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left', 'SHAPE_OUTER_LEFT')
    SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right', 'SHAPE_OUTER_RIGHT')


class BrownMushroom(BlockDefinition):
    def __init__(self):
        self.id = 39
        self.name = 'brown_mushroom'
        self.short_usage_str = 'block.BROWN_MUSHROOM'

    ALL_PROPERTIES = []


class BrownMushroomBlock(BlockDefinition):
    def __init__(self):
        self.id = 99
        self.name = 'brown_mushroom_block'
        self.short_usage_str = 'block.BROWN_MUSHROOM_BLOCK'

    ALL_PROPERTIES = []

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_NORTH_WEST  = PROPERTY_VARIANT.value('north_west', 'VARIANT_NORTH_WEST')
    VARIANT_NORTH       = PROPERTY_VARIANT.value('north', 'VARIANT_NORTH')
    VARIANT_NORTH_EAST  = PROPERTY_VARIANT.value('north_east', 'VARIANT_NORTH_EAST')
    VARIANT_WEST        = PROPERTY_VARIANT.value('west', 'VARIANT_WEST')
    VARIANT_CENTER      = PROPERTY_VARIANT.value('center', 'VARIANT_CENTER')
    VARIANT_EAST        = PROPERTY_VARIANT.value('east', 'VARIANT_EAST')
    VARIANT_SOUTH_WEST  = PROPERTY_VARIANT.value('south_west', 'VARIANT_SOUTH_WEST')
    VARIANT_SOUTH       = PROPERTY_VARIANT.value('south', 'VARIANT_SOUTH')
    VARIANT_SOUTH_EAST  = PROPERTY_VARIANT.value('south_east', 'VARIANT_SOUTH_EAST')
    VARIANT_STEM        = PROPERTY_VARIANT.value('stem', 'VARIANT_STEM')
    VARIANT_ALL_INSIDE  = PROPERTY_VARIANT.value('all_inside', 'VARIANT_ALL_INSIDE')
    VARIANT_ALL_OUTSIDE = PROPERTY_VARIANT.value('all_outside', 'VARIANT_ALL_OUTSIDE')
    VARIANT_ALL_STEM    = PROPERTY_VARIANT.value('all_stem', 'VARIANT_ALL_STEM')


class Cactus(BlockDefinition):
    def __init__(self):
        self.id = 81
        self.name = 'cactus'
        self.short_usage_str = 'block.CACTUS'

    ALL_PROPERTIES = []

    PROPERTY_AGE = IntegerProperty('age'); ALL_PROPERTIES.append(PROPERTY_AGE)
    AGE_0  = PROPERTY_AGE.value(0, 'AGE_0')
    AGE_1  = PROPERTY_AGE.value(1, 'AGE_1')
    AGE_2  = PROPERTY_AGE.value(2, 'AGE_2')
    AGE_3  = PROPERTY_AGE.value(3, 'AGE_3')
    AGE_4  = PROPERTY_AGE.value(4, 'AGE_4')
    AGE_5  = PROPERTY_AGE.value(5, 'AGE_5')
    AGE_6  = PROPERTY_AGE.value(6, 'AGE_6')
    AGE_7  = PROPERTY_AGE.value(7, 'AGE_7')
    AGE_8  = PROPERTY_AGE.value(8, 'AGE_8')
    AGE_9  = PROPERTY_AGE.value(9, 'AGE_9')
    AGE_10 = PROPERTY_AGE.value(10, 'AGE_10')
    AGE_11 = PROPERTY_AGE.value(11, 'AGE_11')
    AGE_12 = PROPERTY_AGE.value(12, 'AGE_12')
    AGE_13 = PROPERTY_AGE.value(13, 'AGE_13')
    AGE_14 = PROPERTY_AGE.value(14, 'AGE_14')
    AGE_15 = PROPERTY_AGE.value(15, 'AGE_15')


class Cake(BlockDefinition):
    def __init__(self):
        self.id = 92
        self.name = 'cake'
        self.short_usage_str = 'block.CAKE'

    ALL_PROPERTIES = []

    PROPERTY_BITES = IntegerProperty('bites'); ALL_PROPERTIES.append(PROPERTY_BITES)
    BITES_0 = PROPERTY_BITES.value(0, 'BITES_0')
    BITES_1 = PROPERTY_BITES.value(1, 'BITES_1')
    BITES_2 = PROPERTY_BITES.value(2, 'BITES_2')
    BITES_3 = PROPERTY_BITES.value(3, 'BITES_3')
    BITES_4 = PROPERTY_BITES.value(4, 'BITES_4')
    BITES_5 = PROPERTY_BITES.value(5, 'BITES_5')
    BITES_6 = PROPERTY_BITES.value(6, 'BITES_6')


class Carpet(BlockDefinition):
    def __init__(self):
        self.id = 171
        self.name = 'carpet'
        self.short_usage_str = 'block.CARPET'

    ALL_PROPERTIES = []

    PROPERTY_COLOR = EnumProperty('color'); ALL_PROPERTIES.append(PROPERTY_COLOR)
    COLOR_WHITE      = PROPERTY_COLOR.value('white', 'COLOR_WHITE')
    COLOR_ORANGE     = PROPERTY_COLOR.value('orange', 'COLOR_ORANGE')
    COLOR_MAGENTA    = PROPERTY_COLOR.value('magenta', 'COLOR_MAGENTA')
    COLOR_LIGHT_BLUE = PROPERTY_COLOR.value('light_blue', 'COLOR_LIGHT_BLUE')
    COLOR_YELLOW     = PROPERTY_COLOR.value('yellow', 'COLOR_YELLOW')
    COLOR_LIME       = PROPERTY_COLOR.value('lime', 'COLOR_LIME')
    COLOR_PINK       = PROPERTY_COLOR.value('pink', 'COLOR_PINK')
    COLOR_GRAY       = PROPERTY_COLOR.value('gray', 'COLOR_GRAY')
    COLOR_SILVER     = PROPERTY_COLOR.value('silver', 'COLOR_SILVER')
    COLOR_CYAN       = PROPERTY_COLOR.value('cyan', 'COLOR_CYAN')
    COLOR_PURPLE     = PROPERTY_COLOR.value('purple', 'COLOR_PURPLE')
    COLOR_BLUE       = PROPERTY_COLOR.value('blue', 'COLOR_BLUE')
    COLOR_BROWN      = PROPERTY_COLOR.value('brown', 'COLOR_BROWN')
    COLOR_GREEN      = PROPERTY_COLOR.value('green', 'COLOR_GREEN')
    COLOR_RED        = PROPERTY_COLOR.value('red', 'COLOR_RED')
    COLOR_BLACK      = PROPERTY_COLOR.value('black', 'COLOR_BLACK')


class Carrots(BlockDefinition):
    def __init__(self):
        self.id = 141
        self.name = 'carrots'
        self.short_usage_str = 'block.CARROTS'

    ALL_PROPERTIES = []

    PROPERTY_AGE = IntegerProperty('age'); ALL_PROPERTIES.append(PROPERTY_AGE)
    AGE_0 = PROPERTY_AGE.value(0, 'AGE_0')
    AGE_1 = PROPERTY_AGE.value(1, 'AGE_1')
    AGE_2 = PROPERTY_AGE.value(2, 'AGE_2')
    AGE_3 = PROPERTY_AGE.value(3, 'AGE_3')
    AGE_4 = PROPERTY_AGE.value(4, 'AGE_4')
    AGE_5 = PROPERTY_AGE.value(5, 'AGE_5')
    AGE_6 = PROPERTY_AGE.value(6, 'AGE_6')
    AGE_7 = PROPERTY_AGE.value(7, 'AGE_7')


class Cauldron(BlockDefinition):
    def __init__(self):
        self.id = 118
        self.name = 'cauldron'
        self.short_usage_str = 'block.CAULDRON'

    ALL_PROPERTIES = []

    PROPERTY_LEVEL = IntegerProperty('level'); ALL_PROPERTIES.append(PROPERTY_LEVEL)
    LEVEL_0 = PROPERTY_LEVEL.value(0, 'LEVEL_0')
    LEVEL_1 = PROPERTY_LEVEL.value(1, 'LEVEL_1')
    LEVEL_2 = PROPERTY_LEVEL.value(2, 'LEVEL_2')
    LEVEL_3 = PROPERTY_LEVEL.value(3, 'LEVEL_3')


class Chest(BlockDefinition):
    def __init__(self):
        self.id = 54
        self.name = 'chest'
        self.short_usage_str = 'block.CHEST'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class Clay(BlockDefinition):
    def __init__(self):
        self.id = 82
        self.name = 'clay'
        self.short_usage_str = 'block.CLAY'

    ALL_PROPERTIES = []


class CoalBlock(BlockDefinition):
    def __init__(self):
        self.id = 173
        self.name = 'coal_block'
        self.short_usage_str = 'block.COAL_BLOCK'

    ALL_PROPERTIES = []


class CoalOre(BlockDefinition):
    def __init__(self):
        self.id = 16
        self.name = 'coal_ore'
        self.short_usage_str = 'block.COAL_ORE'

    ALL_PROPERTIES = []


class Cobblestone(BlockDefinition):
    def __init__(self):
        self.id = 4
        self.name = 'cobblestone'
        self.short_usage_str = 'block.COBBLESTONE'

    ALL_PROPERTIES = []


class CobblestoneWall(BlockDefinition):
    def __init__(self):
        self.id = 139
        self.name = 'cobblestone_wall'
        self.short_usage_str = 'block.COBBLESTONE_WALL'

    ALL_PROPERTIES = []

    PROPERTY_EAST = BooleanProperty('east'); ALL_PROPERTIES.append(PROPERTY_EAST)
    EAST_TRUE  = PROPERTY_EAST.value(True, 'EAST_TRUE')
    EAST_FALSE = PROPERTY_EAST.value(False, 'EAST_FALSE')

    PROPERTY_NORTH = BooleanProperty('north'); ALL_PROPERTIES.append(PROPERTY_NORTH)
    NORTH_TRUE  = PROPERTY_NORTH.value(True, 'NORTH_TRUE')
    NORTH_FALSE = PROPERTY_NORTH.value(False, 'NORTH_FALSE')

    PROPERTY_SOUTH = BooleanProperty('south'); ALL_PROPERTIES.append(PROPERTY_SOUTH)
    SOUTH_TRUE  = PROPERTY_SOUTH.value(True, 'SOUTH_TRUE')
    SOUTH_FALSE = PROPERTY_SOUTH.value(False, 'SOUTH_FALSE')

    PROPERTY_UP = BooleanProperty('up'); ALL_PROPERTIES.append(PROPERTY_UP)
    UP_TRUE  = PROPERTY_UP.value(True, 'UP_TRUE')
    UP_FALSE = PROPERTY_UP.value(False, 'UP_FALSE')

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_COBBLESTONE       = PROPERTY_VARIANT.value('cobblestone', 'VARIANT_COBBLESTONE')
    VARIANT_MOSSY_COBBLESTONE = PROPERTY_VARIANT.value('mossy_cobblestone', 'VARIANT_MOSSY_COBBLESTONE')

    PROPERTY_WEST = BooleanProperty('west'); ALL_PROPERTIES.append(PROPERTY_WEST)
    WEST_TRUE  = PROPERTY_WEST.value(True, 'WEST_TRUE')
    WEST_FALSE = PROPERTY_WEST.value(False, 'WEST_FALSE')


class Cocoa(BlockDefinition):
    def __init__(self):
        self.id = 127
        self.name = 'cocoa'
        self.short_usage_str = 'block.COCOA'

    ALL_PROPERTIES = []

    PROPERTY_AGE = IntegerProperty('age'); ALL_PROPERTIES.append(PROPERTY_AGE)
    AGE_0 = PROPERTY_AGE.value(0, 'AGE_0')
    AGE_1 = PROPERTY_AGE.value(1, 'AGE_1')
    AGE_2 = PROPERTY_AGE.value(2, 'AGE_2')

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class CommandBlock(BlockDefinition):
    def __init__(self):
        self.id = 137
        self.name = 'command_block'
        self.short_usage_str = 'block.COMMAND_BLOCK'

    ALL_PROPERTIES = []

    PROPERTY_TRIGGERED = BooleanProperty('triggered'); ALL_PROPERTIES.append(PROPERTY_TRIGGERED)
    TRIGGERED_TRUE  = PROPERTY_TRIGGERED.value(True, 'TRIGGERED_TRUE')
    TRIGGERED_FALSE = PROPERTY_TRIGGERED.value(False, 'TRIGGERED_FALSE')


class CraftingTable(BlockDefinition):
    def __init__(self):
        self.id = 58
        self.name = 'crafting_table'
        self.short_usage_str = 'block.CRAFTING_TABLE'

    ALL_PROPERTIES = []


class DarkOakDoor(BlockDefinition):
    def __init__(self):
        self.id = 197
        self.name = 'dark_oak_door'
        self.short_usage_str = 'block.DARK_OAK_DOOR'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_UPPER = PROPERTY_HALF.value('upper', 'HALF_UPPER')
    HALF_LOWER = PROPERTY_HALF.value('lower', 'HALF_LOWER')

    PROPERTY_HINGE = EnumProperty('hinge'); ALL_PROPERTIES.append(PROPERTY_HINGE)
    HINGE_LEFT  = PROPERTY_HINGE.value('left', 'HINGE_LEFT')
    HINGE_RIGHT = PROPERTY_HINGE.value('right', 'HINGE_RIGHT')

    PROPERTY_OPEN = BooleanProperty('open'); ALL_PROPERTIES.append(PROPERTY_OPEN)
    OPEN_TRUE  = PROPERTY_OPEN.value(True, 'OPEN_TRUE')
    OPEN_FALSE = PROPERTY_OPEN.value(False, 'OPEN_FALSE')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class DarkOakFence(BlockDefinition):
    def __init__(self):
        self.id = 191
        self.name = 'dark_oak_fence'
        self.short_usage_str = 'block.DARK_OAK_FENCE'

    ALL_PROPERTIES = []

    PROPERTY_EAST = BooleanProperty('east'); ALL_PROPERTIES.append(PROPERTY_EAST)
    EAST_TRUE  = PROPERTY_EAST.value(True, 'EAST_TRUE')
    EAST_FALSE = PROPERTY_EAST.value(False, 'EAST_FALSE')

    PROPERTY_NORTH = BooleanProperty('north'); ALL_PROPERTIES.append(PROPERTY_NORTH)
    NORTH_TRUE  = PROPERTY_NORTH.value(True, 'NORTH_TRUE')
    NORTH_FALSE = PROPERTY_NORTH.value(False, 'NORTH_FALSE')

    PROPERTY_SOUTH = BooleanProperty('south'); ALL_PROPERTIES.append(PROPERTY_SOUTH)
    SOUTH_TRUE  = PROPERTY_SOUTH.value(True, 'SOUTH_TRUE')
    SOUTH_FALSE = PROPERTY_SOUTH.value(False, 'SOUTH_FALSE')

    PROPERTY_WEST = BooleanProperty('west'); ALL_PROPERTIES.append(PROPERTY_WEST)
    WEST_TRUE  = PROPERTY_WEST.value(True, 'WEST_TRUE')
    WEST_FALSE = PROPERTY_WEST.value(False, 'WEST_FALSE')


class DarkOakFenceGate(BlockDefinition):
    def __init__(self):
        self.id = 186
        self.name = 'dark_oak_fence_gate'
        self.short_usage_str = 'block.DARK_OAK_FENCE_GATE'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_IN_WALL = BooleanProperty('in_wall'); ALL_PROPERTIES.append(PROPERTY_IN_WALL)
    IN_WALL_TRUE  = PROPERTY_IN_WALL.value(True, 'IN_WALL_TRUE')
    IN_WALL_FALSE = PROPERTY_IN_WALL.value(False, 'IN_WALL_FALSE')

    PROPERTY_OPEN = BooleanProperty('open'); ALL_PROPERTIES.append(PROPERTY_OPEN)
    OPEN_TRUE  = PROPERTY_OPEN.value(True, 'OPEN_TRUE')
    OPEN_FALSE = PROPERTY_OPEN.value(False, 'OPEN_FALSE')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class DarkOakStairs(BlockDefinition):
    def __init__(self):
        self.id = 164
        self.name = 'dark_oak_stairs'
        self.short_usage_str = 'block.DARK_OAK_STAIRS'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_SHAPE = EnumProperty('shape'); ALL_PROPERTIES.append(PROPERTY_SHAPE)
    SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight', 'SHAPE_STRAIGHT')
    SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left', 'SHAPE_INNER_LEFT')
    SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right', 'SHAPE_INNER_RIGHT')
    SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left', 'SHAPE_OUTER_LEFT')
    SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right', 'SHAPE_OUTER_RIGHT')


class DaylightDetector(BlockDefinition):
    def __init__(self):
        self.id = 151
        self.name = 'daylight_detector'
        self.short_usage_str = 'block.DAYLIGHT_DETECTOR'

    ALL_PROPERTIES = []

    PROPERTY_POWER = IntegerProperty('power'); ALL_PROPERTIES.append(PROPERTY_POWER)
    POWER_0  = PROPERTY_POWER.value(0, 'POWER_0')
    POWER_1  = PROPERTY_POWER.value(1, 'POWER_1')
    POWER_2  = PROPERTY_POWER.value(2, 'POWER_2')
    POWER_3  = PROPERTY_POWER.value(3, 'POWER_3')
    POWER_4  = PROPERTY_POWER.value(4, 'POWER_4')
    POWER_5  = PROPERTY_POWER.value(5, 'POWER_5')
    POWER_6  = PROPERTY_POWER.value(6, 'POWER_6')
    POWER_7  = PROPERTY_POWER.value(7, 'POWER_7')
    POWER_8  = PROPERTY_POWER.value(8, 'POWER_8')
    POWER_9  = PROPERTY_POWER.value(9, 'POWER_9')
    POWER_10 = PROPERTY_POWER.value(10, 'POWER_10')
    POWER_11 = PROPERTY_POWER.value(11, 'POWER_11')
    POWER_12 = PROPERTY_POWER.value(12, 'POWER_12')
    POWER_13 = PROPERTY_POWER.value(13, 'POWER_13')
    POWER_14 = PROPERTY_POWER.value(14, 'POWER_14')
    POWER_15 = PROPERTY_POWER.value(15, 'POWER_15')


class DaylightDetectorInverted(BlockDefinition):
    def __init__(self):
        self.id = 178
        self.name = 'daylight_detector_inverted'
        self.short_usage_str = 'block.DAYLIGHT_DETECTOR_INVERTED'

    ALL_PROPERTIES = []

    PROPERTY_POWER = IntegerProperty('power'); ALL_PROPERTIES.append(PROPERTY_POWER)
    POWER_0  = PROPERTY_POWER.value(0, 'POWER_0')
    POWER_1  = PROPERTY_POWER.value(1, 'POWER_1')
    POWER_2  = PROPERTY_POWER.value(2, 'POWER_2')
    POWER_3  = PROPERTY_POWER.value(3, 'POWER_3')
    POWER_4  = PROPERTY_POWER.value(4, 'POWER_4')
    POWER_5  = PROPERTY_POWER.value(5, 'POWER_5')
    POWER_6  = PROPERTY_POWER.value(6, 'POWER_6')
    POWER_7  = PROPERTY_POWER.value(7, 'POWER_7')
    POWER_8  = PROPERTY_POWER.value(8, 'POWER_8')
    POWER_9  = PROPERTY_POWER.value(9, 'POWER_9')
    POWER_10 = PROPERTY_POWER.value(10, 'POWER_10')
    POWER_11 = PROPERTY_POWER.value(11, 'POWER_11')
    POWER_12 = PROPERTY_POWER.value(12, 'POWER_12')
    POWER_13 = PROPERTY_POWER.value(13, 'POWER_13')
    POWER_14 = PROPERTY_POWER.value(14, 'POWER_14')
    POWER_15 = PROPERTY_POWER.value(15, 'POWER_15')


class Deadbush(BlockDefinition):
    def __init__(self):
        self.id = 32
        self.name = 'deadbush'
        self.short_usage_str = 'block.DEADBUSH'

    ALL_PROPERTIES = []


class DetectorRail(BlockDefinition):
    def __init__(self):
        self.id = 28
        self.name = 'detector_rail'
        self.short_usage_str = 'block.DETECTOR_RAIL'

    ALL_PROPERTIES = []

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')

    PROPERTY_SHAPE = EnumProperty('shape'); ALL_PROPERTIES.append(PROPERTY_SHAPE)
    SHAPE_NORTH_SOUTH     = PROPERTY_SHAPE.value('north_south', 'SHAPE_NORTH_SOUTH')
    SHAPE_EAST_WEST       = PROPERTY_SHAPE.value('east_west', 'SHAPE_EAST_WEST')
    SHAPE_ASCENDING_EAST  = PROPERTY_SHAPE.value('ascending_east', 'SHAPE_ASCENDING_EAST')
    SHAPE_ASCENDING_WEST  = PROPERTY_SHAPE.value('ascending_west', 'SHAPE_ASCENDING_WEST')
    SHAPE_ASCENDING_NORTH = PROPERTY_SHAPE.value('ascending_north', 'SHAPE_ASCENDING_NORTH')
    SHAPE_ASCENDING_SOUTH = PROPERTY_SHAPE.value('ascending_south', 'SHAPE_ASCENDING_SOUTH')


class DiamondBlock(BlockDefinition):
    def __init__(self):
        self.id = 57
        self.name = 'diamond_block'
        self.short_usage_str = 'block.DIAMOND_BLOCK'

    ALL_PROPERTIES = []


class DiamondOre(BlockDefinition):
    def __init__(self):
        self.id = 56
        self.name = 'diamond_ore'
        self.short_usage_str = 'block.DIAMOND_ORE'

    ALL_PROPERTIES = []


class Dirt(BlockDefinition):
    def __init__(self):
        self.id = 3
        self.name = 'dirt'
        self.short_usage_str = 'block.DIRT'

    ALL_PROPERTIES = []

    PROPERTY_SNOWY = BooleanProperty('snowy'); ALL_PROPERTIES.append(PROPERTY_SNOWY)
    SNOWY_TRUE  = PROPERTY_SNOWY.value(True, 'SNOWY_TRUE')
    SNOWY_FALSE = PROPERTY_SNOWY.value(False, 'SNOWY_FALSE')

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_DIRT        = PROPERTY_VARIANT.value('dirt', 'VARIANT_DIRT')
    VARIANT_COARSE_DIRT = PROPERTY_VARIANT.value('coarse_dirt', 'VARIANT_COARSE_DIRT')
    VARIANT_PODZOL      = PROPERTY_VARIANT.value('podzol', 'VARIANT_PODZOL')


class Dispenser(BlockDefinition):
    def __init__(self):
        self.id = 23
        self.name = 'dispenser'
        self.short_usage_str = 'block.DISPENSER'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_DOWN  = PROPERTY_FACING.value('down', 'FACING_DOWN')
    FACING_UP    = PROPERTY_FACING.value('up', 'FACING_UP')
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_TRIGGERED = BooleanProperty('triggered'); ALL_PROPERTIES.append(PROPERTY_TRIGGERED)
    TRIGGERED_TRUE  = PROPERTY_TRIGGERED.value(True, 'TRIGGERED_TRUE')
    TRIGGERED_FALSE = PROPERTY_TRIGGERED.value(False, 'TRIGGERED_FALSE')


class DoublePlant(BlockDefinition):
    def __init__(self):
        self.id = 175
        self.name = 'double_plant'
        self.short_usage_str = 'block.DOUBLE_PLANT'

    ALL_PROPERTIES = []

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_UPPER = PROPERTY_HALF.value('upper', 'HALF_UPPER')
    HALF_LOWER = PROPERTY_HALF.value('lower', 'HALF_LOWER')

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_SUNFLOWER    = PROPERTY_VARIANT.value('sunflower', 'VARIANT_SUNFLOWER')
    VARIANT_SYRINGA      = PROPERTY_VARIANT.value('syringa', 'VARIANT_SYRINGA')
    VARIANT_DOUBLE_GRASS = PROPERTY_VARIANT.value('double_grass', 'VARIANT_DOUBLE_GRASS')
    VARIANT_DOUBLE_FERN  = PROPERTY_VARIANT.value('double_fern', 'VARIANT_DOUBLE_FERN')
    VARIANT_DOUBLE_ROSE  = PROPERTY_VARIANT.value('double_rose', 'VARIANT_DOUBLE_ROSE')
    VARIANT_PAEONIA      = PROPERTY_VARIANT.value('paeonia', 'VARIANT_PAEONIA')


class DoubleStoneSlab(BlockDefinition):
    def __init__(self):
        self.id = 43
        self.name = 'double_stone_slab'
        self.short_usage_str = 'block.DOUBLE_STONE_SLAB'

    ALL_PROPERTIES = []

    PROPERTY_SEAMLESS = BooleanProperty('seamless'); ALL_PROPERTIES.append(PROPERTY_SEAMLESS)
    SEAMLESS_TRUE  = PROPERTY_SEAMLESS.value(True, 'SEAMLESS_TRUE')
    SEAMLESS_FALSE = PROPERTY_SEAMLESS.value(False, 'SEAMLESS_FALSE')

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_STONE        = PROPERTY_VARIANT.value('stone', 'VARIANT_STONE')
    VARIANT_SANDSTONE    = PROPERTY_VARIANT.value('sandstone', 'VARIANT_SANDSTONE')
    VARIANT_WOOD_OLD     = PROPERTY_VARIANT.value('wood_old', 'VARIANT_WOOD_OLD')
    VARIANT_COBBLESTONE  = PROPERTY_VARIANT.value('cobblestone', 'VARIANT_COBBLESTONE')
    VARIANT_BRICK        = PROPERTY_VARIANT.value('brick', 'VARIANT_BRICK')
    VARIANT_STONE_BRICK  = PROPERTY_VARIANT.value('stone_brick', 'VARIANT_STONE_BRICK')
    VARIANT_NETHER_BRICK = PROPERTY_VARIANT.value('nether_brick', 'VARIANT_NETHER_BRICK')
    VARIANT_QUARTZ       = PROPERTY_VARIANT.value('quartz', 'VARIANT_QUARTZ')


class DoubleStoneSlab2(BlockDefinition):
    def __init__(self):
        self.id = 181
        self.name = 'double_stone_slab2'
        self.short_usage_str = 'block.DOUBLE_STONE_SLAB2'

    ALL_PROPERTIES = []

    PROPERTY_SEAMLESS = BooleanProperty('seamless'); ALL_PROPERTIES.append(PROPERTY_SEAMLESS)
    SEAMLESS_TRUE  = PROPERTY_SEAMLESS.value(True, 'SEAMLESS_TRUE')
    SEAMLESS_FALSE = PROPERTY_SEAMLESS.value(False, 'SEAMLESS_FALSE')

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_RED_SANDSTONE = PROPERTY_VARIANT.value('red_sandstone', 'VARIANT_RED_SANDSTONE')


class DoubleWoodenSlab(BlockDefinition):
    def __init__(self):
        self.id = 125
        self.name = 'double_wooden_slab'
        self.short_usage_str = 'block.DOUBLE_WOODEN_SLAB'

    ALL_PROPERTIES = []

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_OAK      = PROPERTY_VARIANT.value('oak', 'VARIANT_OAK')
    VARIANT_SPRUCE   = PROPERTY_VARIANT.value('spruce', 'VARIANT_SPRUCE')
    VARIANT_BIRCH    = PROPERTY_VARIANT.value('birch', 'VARIANT_BIRCH')
    VARIANT_JUNGLE   = PROPERTY_VARIANT.value('jungle', 'VARIANT_JUNGLE')
    VARIANT_ACACIA   = PROPERTY_VARIANT.value('acacia', 'VARIANT_ACACIA')
    VARIANT_DARK_OAK = PROPERTY_VARIANT.value('dark_oak', 'VARIANT_DARK_OAK')


class DragonEgg(BlockDefinition):
    def __init__(self):
        self.id = 122
        self.name = 'dragon_egg'
        self.short_usage_str = 'block.DRAGON_EGG'

    ALL_PROPERTIES = []


class Dropper(BlockDefinition):
    def __init__(self):
        self.id = 158
        self.name = 'dropper'
        self.short_usage_str = 'block.DROPPER'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_DOWN  = PROPERTY_FACING.value('down', 'FACING_DOWN')
    FACING_UP    = PROPERTY_FACING.value('up', 'FACING_UP')
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_TRIGGERED = BooleanProperty('triggered'); ALL_PROPERTIES.append(PROPERTY_TRIGGERED)
    TRIGGERED_TRUE  = PROPERTY_TRIGGERED.value(True, 'TRIGGERED_TRUE')
    TRIGGERED_FALSE = PROPERTY_TRIGGERED.value(False, 'TRIGGERED_FALSE')


class EmeraldBlock(BlockDefinition):
    def __init__(self):
        self.id = 133
        self.name = 'emerald_block'
        self.short_usage_str = 'block.EMERALD_BLOCK'

    ALL_PROPERTIES = []


class EmeraldOre(BlockDefinition):
    def __init__(self):
        self.id = 129
        self.name = 'emerald_ore'
        self.short_usage_str = 'block.EMERALD_ORE'

    ALL_PROPERTIES = []


class EnchantingTable(BlockDefinition):
    def __init__(self):
        self.id = 116
        self.name = 'enchanting_table'
        self.short_usage_str = 'block.ENCHANTING_TABLE'

    ALL_PROPERTIES = []


class EndPortal(BlockDefinition):
    def __init__(self):
        self.id = 119
        self.name = 'end_portal'
        self.short_usage_str = 'block.END_PORTAL'

    ALL_PROPERTIES = []


class EndPortalFrame(BlockDefinition):
    def __init__(self):
        self.id = 120
        self.name = 'end_portal_frame'
        self.short_usage_str = 'block.END_PORTAL_FRAME'

    ALL_PROPERTIES = []

    PROPERTY_EYE = BooleanProperty('eye'); ALL_PROPERTIES.append(PROPERTY_EYE)
    EYE_TRUE  = PROPERTY_EYE.value(True, 'EYE_TRUE')
    EYE_FALSE = PROPERTY_EYE.value(False, 'EYE_FALSE')

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class EndStone(BlockDefinition):
    def __init__(self):
        self.id = 121
        self.name = 'end_stone'
        self.short_usage_str = 'block.END_STONE'

    ALL_PROPERTIES = []


class EnderChest(BlockDefinition):
    def __init__(self):
        self.id = 130
        self.name = 'ender_chest'
        self.short_usage_str = 'block.ENDER_CHEST'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class Farmland(BlockDefinition):
    def __init__(self):
        self.id = 60
        self.name = 'farmland'
        self.short_usage_str = 'block.FARMLAND'

    ALL_PROPERTIES = []

    PROPERTY_MOISTURE = IntegerProperty('moisture'); ALL_PROPERTIES.append(PROPERTY_MOISTURE)
    MOISTURE_0 = PROPERTY_MOISTURE.value(0, 'MOISTURE_0')
    MOISTURE_1 = PROPERTY_MOISTURE.value(1, 'MOISTURE_1')
    MOISTURE_2 = PROPERTY_MOISTURE.value(2, 'MOISTURE_2')
    MOISTURE_3 = PROPERTY_MOISTURE.value(3, 'MOISTURE_3')
    MOISTURE_4 = PROPERTY_MOISTURE.value(4, 'MOISTURE_4')
    MOISTURE_5 = PROPERTY_MOISTURE.value(5, 'MOISTURE_5')
    MOISTURE_6 = PROPERTY_MOISTURE.value(6, 'MOISTURE_6')
    MOISTURE_7 = PROPERTY_MOISTURE.value(7, 'MOISTURE_7')


class Fence(BlockDefinition):
    def __init__(self):
        self.id = 85
        self.name = 'fence'
        self.short_usage_str = 'block.FENCE'

    ALL_PROPERTIES = []

    PROPERTY_EAST = BooleanProperty('east'); ALL_PROPERTIES.append(PROPERTY_EAST)
    EAST_TRUE  = PROPERTY_EAST.value(True, 'EAST_TRUE')
    EAST_FALSE = PROPERTY_EAST.value(False, 'EAST_FALSE')

    PROPERTY_NORTH = BooleanProperty('north'); ALL_PROPERTIES.append(PROPERTY_NORTH)
    NORTH_TRUE  = PROPERTY_NORTH.value(True, 'NORTH_TRUE')
    NORTH_FALSE = PROPERTY_NORTH.value(False, 'NORTH_FALSE')

    PROPERTY_SOUTH = BooleanProperty('south'); ALL_PROPERTIES.append(PROPERTY_SOUTH)
    SOUTH_TRUE  = PROPERTY_SOUTH.value(True, 'SOUTH_TRUE')
    SOUTH_FALSE = PROPERTY_SOUTH.value(False, 'SOUTH_FALSE')

    PROPERTY_WEST = BooleanProperty('west'); ALL_PROPERTIES.append(PROPERTY_WEST)
    WEST_TRUE  = PROPERTY_WEST.value(True, 'WEST_TRUE')
    WEST_FALSE = PROPERTY_WEST.value(False, 'WEST_FALSE')


class FenceGate(BlockDefinition):
    def __init__(self):
        self.id = 107
        self.name = 'fence_gate'
        self.short_usage_str = 'block.FENCE_GATE'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_IN_WALL = BooleanProperty('in_wall'); ALL_PROPERTIES.append(PROPERTY_IN_WALL)
    IN_WALL_TRUE  = PROPERTY_IN_WALL.value(True, 'IN_WALL_TRUE')
    IN_WALL_FALSE = PROPERTY_IN_WALL.value(False, 'IN_WALL_FALSE')

    PROPERTY_OPEN = BooleanProperty('open'); ALL_PROPERTIES.append(PROPERTY_OPEN)
    OPEN_TRUE  = PROPERTY_OPEN.value(True, 'OPEN_TRUE')
    OPEN_FALSE = PROPERTY_OPEN.value(False, 'OPEN_FALSE')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class Fire(BlockDefinition):
    def __init__(self):
        self.id = 51
        self.name = 'fire'
        self.short_usage_str = 'block.FIRE'

    ALL_PROPERTIES = []

    PROPERTY_AGE = IntegerProperty('age'); ALL_PROPERTIES.append(PROPERTY_AGE)
    AGE_0  = PROPERTY_AGE.value(0, 'AGE_0')
    AGE_1  = PROPERTY_AGE.value(1, 'AGE_1')
    AGE_2  = PROPERTY_AGE.value(2, 'AGE_2')
    AGE_3  = PROPERTY_AGE.value(3, 'AGE_3')
    AGE_4  = PROPERTY_AGE.value(4, 'AGE_4')
    AGE_5  = PROPERTY_AGE.value(5, 'AGE_5')
    AGE_6  = PROPERTY_AGE.value(6, 'AGE_6')
    AGE_7  = PROPERTY_AGE.value(7, 'AGE_7')
    AGE_8  = PROPERTY_AGE.value(8, 'AGE_8')
    AGE_9  = PROPERTY_AGE.value(9, 'AGE_9')
    AGE_10 = PROPERTY_AGE.value(10, 'AGE_10')
    AGE_11 = PROPERTY_AGE.value(11, 'AGE_11')
    AGE_12 = PROPERTY_AGE.value(12, 'AGE_12')
    AGE_13 = PROPERTY_AGE.value(13, 'AGE_13')
    AGE_14 = PROPERTY_AGE.value(14, 'AGE_14')
    AGE_15 = PROPERTY_AGE.value(15, 'AGE_15')

    PROPERTY_ALT = BooleanProperty('alt'); ALL_PROPERTIES.append(PROPERTY_ALT)
    ALT_TRUE  = PROPERTY_ALT.value(True, 'ALT_TRUE')
    ALT_FALSE = PROPERTY_ALT.value(False, 'ALT_FALSE')

    PROPERTY_EAST = BooleanProperty('east'); ALL_PROPERTIES.append(PROPERTY_EAST)
    EAST_TRUE  = PROPERTY_EAST.value(True, 'EAST_TRUE')
    EAST_FALSE = PROPERTY_EAST.value(False, 'EAST_FALSE')

    PROPERTY_FLIP = BooleanProperty('flip'); ALL_PROPERTIES.append(PROPERTY_FLIP)
    FLIP_TRUE  = PROPERTY_FLIP.value(True, 'FLIP_TRUE')
    FLIP_FALSE = PROPERTY_FLIP.value(False, 'FLIP_FALSE')

    PROPERTY_NORTH = BooleanProperty('north'); ALL_PROPERTIES.append(PROPERTY_NORTH)
    NORTH_TRUE  = PROPERTY_NORTH.value(True, 'NORTH_TRUE')
    NORTH_FALSE = PROPERTY_NORTH.value(False, 'NORTH_FALSE')

    PROPERTY_SOUTH = BooleanProperty('south'); ALL_PROPERTIES.append(PROPERTY_SOUTH)
    SOUTH_TRUE  = PROPERTY_SOUTH.value(True, 'SOUTH_TRUE')
    SOUTH_FALSE = PROPERTY_SOUTH.value(False, 'SOUTH_FALSE')

    PROPERTY_UPPER = IntegerProperty('upper'); ALL_PROPERTIES.append(PROPERTY_UPPER)
    UPPER_0 = PROPERTY_UPPER.value(0, 'UPPER_0')
    UPPER_1 = PROPERTY_UPPER.value(1, 'UPPER_1')
    UPPER_2 = PROPERTY_UPPER.value(2, 'UPPER_2')

    PROPERTY_WEST = BooleanProperty('west'); ALL_PROPERTIES.append(PROPERTY_WEST)
    WEST_TRUE  = PROPERTY_WEST.value(True, 'WEST_TRUE')
    WEST_FALSE = PROPERTY_WEST.value(False, 'WEST_FALSE')


class FlowerPot(BlockDefinition):
    def __init__(self):
        self.id = 140
        self.name = 'flower_pot'
        self.short_usage_str = 'block.FLOWER_POT'

    ALL_PROPERTIES = []

    PROPERTY_CONTENTS = EnumProperty('contents'); ALL_PROPERTIES.append(PROPERTY_CONTENTS)
    CONTENTS_EMPTY            = PROPERTY_CONTENTS.value('empty', 'CONTENTS_EMPTY')
    CONTENTS_ROSE             = PROPERTY_CONTENTS.value('rose', 'CONTENTS_ROSE')
    CONTENTS_BLUE_ORCHID      = PROPERTY_CONTENTS.value('blue_orchid', 'CONTENTS_BLUE_ORCHID')
    CONTENTS_ALLIUM           = PROPERTY_CONTENTS.value('allium', 'CONTENTS_ALLIUM')
    CONTENTS_HOUSTONIA        = PROPERTY_CONTENTS.value('houstonia', 'CONTENTS_HOUSTONIA')
    CONTENTS_RED_TULIP        = PROPERTY_CONTENTS.value('red_tulip', 'CONTENTS_RED_TULIP')
    CONTENTS_ORANGE_TULIP     = PROPERTY_CONTENTS.value('orange_tulip', 'CONTENTS_ORANGE_TULIP')
    CONTENTS_WHITE_TULIP      = PROPERTY_CONTENTS.value('white_tulip', 'CONTENTS_WHITE_TULIP')
    CONTENTS_PINK_TULIP       = PROPERTY_CONTENTS.value('pink_tulip', 'CONTENTS_PINK_TULIP')
    CONTENTS_OXEYE_DAISY      = PROPERTY_CONTENTS.value('oxeye_daisy', 'CONTENTS_OXEYE_DAISY')
    CONTENTS_DANDELION        = PROPERTY_CONTENTS.value('dandelion', 'CONTENTS_DANDELION')
    CONTENTS_OAK_SAPLING      = PROPERTY_CONTENTS.value('oak_sapling', 'CONTENTS_OAK_SAPLING')
    CONTENTS_SPRUCE_SAPLING   = PROPERTY_CONTENTS.value('spruce_sapling', 'CONTENTS_SPRUCE_SAPLING')
    CONTENTS_BIRCH_SAPLING    = PROPERTY_CONTENTS.value('birch_sapling', 'CONTENTS_BIRCH_SAPLING')
    CONTENTS_JUNGLE_SAPLING   = PROPERTY_CONTENTS.value('jungle_sapling', 'CONTENTS_JUNGLE_SAPLING')
    CONTENTS_ACACIA_SAPLING   = PROPERTY_CONTENTS.value('acacia_sapling', 'CONTENTS_ACACIA_SAPLING')
    CONTENTS_DARK_OAK_SAPLING = PROPERTY_CONTENTS.value('dark_oak_sapling', 'CONTENTS_DARK_OAK_SAPLING')
    CONTENTS_MUSHROOM_RED     = PROPERTY_CONTENTS.value('mushroom_red', 'CONTENTS_MUSHROOM_RED')
    CONTENTS_MUSHROOM_BROWN   = PROPERTY_CONTENTS.value('mushroom_brown', 'CONTENTS_MUSHROOM_BROWN')
    CONTENTS_DEAD_BUSH        = PROPERTY_CONTENTS.value('dead_bush', 'CONTENTS_DEAD_BUSH')
    CONTENTS_FERN             = PROPERTY_CONTENTS.value('fern', 'CONTENTS_FERN')
    CONTENTS_CACTUS           = PROPERTY_CONTENTS.value('cactus', 'CONTENTS_CACTUS')

    PROPERTY_LEGACY_DATA = IntegerProperty('legacy_data'); ALL_PROPERTIES.append(PROPERTY_LEGACY_DATA)
    LEGACY_DATA_0  = PROPERTY_LEGACY_DATA.value(0, 'LEGACY_DATA_0')
    LEGACY_DATA_1  = PROPERTY_LEGACY_DATA.value(1, 'LEGACY_DATA_1')
    LEGACY_DATA_2  = PROPERTY_LEGACY_DATA.value(2, 'LEGACY_DATA_2')
    LEGACY_DATA_3  = PROPERTY_LEGACY_DATA.value(3, 'LEGACY_DATA_3')
    LEGACY_DATA_4  = PROPERTY_LEGACY_DATA.value(4, 'LEGACY_DATA_4')
    LEGACY_DATA_5  = PROPERTY_LEGACY_DATA.value(5, 'LEGACY_DATA_5')
    LEGACY_DATA_6  = PROPERTY_LEGACY_DATA.value(6, 'LEGACY_DATA_6')
    LEGACY_DATA_7  = PROPERTY_LEGACY_DATA.value(7, 'LEGACY_DATA_7')
    LEGACY_DATA_8  = PROPERTY_LEGACY_DATA.value(8, 'LEGACY_DATA_8')
    LEGACY_DATA_9  = PROPERTY_LEGACY_DATA.value(9, 'LEGACY_DATA_9')
    LEGACY_DATA_10 = PROPERTY_LEGACY_DATA.value(10, 'LEGACY_DATA_10')
    LEGACY_DATA_11 = PROPERTY_LEGACY_DATA.value(11, 'LEGACY_DATA_11')
    LEGACY_DATA_12 = PROPERTY_LEGACY_DATA.value(12, 'LEGACY_DATA_12')
    LEGACY_DATA_13 = PROPERTY_LEGACY_DATA.value(13, 'LEGACY_DATA_13')
    LEGACY_DATA_14 = PROPERTY_LEGACY_DATA.value(14, 'LEGACY_DATA_14')
    LEGACY_DATA_15 = PROPERTY_LEGACY_DATA.value(15, 'LEGACY_DATA_15')


class FlowingLava(BlockDefinition):
    def __init__(self):
        self.id = 10
        self.name = 'flowing_lava'
        self.short_usage_str = 'block.FLOWING_LAVA'

    ALL_PROPERTIES = []

    PROPERTY_LEVEL = IntegerProperty('level'); ALL_PROPERTIES.append(PROPERTY_LEVEL)
    LEVEL_0  = PROPERTY_LEVEL.value(0, 'LEVEL_0')
    LEVEL_1  = PROPERTY_LEVEL.value(1, 'LEVEL_1')
    LEVEL_2  = PROPERTY_LEVEL.value(2, 'LEVEL_2')
    LEVEL_3  = PROPERTY_LEVEL.value(3, 'LEVEL_3')
    LEVEL_4  = PROPERTY_LEVEL.value(4, 'LEVEL_4')
    LEVEL_5  = PROPERTY_LEVEL.value(5, 'LEVEL_5')
    LEVEL_6  = PROPERTY_LEVEL.value(6, 'LEVEL_6')
    LEVEL_7  = PROPERTY_LEVEL.value(7, 'LEVEL_7')
    LEVEL_8  = PROPERTY_LEVEL.value(8, 'LEVEL_8')
    LEVEL_9  = PROPERTY_LEVEL.value(9, 'LEVEL_9')
    LEVEL_10 = PROPERTY_LEVEL.value(10, 'LEVEL_10')
    LEVEL_11 = PROPERTY_LEVEL.value(11, 'LEVEL_11')
    LEVEL_12 = PROPERTY_LEVEL.value(12, 'LEVEL_12')
    LEVEL_13 = PROPERTY_LEVEL.value(13, 'LEVEL_13')
    LEVEL_14 = PROPERTY_LEVEL.value(14, 'LEVEL_14')
    LEVEL_15 = PROPERTY_LEVEL.value(15, 'LEVEL_15')


class FlowingWater(BlockDefinition):
    def __init__(self):
        self.id = 8
        self.name = 'flowing_water'
        self.short_usage_str = 'block.FLOWING_WATER'

    ALL_PROPERTIES = []

    PROPERTY_LEVEL = IntegerProperty('level'); ALL_PROPERTIES.append(PROPERTY_LEVEL)
    LEVEL_0  = PROPERTY_LEVEL.value(0, 'LEVEL_0')
    LEVEL_1  = PROPERTY_LEVEL.value(1, 'LEVEL_1')
    LEVEL_2  = PROPERTY_LEVEL.value(2, 'LEVEL_2')
    LEVEL_3  = PROPERTY_LEVEL.value(3, 'LEVEL_3')
    LEVEL_4  = PROPERTY_LEVEL.value(4, 'LEVEL_4')
    LEVEL_5  = PROPERTY_LEVEL.value(5, 'LEVEL_5')
    LEVEL_6  = PROPERTY_LEVEL.value(6, 'LEVEL_6')
    LEVEL_7  = PROPERTY_LEVEL.value(7, 'LEVEL_7')
    LEVEL_8  = PROPERTY_LEVEL.value(8, 'LEVEL_8')
    LEVEL_9  = PROPERTY_LEVEL.value(9, 'LEVEL_9')
    LEVEL_10 = PROPERTY_LEVEL.value(10, 'LEVEL_10')
    LEVEL_11 = PROPERTY_LEVEL.value(11, 'LEVEL_11')
    LEVEL_12 = PROPERTY_LEVEL.value(12, 'LEVEL_12')
    LEVEL_13 = PROPERTY_LEVEL.value(13, 'LEVEL_13')
    LEVEL_14 = PROPERTY_LEVEL.value(14, 'LEVEL_14')
    LEVEL_15 = PROPERTY_LEVEL.value(15, 'LEVEL_15')


class Furnace(BlockDefinition):
    def __init__(self):
        self.id = 61
        self.name = 'furnace'
        self.short_usage_str = 'block.FURNACE'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class Glass(BlockDefinition):
    def __init__(self):
        self.id = 20
        self.name = 'glass'
        self.short_usage_str = 'block.GLASS'

    ALL_PROPERTIES = []


class GlassPane(BlockDefinition):
    def __init__(self):
        self.id = 102
        self.name = 'glass_pane'
        self.short_usage_str = 'block.GLASS_PANE'

    ALL_PROPERTIES = []

    PROPERTY_EAST = BooleanProperty('east'); ALL_PROPERTIES.append(PROPERTY_EAST)
    EAST_TRUE  = PROPERTY_EAST.value(True, 'EAST_TRUE')
    EAST_FALSE = PROPERTY_EAST.value(False, 'EAST_FALSE')

    PROPERTY_NORTH = BooleanProperty('north'); ALL_PROPERTIES.append(PROPERTY_NORTH)
    NORTH_TRUE  = PROPERTY_NORTH.value(True, 'NORTH_TRUE')
    NORTH_FALSE = PROPERTY_NORTH.value(False, 'NORTH_FALSE')

    PROPERTY_SOUTH = BooleanProperty('south'); ALL_PROPERTIES.append(PROPERTY_SOUTH)
    SOUTH_TRUE  = PROPERTY_SOUTH.value(True, 'SOUTH_TRUE')
    SOUTH_FALSE = PROPERTY_SOUTH.value(False, 'SOUTH_FALSE')

    PROPERTY_WEST = BooleanProperty('west'); ALL_PROPERTIES.append(PROPERTY_WEST)
    WEST_TRUE  = PROPERTY_WEST.value(True, 'WEST_TRUE')
    WEST_FALSE = PROPERTY_WEST.value(False, 'WEST_FALSE')


class Glowstone(BlockDefinition):
    def __init__(self):
        self.id = 89
        self.name = 'glowstone'
        self.short_usage_str = 'block.GLOWSTONE'

    ALL_PROPERTIES = []


class GoldBlock(BlockDefinition):
    def __init__(self):
        self.id = 41
        self.name = 'gold_block'
        self.short_usage_str = 'block.GOLD_BLOCK'

    ALL_PROPERTIES = []


class GoldOre(BlockDefinition):
    def __init__(self):
        self.id = 14
        self.name = 'gold_ore'
        self.short_usage_str = 'block.GOLD_ORE'

    ALL_PROPERTIES = []


class GoldenRail(BlockDefinition):
    def __init__(self):
        self.id = 27
        self.name = 'golden_rail'
        self.short_usage_str = 'block.GOLDEN_RAIL'

    ALL_PROPERTIES = []

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')

    PROPERTY_SHAPE = EnumProperty('shape'); ALL_PROPERTIES.append(PROPERTY_SHAPE)
    SHAPE_NORTH_SOUTH     = PROPERTY_SHAPE.value('north_south', 'SHAPE_NORTH_SOUTH')
    SHAPE_EAST_WEST       = PROPERTY_SHAPE.value('east_west', 'SHAPE_EAST_WEST')
    SHAPE_ASCENDING_EAST  = PROPERTY_SHAPE.value('ascending_east', 'SHAPE_ASCENDING_EAST')
    SHAPE_ASCENDING_WEST  = PROPERTY_SHAPE.value('ascending_west', 'SHAPE_ASCENDING_WEST')
    SHAPE_ASCENDING_NORTH = PROPERTY_SHAPE.value('ascending_north', 'SHAPE_ASCENDING_NORTH')
    SHAPE_ASCENDING_SOUTH = PROPERTY_SHAPE.value('ascending_south', 'SHAPE_ASCENDING_SOUTH')


class Grass(BlockDefinition):
    def __init__(self):
        self.id = 2
        self.name = 'grass'
        self.short_usage_str = 'block.GRASS'

    ALL_PROPERTIES = []

    PROPERTY_SNOWY = BooleanProperty('snowy'); ALL_PROPERTIES.append(PROPERTY_SNOWY)
    SNOWY_TRUE  = PROPERTY_SNOWY.value(True, 'SNOWY_TRUE')
    SNOWY_FALSE = PROPERTY_SNOWY.value(False, 'SNOWY_FALSE')


class Gravel(BlockDefinition):
    def __init__(self):
        self.id = 13
        self.name = 'gravel'
        self.short_usage_str = 'block.GRAVEL'

    ALL_PROPERTIES = []


class HardenedClay(BlockDefinition):
    def __init__(self):
        self.id = 172
        self.name = 'hardened_clay'
        self.short_usage_str = 'block.HARDENED_CLAY'

    ALL_PROPERTIES = []


class HayBlock(BlockDefinition):
    def __init__(self):
        self.id = 170
        self.name = 'hay_block'
        self.short_usage_str = 'block.HAY_BLOCK'

    ALL_PROPERTIES = []

    PROPERTY_AXIS = EnumProperty('axis'); ALL_PROPERTIES.append(PROPERTY_AXIS)
    AXIS_X = PROPERTY_AXIS.value('x', 'AXIS_X')
    AXIS_Y = PROPERTY_AXIS.value('y', 'AXIS_Y')
    AXIS_Z = PROPERTY_AXIS.value('z', 'AXIS_Z')


class HeavyWeightedPressurePlate(BlockDefinition):
    def __init__(self):
        self.id = 148
        self.name = 'heavy_weighted_pressure_plate'
        self.short_usage_str = 'block.HEAVY_WEIGHTED_PRESSURE_PLATE'

    ALL_PROPERTIES = []

    PROPERTY_POWER = IntegerProperty('power'); ALL_PROPERTIES.append(PROPERTY_POWER)
    POWER_0  = PROPERTY_POWER.value(0, 'POWER_0')
    POWER_1  = PROPERTY_POWER.value(1, 'POWER_1')
    POWER_2  = PROPERTY_POWER.value(2, 'POWER_2')
    POWER_3  = PROPERTY_POWER.value(3, 'POWER_3')
    POWER_4  = PROPERTY_POWER.value(4, 'POWER_4')
    POWER_5  = PROPERTY_POWER.value(5, 'POWER_5')
    POWER_6  = PROPERTY_POWER.value(6, 'POWER_6')
    POWER_7  = PROPERTY_POWER.value(7, 'POWER_7')
    POWER_8  = PROPERTY_POWER.value(8, 'POWER_8')
    POWER_9  = PROPERTY_POWER.value(9, 'POWER_9')
    POWER_10 = PROPERTY_POWER.value(10, 'POWER_10')
    POWER_11 = PROPERTY_POWER.value(11, 'POWER_11')
    POWER_12 = PROPERTY_POWER.value(12, 'POWER_12')
    POWER_13 = PROPERTY_POWER.value(13, 'POWER_13')
    POWER_14 = PROPERTY_POWER.value(14, 'POWER_14')
    POWER_15 = PROPERTY_POWER.value(15, 'POWER_15')


class Hopper(BlockDefinition):
    def __init__(self):
        self.id = 154
        self.name = 'hopper'
        self.short_usage_str = 'block.HOPPER'

    ALL_PROPERTIES = []

    PROPERTY_ENABLED = BooleanProperty('enabled'); ALL_PROPERTIES.append(PROPERTY_ENABLED)
    ENABLED_TRUE  = PROPERTY_ENABLED.value(True, 'ENABLED_TRUE')
    ENABLED_FALSE = PROPERTY_ENABLED.value(False, 'ENABLED_FALSE')

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_DOWN  = PROPERTY_FACING.value('down', 'FACING_DOWN')
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class Ice(BlockDefinition):
    def __init__(self):
        self.id = 79
        self.name = 'ice'
        self.short_usage_str = 'block.ICE'

    ALL_PROPERTIES = []


class IronBars(BlockDefinition):
    def __init__(self):
        self.id = 101
        self.name = 'iron_bars'
        self.short_usage_str = 'block.IRON_BARS'

    ALL_PROPERTIES = []

    PROPERTY_EAST = BooleanProperty('east'); ALL_PROPERTIES.append(PROPERTY_EAST)
    EAST_TRUE  = PROPERTY_EAST.value(True, 'EAST_TRUE')
    EAST_FALSE = PROPERTY_EAST.value(False, 'EAST_FALSE')

    PROPERTY_NORTH = BooleanProperty('north'); ALL_PROPERTIES.append(PROPERTY_NORTH)
    NORTH_TRUE  = PROPERTY_NORTH.value(True, 'NORTH_TRUE')
    NORTH_FALSE = PROPERTY_NORTH.value(False, 'NORTH_FALSE')

    PROPERTY_SOUTH = BooleanProperty('south'); ALL_PROPERTIES.append(PROPERTY_SOUTH)
    SOUTH_TRUE  = PROPERTY_SOUTH.value(True, 'SOUTH_TRUE')
    SOUTH_FALSE = PROPERTY_SOUTH.value(False, 'SOUTH_FALSE')

    PROPERTY_WEST = BooleanProperty('west'); ALL_PROPERTIES.append(PROPERTY_WEST)
    WEST_TRUE  = PROPERTY_WEST.value(True, 'WEST_TRUE')
    WEST_FALSE = PROPERTY_WEST.value(False, 'WEST_FALSE')


class IronBlock(BlockDefinition):
    def __init__(self):
        self.id = 42
        self.name = 'iron_block'
        self.short_usage_str = 'block.IRON_BLOCK'

    ALL_PROPERTIES = []


class IronDoor(BlockDefinition):
    def __init__(self):
        self.id = 71
        self.name = 'iron_door'
        self.short_usage_str = 'block.IRON_DOOR'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_UPPER = PROPERTY_HALF.value('upper', 'HALF_UPPER')
    HALF_LOWER = PROPERTY_HALF.value('lower', 'HALF_LOWER')

    PROPERTY_HINGE = EnumProperty('hinge'); ALL_PROPERTIES.append(PROPERTY_HINGE)
    HINGE_LEFT  = PROPERTY_HINGE.value('left', 'HINGE_LEFT')
    HINGE_RIGHT = PROPERTY_HINGE.value('right', 'HINGE_RIGHT')

    PROPERTY_OPEN = BooleanProperty('open'); ALL_PROPERTIES.append(PROPERTY_OPEN)
    OPEN_TRUE  = PROPERTY_OPEN.value(True, 'OPEN_TRUE')
    OPEN_FALSE = PROPERTY_OPEN.value(False, 'OPEN_FALSE')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class IronOre(BlockDefinition):
    def __init__(self):
        self.id = 15
        self.name = 'iron_ore'
        self.short_usage_str = 'block.IRON_ORE'

    ALL_PROPERTIES = []


class IronTrapdoor(BlockDefinition):
    def __init__(self):
        self.id = 167
        self.name = 'iron_trapdoor'
        self.short_usage_str = 'block.IRON_TRAPDOOR'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_OPEN = BooleanProperty('open'); ALL_PROPERTIES.append(PROPERTY_OPEN)
    OPEN_TRUE  = PROPERTY_OPEN.value(True, 'OPEN_TRUE')
    OPEN_FALSE = PROPERTY_OPEN.value(False, 'OPEN_FALSE')


class Jukebox(BlockDefinition):
    def __init__(self):
        self.id = 84
        self.name = 'jukebox'
        self.short_usage_str = 'block.JUKEBOX'

    ALL_PROPERTIES = []

    PROPERTY_HAS_RECORD = BooleanProperty('has_record'); ALL_PROPERTIES.append(PROPERTY_HAS_RECORD)
    HAS_RECORD_TRUE  = PROPERTY_HAS_RECORD.value(True, 'HAS_RECORD_TRUE')
    HAS_RECORD_FALSE = PROPERTY_HAS_RECORD.value(False, 'HAS_RECORD_FALSE')


class JungleDoor(BlockDefinition):
    def __init__(self):
        self.id = 195
        self.name = 'jungle_door'
        self.short_usage_str = 'block.JUNGLE_DOOR'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_UPPER = PROPERTY_HALF.value('upper', 'HALF_UPPER')
    HALF_LOWER = PROPERTY_HALF.value('lower', 'HALF_LOWER')

    PROPERTY_HINGE = EnumProperty('hinge'); ALL_PROPERTIES.append(PROPERTY_HINGE)
    HINGE_LEFT  = PROPERTY_HINGE.value('left', 'HINGE_LEFT')
    HINGE_RIGHT = PROPERTY_HINGE.value('right', 'HINGE_RIGHT')

    PROPERTY_OPEN = BooleanProperty('open'); ALL_PROPERTIES.append(PROPERTY_OPEN)
    OPEN_TRUE  = PROPERTY_OPEN.value(True, 'OPEN_TRUE')
    OPEN_FALSE = PROPERTY_OPEN.value(False, 'OPEN_FALSE')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class JungleFence(BlockDefinition):
    def __init__(self):
        self.id = 190
        self.name = 'jungle_fence'
        self.short_usage_str = 'block.JUNGLE_FENCE'

    ALL_PROPERTIES = []

    PROPERTY_EAST = BooleanProperty('east'); ALL_PROPERTIES.append(PROPERTY_EAST)
    EAST_TRUE  = PROPERTY_EAST.value(True, 'EAST_TRUE')
    EAST_FALSE = PROPERTY_EAST.value(False, 'EAST_FALSE')

    PROPERTY_NORTH = BooleanProperty('north'); ALL_PROPERTIES.append(PROPERTY_NORTH)
    NORTH_TRUE  = PROPERTY_NORTH.value(True, 'NORTH_TRUE')
    NORTH_FALSE = PROPERTY_NORTH.value(False, 'NORTH_FALSE')

    PROPERTY_SOUTH = BooleanProperty('south'); ALL_PROPERTIES.append(PROPERTY_SOUTH)
    SOUTH_TRUE  = PROPERTY_SOUTH.value(True, 'SOUTH_TRUE')
    SOUTH_FALSE = PROPERTY_SOUTH.value(False, 'SOUTH_FALSE')

    PROPERTY_WEST = BooleanProperty('west'); ALL_PROPERTIES.append(PROPERTY_WEST)
    WEST_TRUE  = PROPERTY_WEST.value(True, 'WEST_TRUE')
    WEST_FALSE = PROPERTY_WEST.value(False, 'WEST_FALSE')


class JungleFenceGate(BlockDefinition):
    def __init__(self):
        self.id = 185
        self.name = 'jungle_fence_gate'
        self.short_usage_str = 'block.JUNGLE_FENCE_GATE'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_IN_WALL = BooleanProperty('in_wall'); ALL_PROPERTIES.append(PROPERTY_IN_WALL)
    IN_WALL_TRUE  = PROPERTY_IN_WALL.value(True, 'IN_WALL_TRUE')
    IN_WALL_FALSE = PROPERTY_IN_WALL.value(False, 'IN_WALL_FALSE')

    PROPERTY_OPEN = BooleanProperty('open'); ALL_PROPERTIES.append(PROPERTY_OPEN)
    OPEN_TRUE  = PROPERTY_OPEN.value(True, 'OPEN_TRUE')
    OPEN_FALSE = PROPERTY_OPEN.value(False, 'OPEN_FALSE')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class JungleStairs(BlockDefinition):
    def __init__(self):
        self.id = 136
        self.name = 'jungle_stairs'
        self.short_usage_str = 'block.JUNGLE_STAIRS'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_SHAPE = EnumProperty('shape'); ALL_PROPERTIES.append(PROPERTY_SHAPE)
    SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight', 'SHAPE_STRAIGHT')
    SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left', 'SHAPE_INNER_LEFT')
    SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right', 'SHAPE_INNER_RIGHT')
    SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left', 'SHAPE_OUTER_LEFT')
    SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right', 'SHAPE_OUTER_RIGHT')


class Ladder(BlockDefinition):
    def __init__(self):
        self.id = 65
        self.name = 'ladder'
        self.short_usage_str = 'block.LADDER'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class LapisBlock(BlockDefinition):
    def __init__(self):
        self.id = 22
        self.name = 'lapis_block'
        self.short_usage_str = 'block.LAPIS_BLOCK'

    ALL_PROPERTIES = []


class LapisOre(BlockDefinition):
    def __init__(self):
        self.id = 21
        self.name = 'lapis_ore'
        self.short_usage_str = 'block.LAPIS_ORE'

    ALL_PROPERTIES = []


class Lava(BlockDefinition):
    def __init__(self):
        self.id = 11
        self.name = 'lava'
        self.short_usage_str = 'block.LAVA'

    ALL_PROPERTIES = []

    PROPERTY_LEVEL = IntegerProperty('level'); ALL_PROPERTIES.append(PROPERTY_LEVEL)
    LEVEL_0  = PROPERTY_LEVEL.value(0, 'LEVEL_0')
    LEVEL_1  = PROPERTY_LEVEL.value(1, 'LEVEL_1')
    LEVEL_2  = PROPERTY_LEVEL.value(2, 'LEVEL_2')
    LEVEL_3  = PROPERTY_LEVEL.value(3, 'LEVEL_3')
    LEVEL_4  = PROPERTY_LEVEL.value(4, 'LEVEL_4')
    LEVEL_5  = PROPERTY_LEVEL.value(5, 'LEVEL_5')
    LEVEL_6  = PROPERTY_LEVEL.value(6, 'LEVEL_6')
    LEVEL_7  = PROPERTY_LEVEL.value(7, 'LEVEL_7')
    LEVEL_8  = PROPERTY_LEVEL.value(8, 'LEVEL_8')
    LEVEL_9  = PROPERTY_LEVEL.value(9, 'LEVEL_9')
    LEVEL_10 = PROPERTY_LEVEL.value(10, 'LEVEL_10')
    LEVEL_11 = PROPERTY_LEVEL.value(11, 'LEVEL_11')
    LEVEL_12 = PROPERTY_LEVEL.value(12, 'LEVEL_12')
    LEVEL_13 = PROPERTY_LEVEL.value(13, 'LEVEL_13')
    LEVEL_14 = PROPERTY_LEVEL.value(14, 'LEVEL_14')
    LEVEL_15 = PROPERTY_LEVEL.value(15, 'LEVEL_15')


class Leaves(BlockDefinition):
    def __init__(self):
        self.id = 18
        self.name = 'leaves'
        self.short_usage_str = 'block.LEAVES'

    ALL_PROPERTIES = []

    PROPERTY_CHECK_DECAY = BooleanProperty('check_decay'); ALL_PROPERTIES.append(PROPERTY_CHECK_DECAY)
    CHECK_DECAY_TRUE  = PROPERTY_CHECK_DECAY.value(True, 'CHECK_DECAY_TRUE')
    CHECK_DECAY_FALSE = PROPERTY_CHECK_DECAY.value(False, 'CHECK_DECAY_FALSE')

    PROPERTY_DECAYABLE = BooleanProperty('decayable'); ALL_PROPERTIES.append(PROPERTY_DECAYABLE)
    DECAYABLE_TRUE  = PROPERTY_DECAYABLE.value(True, 'DECAYABLE_TRUE')
    DECAYABLE_FALSE = PROPERTY_DECAYABLE.value(False, 'DECAYABLE_FALSE')

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_OAK    = PROPERTY_VARIANT.value('oak', 'VARIANT_OAK')
    VARIANT_SPRUCE = PROPERTY_VARIANT.value('spruce', 'VARIANT_SPRUCE')
    VARIANT_BIRCH  = PROPERTY_VARIANT.value('birch', 'VARIANT_BIRCH')
    VARIANT_JUNGLE = PROPERTY_VARIANT.value('jungle', 'VARIANT_JUNGLE')


class Leaves2(BlockDefinition):
    def __init__(self):
        self.id = 161
        self.name = 'leaves2'
        self.short_usage_str = 'block.LEAVES2'

    ALL_PROPERTIES = []

    PROPERTY_CHECK_DECAY = BooleanProperty('check_decay'); ALL_PROPERTIES.append(PROPERTY_CHECK_DECAY)
    CHECK_DECAY_TRUE  = PROPERTY_CHECK_DECAY.value(True, 'CHECK_DECAY_TRUE')
    CHECK_DECAY_FALSE = PROPERTY_CHECK_DECAY.value(False, 'CHECK_DECAY_FALSE')

    PROPERTY_DECAYABLE = BooleanProperty('decayable'); ALL_PROPERTIES.append(PROPERTY_DECAYABLE)
    DECAYABLE_TRUE  = PROPERTY_DECAYABLE.value(True, 'DECAYABLE_TRUE')
    DECAYABLE_FALSE = PROPERTY_DECAYABLE.value(False, 'DECAYABLE_FALSE')

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_ACACIA   = PROPERTY_VARIANT.value('acacia', 'VARIANT_ACACIA')
    VARIANT_DARK_OAK = PROPERTY_VARIANT.value('dark_oak', 'VARIANT_DARK_OAK')


class Lever(BlockDefinition):
    def __init__(self):
        self.id = 69
        self.name = 'lever'
        self.short_usage_str = 'block.LEVER'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_DOWN_X = PROPERTY_FACING.value('down_x', 'FACING_DOWN_X')
    FACING_EAST   = PROPERTY_FACING.value('east', 'FACING_EAST')
    FACING_WEST   = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_SOUTH  = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_NORTH  = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_UP_Z   = PROPERTY_FACING.value('up_z', 'FACING_UP_Z')
    FACING_UP_X   = PROPERTY_FACING.value('up_x', 'FACING_UP_X')
    FACING_DOWN_Z = PROPERTY_FACING.value('down_z', 'FACING_DOWN_Z')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class LightWeightedPressurePlate(BlockDefinition):
    def __init__(self):
        self.id = 147
        self.name = 'light_weighted_pressure_plate'
        self.short_usage_str = 'block.LIGHT_WEIGHTED_PRESSURE_PLATE'

    ALL_PROPERTIES = []

    PROPERTY_POWER = IntegerProperty('power'); ALL_PROPERTIES.append(PROPERTY_POWER)
    POWER_0  = PROPERTY_POWER.value(0, 'POWER_0')
    POWER_1  = PROPERTY_POWER.value(1, 'POWER_1')
    POWER_2  = PROPERTY_POWER.value(2, 'POWER_2')
    POWER_3  = PROPERTY_POWER.value(3, 'POWER_3')
    POWER_4  = PROPERTY_POWER.value(4, 'POWER_4')
    POWER_5  = PROPERTY_POWER.value(5, 'POWER_5')
    POWER_6  = PROPERTY_POWER.value(6, 'POWER_6')
    POWER_7  = PROPERTY_POWER.value(7, 'POWER_7')
    POWER_8  = PROPERTY_POWER.value(8, 'POWER_8')
    POWER_9  = PROPERTY_POWER.value(9, 'POWER_9')
    POWER_10 = PROPERTY_POWER.value(10, 'POWER_10')
    POWER_11 = PROPERTY_POWER.value(11, 'POWER_11')
    POWER_12 = PROPERTY_POWER.value(12, 'POWER_12')
    POWER_13 = PROPERTY_POWER.value(13, 'POWER_13')
    POWER_14 = PROPERTY_POWER.value(14, 'POWER_14')
    POWER_15 = PROPERTY_POWER.value(15, 'POWER_15')


class LitFurnace(BlockDefinition):
    def __init__(self):
        self.id = 62
        self.name = 'lit_furnace'
        self.short_usage_str = 'block.LIT_FURNACE'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class LitPumpkin(BlockDefinition):
    def __init__(self):
        self.id = 91
        self.name = 'lit_pumpkin'
        self.short_usage_str = 'block.LIT_PUMPKIN'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class LitRedstoneLamp(BlockDefinition):
    def __init__(self):
        self.id = 124
        self.name = 'lit_redstone_lamp'
        self.short_usage_str = 'block.LIT_REDSTONE_LAMP'

    ALL_PROPERTIES = []


class LitRedstoneOre(BlockDefinition):
    def __init__(self):
        self.id = 74
        self.name = 'lit_redstone_ore'
        self.short_usage_str = 'block.LIT_REDSTONE_ORE'

    ALL_PROPERTIES = []


class Log(BlockDefinition):
    def __init__(self):
        self.id = 17
        self.name = 'log'
        self.short_usage_str = 'block.LOG'

    ALL_PROPERTIES = []

    PROPERTY_AXIS = EnumProperty('axis'); ALL_PROPERTIES.append(PROPERTY_AXIS)
    AXIS_X    = PROPERTY_AXIS.value('x', 'AXIS_X')
    AXIS_Y    = PROPERTY_AXIS.value('y', 'AXIS_Y')
    AXIS_Z    = PROPERTY_AXIS.value('z', 'AXIS_Z')
    AXIS_NONE = PROPERTY_AXIS.value('none', 'AXIS_NONE')

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_OAK    = PROPERTY_VARIANT.value('oak', 'VARIANT_OAK')
    VARIANT_SPRUCE = PROPERTY_VARIANT.value('spruce', 'VARIANT_SPRUCE')
    VARIANT_BIRCH  = PROPERTY_VARIANT.value('birch', 'VARIANT_BIRCH')
    VARIANT_JUNGLE = PROPERTY_VARIANT.value('jungle', 'VARIANT_JUNGLE')


class Log2(BlockDefinition):
    def __init__(self):
        self.id = 162
        self.name = 'log2'
        self.short_usage_str = 'block.LOG2'

    ALL_PROPERTIES = []

    PROPERTY_AXIS = EnumProperty('axis'); ALL_PROPERTIES.append(PROPERTY_AXIS)
    AXIS_X    = PROPERTY_AXIS.value('x', 'AXIS_X')
    AXIS_Y    = PROPERTY_AXIS.value('y', 'AXIS_Y')
    AXIS_Z    = PROPERTY_AXIS.value('z', 'AXIS_Z')
    AXIS_NONE = PROPERTY_AXIS.value('none', 'AXIS_NONE')

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_ACACIA   = PROPERTY_VARIANT.value('acacia', 'VARIANT_ACACIA')
    VARIANT_DARK_OAK = PROPERTY_VARIANT.value('dark_oak', 'VARIANT_DARK_OAK')


class MelonBlock(BlockDefinition):
    def __init__(self):
        self.id = 103
        self.name = 'melon_block'
        self.short_usage_str = 'block.MELON_BLOCK'

    ALL_PROPERTIES = []


class MelonStem(BlockDefinition):
    def __init__(self):
        self.id = 105
        self.name = 'melon_stem'
        self.short_usage_str = 'block.MELON_STEM'

    ALL_PROPERTIES = []

    PROPERTY_AGE = IntegerProperty('age'); ALL_PROPERTIES.append(PROPERTY_AGE)
    AGE_0 = PROPERTY_AGE.value(0, 'AGE_0')
    AGE_1 = PROPERTY_AGE.value(1, 'AGE_1')
    AGE_2 = PROPERTY_AGE.value(2, 'AGE_2')
    AGE_3 = PROPERTY_AGE.value(3, 'AGE_3')
    AGE_4 = PROPERTY_AGE.value(4, 'AGE_4')
    AGE_5 = PROPERTY_AGE.value(5, 'AGE_5')
    AGE_6 = PROPERTY_AGE.value(6, 'AGE_6')
    AGE_7 = PROPERTY_AGE.value(7, 'AGE_7')

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_UP    = PROPERTY_FACING.value('up', 'FACING_UP')
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class MobSpawner(BlockDefinition):
    def __init__(self):
        self.id = 52
        self.name = 'mob_spawner'
        self.short_usage_str = 'block.MOB_SPAWNER'

    ALL_PROPERTIES = []


class MonsterEgg(BlockDefinition):
    def __init__(self):
        self.id = 97
        self.name = 'monster_egg'
        self.short_usage_str = 'block.MONSTER_EGG'

    ALL_PROPERTIES = []

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_STONE          = PROPERTY_VARIANT.value('stone', 'VARIANT_STONE')
    VARIANT_COBBLESTONE    = PROPERTY_VARIANT.value('cobblestone', 'VARIANT_COBBLESTONE')
    VARIANT_STONE_BRICK    = PROPERTY_VARIANT.value('stone_brick', 'VARIANT_STONE_BRICK')
    VARIANT_MOSSY_BRICK    = PROPERTY_VARIANT.value('mossy_brick', 'VARIANT_MOSSY_BRICK')
    VARIANT_CRACKED_BRICK  = PROPERTY_VARIANT.value('cracked_brick', 'VARIANT_CRACKED_BRICK')
    VARIANT_CHISELED_BRICK = PROPERTY_VARIANT.value('chiseled_brick', 'VARIANT_CHISELED_BRICK')


class MossyCobblestone(BlockDefinition):
    def __init__(self):
        self.id = 48
        self.name = 'mossy_cobblestone'
        self.short_usage_str = 'block.MOSSY_COBBLESTONE'

    ALL_PROPERTIES = []


class Mycelium(BlockDefinition):
    def __init__(self):
        self.id = 110
        self.name = 'mycelium'
        self.short_usage_str = 'block.MYCELIUM'

    ALL_PROPERTIES = []

    PROPERTY_SNOWY = BooleanProperty('snowy'); ALL_PROPERTIES.append(PROPERTY_SNOWY)
    SNOWY_TRUE  = PROPERTY_SNOWY.value(True, 'SNOWY_TRUE')
    SNOWY_FALSE = PROPERTY_SNOWY.value(False, 'SNOWY_FALSE')


class NetherBrick(BlockDefinition):
    def __init__(self):
        self.id = 112
        self.name = 'nether_brick'
        self.short_usage_str = 'block.NETHER_BRICK'

    ALL_PROPERTIES = []


class NetherBrickFence(BlockDefinition):
    def __init__(self):
        self.id = 113
        self.name = 'nether_brick_fence'
        self.short_usage_str = 'block.NETHER_BRICK_FENCE'

    ALL_PROPERTIES = []

    PROPERTY_EAST = BooleanProperty('east'); ALL_PROPERTIES.append(PROPERTY_EAST)
    EAST_TRUE  = PROPERTY_EAST.value(True, 'EAST_TRUE')
    EAST_FALSE = PROPERTY_EAST.value(False, 'EAST_FALSE')

    PROPERTY_NORTH = BooleanProperty('north'); ALL_PROPERTIES.append(PROPERTY_NORTH)
    NORTH_TRUE  = PROPERTY_NORTH.value(True, 'NORTH_TRUE')
    NORTH_FALSE = PROPERTY_NORTH.value(False, 'NORTH_FALSE')

    PROPERTY_SOUTH = BooleanProperty('south'); ALL_PROPERTIES.append(PROPERTY_SOUTH)
    SOUTH_TRUE  = PROPERTY_SOUTH.value(True, 'SOUTH_TRUE')
    SOUTH_FALSE = PROPERTY_SOUTH.value(False, 'SOUTH_FALSE')

    PROPERTY_WEST = BooleanProperty('west'); ALL_PROPERTIES.append(PROPERTY_WEST)
    WEST_TRUE  = PROPERTY_WEST.value(True, 'WEST_TRUE')
    WEST_FALSE = PROPERTY_WEST.value(False, 'WEST_FALSE')


class NetherBrickStairs(BlockDefinition):
    def __init__(self):
        self.id = 114
        self.name = 'nether_brick_stairs'
        self.short_usage_str = 'block.NETHER_BRICK_STAIRS'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_SHAPE = EnumProperty('shape'); ALL_PROPERTIES.append(PROPERTY_SHAPE)
    SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight', 'SHAPE_STRAIGHT')
    SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left', 'SHAPE_INNER_LEFT')
    SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right', 'SHAPE_INNER_RIGHT')
    SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left', 'SHAPE_OUTER_LEFT')
    SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right', 'SHAPE_OUTER_RIGHT')


class NetherWart(BlockDefinition):
    def __init__(self):
        self.id = 115
        self.name = 'nether_wart'
        self.short_usage_str = 'block.NETHER_WART'

    ALL_PROPERTIES = []

    PROPERTY_AGE = IntegerProperty('age'); ALL_PROPERTIES.append(PROPERTY_AGE)
    AGE_0 = PROPERTY_AGE.value(0, 'AGE_0')
    AGE_1 = PROPERTY_AGE.value(1, 'AGE_1')
    AGE_2 = PROPERTY_AGE.value(2, 'AGE_2')
    AGE_3 = PROPERTY_AGE.value(3, 'AGE_3')


class Netherrack(BlockDefinition):
    def __init__(self):
        self.id = 87
        self.name = 'netherrack'
        self.short_usage_str = 'block.NETHERRACK'

    ALL_PROPERTIES = []


class Noteblock(BlockDefinition):
    def __init__(self):
        self.id = 25
        self.name = 'noteblock'
        self.short_usage_str = 'block.NOTEBLOCK'

    ALL_PROPERTIES = []


class OakStairs(BlockDefinition):
    def __init__(self):
        self.id = 53
        self.name = 'oak_stairs'
        self.short_usage_str = 'block.OAK_STAIRS'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_SHAPE = EnumProperty('shape'); ALL_PROPERTIES.append(PROPERTY_SHAPE)
    SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight', 'SHAPE_STRAIGHT')
    SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left', 'SHAPE_INNER_LEFT')
    SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right', 'SHAPE_INNER_RIGHT')
    SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left', 'SHAPE_OUTER_LEFT')
    SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right', 'SHAPE_OUTER_RIGHT')


class Obsidian(BlockDefinition):
    def __init__(self):
        self.id = 49
        self.name = 'obsidian'
        self.short_usage_str = 'block.OBSIDIAN'

    ALL_PROPERTIES = []


class PackedIce(BlockDefinition):
    def __init__(self):
        self.id = 174
        self.name = 'packed_ice'
        self.short_usage_str = 'block.PACKED_ICE'

    ALL_PROPERTIES = []


class Piston(BlockDefinition):
    def __init__(self):
        self.id = 33
        self.name = 'piston'
        self.short_usage_str = 'block.PISTON'

    ALL_PROPERTIES = []

    PROPERTY_EXTENDED = BooleanProperty('extended'); ALL_PROPERTIES.append(PROPERTY_EXTENDED)
    EXTENDED_TRUE  = PROPERTY_EXTENDED.value(True, 'EXTENDED_TRUE')
    EXTENDED_FALSE = PROPERTY_EXTENDED.value(False, 'EXTENDED_FALSE')

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_DOWN  = PROPERTY_FACING.value('down', 'FACING_DOWN')
    FACING_UP    = PROPERTY_FACING.value('up', 'FACING_UP')
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class PistonExtension(BlockDefinition):
    def __init__(self):
        self.id = 36
        self.name = 'piston_extension'
        self.short_usage_str = 'block.PISTON_EXTENSION'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_DOWN  = PROPERTY_FACING.value('down', 'FACING_DOWN')
    FACING_UP    = PROPERTY_FACING.value('up', 'FACING_UP')
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_TYPE = EnumProperty('type'); ALL_PROPERTIES.append(PROPERTY_TYPE)
    TYPE_NORMAL = PROPERTY_TYPE.value('normal', 'TYPE_NORMAL')
    TYPE_STICKY = PROPERTY_TYPE.value('sticky', 'TYPE_STICKY')


class PistonHead(BlockDefinition):
    def __init__(self):
        self.id = 34
        self.name = 'piston_head'
        self.short_usage_str = 'block.PISTON_HEAD'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_DOWN  = PROPERTY_FACING.value('down', 'FACING_DOWN')
    FACING_UP    = PROPERTY_FACING.value('up', 'FACING_UP')
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_SHORT = BooleanProperty('short'); ALL_PROPERTIES.append(PROPERTY_SHORT)
    SHORT_TRUE  = PROPERTY_SHORT.value(True, 'SHORT_TRUE')
    SHORT_FALSE = PROPERTY_SHORT.value(False, 'SHORT_FALSE')

    PROPERTY_TYPE = EnumProperty('type'); ALL_PROPERTIES.append(PROPERTY_TYPE)
    TYPE_NORMAL = PROPERTY_TYPE.value('normal', 'TYPE_NORMAL')
    TYPE_STICKY = PROPERTY_TYPE.value('sticky', 'TYPE_STICKY')


class Planks(BlockDefinition):
    def __init__(self):
        self.id = 5
        self.name = 'planks'
        self.short_usage_str = 'block.PLANKS'

    ALL_PROPERTIES = []

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_OAK      = PROPERTY_VARIANT.value('oak', 'VARIANT_OAK')
    VARIANT_SPRUCE   = PROPERTY_VARIANT.value('spruce', 'VARIANT_SPRUCE')
    VARIANT_BIRCH    = PROPERTY_VARIANT.value('birch', 'VARIANT_BIRCH')
    VARIANT_JUNGLE   = PROPERTY_VARIANT.value('jungle', 'VARIANT_JUNGLE')
    VARIANT_ACACIA   = PROPERTY_VARIANT.value('acacia', 'VARIANT_ACACIA')
    VARIANT_DARK_OAK = PROPERTY_VARIANT.value('dark_oak', 'VARIANT_DARK_OAK')


class Portal(BlockDefinition):
    def __init__(self):
        self.id = 90
        self.name = 'portal'
        self.short_usage_str = 'block.PORTAL'

    ALL_PROPERTIES = []

    PROPERTY_AXIS = EnumProperty('axis'); ALL_PROPERTIES.append(PROPERTY_AXIS)
    AXIS_X = PROPERTY_AXIS.value('x', 'AXIS_X')
    AXIS_Z = PROPERTY_AXIS.value('z', 'AXIS_Z')


class Potatoes(BlockDefinition):
    def __init__(self):
        self.id = 142
        self.name = 'potatoes'
        self.short_usage_str = 'block.POTATOES'

    ALL_PROPERTIES = []

    PROPERTY_AGE = IntegerProperty('age'); ALL_PROPERTIES.append(PROPERTY_AGE)
    AGE_0 = PROPERTY_AGE.value(0, 'AGE_0')
    AGE_1 = PROPERTY_AGE.value(1, 'AGE_1')
    AGE_2 = PROPERTY_AGE.value(2, 'AGE_2')
    AGE_3 = PROPERTY_AGE.value(3, 'AGE_3')
    AGE_4 = PROPERTY_AGE.value(4, 'AGE_4')
    AGE_5 = PROPERTY_AGE.value(5, 'AGE_5')
    AGE_6 = PROPERTY_AGE.value(6, 'AGE_6')
    AGE_7 = PROPERTY_AGE.value(7, 'AGE_7')


class PoweredComparator(BlockDefinition):
    def __init__(self):
        self.id = 150
        self.name = 'powered_comparator'
        self.short_usage_str = 'block.POWERED_COMPARATOR'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_MODE = EnumProperty('mode'); ALL_PROPERTIES.append(PROPERTY_MODE)
    MODE_COMPARE  = PROPERTY_MODE.value('compare', 'MODE_COMPARE')
    MODE_SUBTRACT = PROPERTY_MODE.value('subtract', 'MODE_SUBTRACT')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class PoweredRepeater(BlockDefinition):
    def __init__(self):
        self.id = 94
        self.name = 'powered_repeater'
        self.short_usage_str = 'block.POWERED_REPEATER'

    ALL_PROPERTIES = []

    PROPERTY_DELAY = IntegerProperty('delay'); ALL_PROPERTIES.append(PROPERTY_DELAY)
    DELAY_1 = PROPERTY_DELAY.value(1, 'DELAY_1')
    DELAY_2 = PROPERTY_DELAY.value(2, 'DELAY_2')
    DELAY_3 = PROPERTY_DELAY.value(3, 'DELAY_3')
    DELAY_4 = PROPERTY_DELAY.value(4, 'DELAY_4')

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_LOCKED = BooleanProperty('locked'); ALL_PROPERTIES.append(PROPERTY_LOCKED)
    LOCKED_TRUE  = PROPERTY_LOCKED.value(True, 'LOCKED_TRUE')
    LOCKED_FALSE = PROPERTY_LOCKED.value(False, 'LOCKED_FALSE')


class Prismarine(BlockDefinition):
    def __init__(self):
        self.id = 168
        self.name = 'prismarine'
        self.short_usage_str = 'block.PRISMARINE'

    ALL_PROPERTIES = []

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_PRISMARINE        = PROPERTY_VARIANT.value('prismarine', 'VARIANT_PRISMARINE')
    VARIANT_PRISMARINE_BRICKS = PROPERTY_VARIANT.value('prismarine_bricks', 'VARIANT_PRISMARINE_BRICKS')
    VARIANT_DARK_PRISMARINE   = PROPERTY_VARIANT.value('dark_prismarine', 'VARIANT_DARK_PRISMARINE')


class Pumpkin(BlockDefinition):
    def __init__(self):
        self.id = 86
        self.name = 'pumpkin'
        self.short_usage_str = 'block.PUMPKIN'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class PumpkinStem(BlockDefinition):
    def __init__(self):
        self.id = 104
        self.name = 'pumpkin_stem'
        self.short_usage_str = 'block.PUMPKIN_STEM'

    ALL_PROPERTIES = []

    PROPERTY_AGE = IntegerProperty('age'); ALL_PROPERTIES.append(PROPERTY_AGE)
    AGE_0 = PROPERTY_AGE.value(0, 'AGE_0')
    AGE_1 = PROPERTY_AGE.value(1, 'AGE_1')
    AGE_2 = PROPERTY_AGE.value(2, 'AGE_2')
    AGE_3 = PROPERTY_AGE.value(3, 'AGE_3')
    AGE_4 = PROPERTY_AGE.value(4, 'AGE_4')
    AGE_5 = PROPERTY_AGE.value(5, 'AGE_5')
    AGE_6 = PROPERTY_AGE.value(6, 'AGE_6')
    AGE_7 = PROPERTY_AGE.value(7, 'AGE_7')

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_UP    = PROPERTY_FACING.value('up', 'FACING_UP')
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class QuartzBlock(BlockDefinition):
    def __init__(self):
        self.id = 155
        self.name = 'quartz_block'
        self.short_usage_str = 'block.QUARTZ_BLOCK'

    ALL_PROPERTIES = []

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_DEFAULT  = PROPERTY_VARIANT.value('default', 'VARIANT_DEFAULT')
    VARIANT_CHISELED = PROPERTY_VARIANT.value('chiseled', 'VARIANT_CHISELED')
    VARIANT_LINES_Y  = PROPERTY_VARIANT.value('lines_y', 'VARIANT_LINES_Y')
    VARIANT_LINES_X  = PROPERTY_VARIANT.value('lines_x', 'VARIANT_LINES_X')
    VARIANT_LINES_Z  = PROPERTY_VARIANT.value('lines_z', 'VARIANT_LINES_Z')


class QuartzOre(BlockDefinition):
    def __init__(self):
        self.id = 153
        self.name = 'quartz_ore'
        self.short_usage_str = 'block.QUARTZ_ORE'

    ALL_PROPERTIES = []


class QuartzStairs(BlockDefinition):
    def __init__(self):
        self.id = 156
        self.name = 'quartz_stairs'
        self.short_usage_str = 'block.QUARTZ_STAIRS'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_SHAPE = EnumProperty('shape'); ALL_PROPERTIES.append(PROPERTY_SHAPE)
    SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight', 'SHAPE_STRAIGHT')
    SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left', 'SHAPE_INNER_LEFT')
    SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right', 'SHAPE_INNER_RIGHT')
    SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left', 'SHAPE_OUTER_LEFT')
    SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right', 'SHAPE_OUTER_RIGHT')


class Rail(BlockDefinition):
    def __init__(self):
        self.id = 66
        self.name = 'rail'
        self.short_usage_str = 'block.RAIL'

    ALL_PROPERTIES = []

    PROPERTY_SHAPE = EnumProperty('shape'); ALL_PROPERTIES.append(PROPERTY_SHAPE)
    SHAPE_NORTH_SOUTH     = PROPERTY_SHAPE.value('north_south', 'SHAPE_NORTH_SOUTH')
    SHAPE_EAST_WEST       = PROPERTY_SHAPE.value('east_west', 'SHAPE_EAST_WEST')
    SHAPE_ASCENDING_EAST  = PROPERTY_SHAPE.value('ascending_east', 'SHAPE_ASCENDING_EAST')
    SHAPE_ASCENDING_WEST  = PROPERTY_SHAPE.value('ascending_west', 'SHAPE_ASCENDING_WEST')
    SHAPE_ASCENDING_NORTH = PROPERTY_SHAPE.value('ascending_north', 'SHAPE_ASCENDING_NORTH')
    SHAPE_ASCENDING_SOUTH = PROPERTY_SHAPE.value('ascending_south', 'SHAPE_ASCENDING_SOUTH')
    SHAPE_SOUTH_EAST      = PROPERTY_SHAPE.value('south_east', 'SHAPE_SOUTH_EAST')
    SHAPE_SOUTH_WEST      = PROPERTY_SHAPE.value('south_west', 'SHAPE_SOUTH_WEST')
    SHAPE_NORTH_WEST      = PROPERTY_SHAPE.value('north_west', 'SHAPE_NORTH_WEST')
    SHAPE_NORTH_EAST      = PROPERTY_SHAPE.value('north_east', 'SHAPE_NORTH_EAST')


class RedFlower(BlockDefinition):
    def __init__(self):
        self.id = 38
        self.name = 'red_flower'
        self.short_usage_str = 'block.RED_FLOWER'

    ALL_PROPERTIES = []

    PROPERTY_TYPE = EnumProperty('type'); ALL_PROPERTIES.append(PROPERTY_TYPE)
    TYPE_POPPY        = PROPERTY_TYPE.value('poppy', 'TYPE_POPPY')
    TYPE_BLUE_ORCHID  = PROPERTY_TYPE.value('blue_orchid', 'TYPE_BLUE_ORCHID')
    TYPE_ALLIUM       = PROPERTY_TYPE.value('allium', 'TYPE_ALLIUM')
    TYPE_HOUSTONIA    = PROPERTY_TYPE.value('houstonia', 'TYPE_HOUSTONIA')
    TYPE_RED_TULIP    = PROPERTY_TYPE.value('red_tulip', 'TYPE_RED_TULIP')
    TYPE_ORANGE_TULIP = PROPERTY_TYPE.value('orange_tulip', 'TYPE_ORANGE_TULIP')
    TYPE_WHITE_TULIP  = PROPERTY_TYPE.value('white_tulip', 'TYPE_WHITE_TULIP')
    TYPE_PINK_TULIP   = PROPERTY_TYPE.value('pink_tulip', 'TYPE_PINK_TULIP')
    TYPE_OXEYE_DAISY  = PROPERTY_TYPE.value('oxeye_daisy', 'TYPE_OXEYE_DAISY')


class RedMushroom(BlockDefinition):
    def __init__(self):
        self.id = 40
        self.name = 'red_mushroom'
        self.short_usage_str = 'block.RED_MUSHROOM'

    ALL_PROPERTIES = []


class RedMushroomBlock(BlockDefinition):
    def __init__(self):
        self.id = 100
        self.name = 'red_mushroom_block'
        self.short_usage_str = 'block.RED_MUSHROOM_BLOCK'

    ALL_PROPERTIES = []

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_NORTH_WEST  = PROPERTY_VARIANT.value('north_west', 'VARIANT_NORTH_WEST')
    VARIANT_NORTH       = PROPERTY_VARIANT.value('north', 'VARIANT_NORTH')
    VARIANT_NORTH_EAST  = PROPERTY_VARIANT.value('north_east', 'VARIANT_NORTH_EAST')
    VARIANT_WEST        = PROPERTY_VARIANT.value('west', 'VARIANT_WEST')
    VARIANT_CENTER      = PROPERTY_VARIANT.value('center', 'VARIANT_CENTER')
    VARIANT_EAST        = PROPERTY_VARIANT.value('east', 'VARIANT_EAST')
    VARIANT_SOUTH_WEST  = PROPERTY_VARIANT.value('south_west', 'VARIANT_SOUTH_WEST')
    VARIANT_SOUTH       = PROPERTY_VARIANT.value('south', 'VARIANT_SOUTH')
    VARIANT_SOUTH_EAST  = PROPERTY_VARIANT.value('south_east', 'VARIANT_SOUTH_EAST')
    VARIANT_STEM        = PROPERTY_VARIANT.value('stem', 'VARIANT_STEM')
    VARIANT_ALL_INSIDE  = PROPERTY_VARIANT.value('all_inside', 'VARIANT_ALL_INSIDE')
    VARIANT_ALL_OUTSIDE = PROPERTY_VARIANT.value('all_outside', 'VARIANT_ALL_OUTSIDE')
    VARIANT_ALL_STEM    = PROPERTY_VARIANT.value('all_stem', 'VARIANT_ALL_STEM')


class RedSandstone(BlockDefinition):
    def __init__(self):
        self.id = 179
        self.name = 'red_sandstone'
        self.short_usage_str = 'block.RED_SANDSTONE'

    ALL_PROPERTIES = []

    PROPERTY_TYPE = EnumProperty('type'); ALL_PROPERTIES.append(PROPERTY_TYPE)
    TYPE_RED_SANDSTONE          = PROPERTY_TYPE.value('red_sandstone', 'TYPE_RED_SANDSTONE')
    TYPE_CHISELED_RED_SANDSTONE = PROPERTY_TYPE.value('chiseled_red_sandstone', 'TYPE_CHISELED_RED_SANDSTONE')
    TYPE_SMOOTH_RED_SANDSTONE   = PROPERTY_TYPE.value('smooth_red_sandstone', 'TYPE_SMOOTH_RED_SANDSTONE')


class RedSandstoneStairs(BlockDefinition):
    def __init__(self):
        self.id = 180
        self.name = 'red_sandstone_stairs'
        self.short_usage_str = 'block.RED_SANDSTONE_STAIRS'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_SHAPE = EnumProperty('shape'); ALL_PROPERTIES.append(PROPERTY_SHAPE)
    SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight', 'SHAPE_STRAIGHT')
    SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left', 'SHAPE_INNER_LEFT')
    SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right', 'SHAPE_INNER_RIGHT')
    SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left', 'SHAPE_OUTER_LEFT')
    SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right', 'SHAPE_OUTER_RIGHT')


class RedstoneBlock(BlockDefinition):
    def __init__(self):
        self.id = 152
        self.name = 'redstone_block'
        self.short_usage_str = 'block.REDSTONE_BLOCK'

    ALL_PROPERTIES = []


class RedstoneLamp(BlockDefinition):
    def __init__(self):
        self.id = 123
        self.name = 'redstone_lamp'
        self.short_usage_str = 'block.REDSTONE_LAMP'

    ALL_PROPERTIES = []


class RedstoneOre(BlockDefinition):
    def __init__(self):
        self.id = 73
        self.name = 'redstone_ore'
        self.short_usage_str = 'block.REDSTONE_ORE'

    ALL_PROPERTIES = []


class RedstoneTorch(BlockDefinition):
    def __init__(self):
        self.id = 76
        self.name = 'redstone_torch'
        self.short_usage_str = 'block.REDSTONE_TORCH'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_UP    = PROPERTY_FACING.value('up', 'FACING_UP')
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class RedstoneWire(BlockDefinition):
    def __init__(self):
        self.id = 55
        self.name = 'redstone_wire'
        self.short_usage_str = 'block.REDSTONE_WIRE'

    ALL_PROPERTIES = []

    PROPERTY_EAST = EnumProperty('east'); ALL_PROPERTIES.append(PROPERTY_EAST)
    EAST_UP   = PROPERTY_EAST.value('up', 'EAST_UP')
    EAST_SIDE = PROPERTY_EAST.value('side', 'EAST_SIDE')
    EAST_NONE = PROPERTY_EAST.value('none', 'EAST_NONE')

    PROPERTY_NORTH = EnumProperty('north'); ALL_PROPERTIES.append(PROPERTY_NORTH)
    NORTH_UP   = PROPERTY_NORTH.value('up', 'NORTH_UP')
    NORTH_SIDE = PROPERTY_NORTH.value('side', 'NORTH_SIDE')
    NORTH_NONE = PROPERTY_NORTH.value('none', 'NORTH_NONE')

    PROPERTY_POWER = IntegerProperty('power'); ALL_PROPERTIES.append(PROPERTY_POWER)
    POWER_0  = PROPERTY_POWER.value(0, 'POWER_0')
    POWER_1  = PROPERTY_POWER.value(1, 'POWER_1')
    POWER_2  = PROPERTY_POWER.value(2, 'POWER_2')
    POWER_3  = PROPERTY_POWER.value(3, 'POWER_3')
    POWER_4  = PROPERTY_POWER.value(4, 'POWER_4')
    POWER_5  = PROPERTY_POWER.value(5, 'POWER_5')
    POWER_6  = PROPERTY_POWER.value(6, 'POWER_6')
    POWER_7  = PROPERTY_POWER.value(7, 'POWER_7')
    POWER_8  = PROPERTY_POWER.value(8, 'POWER_8')
    POWER_9  = PROPERTY_POWER.value(9, 'POWER_9')
    POWER_10 = PROPERTY_POWER.value(10, 'POWER_10')
    POWER_11 = PROPERTY_POWER.value(11, 'POWER_11')
    POWER_12 = PROPERTY_POWER.value(12, 'POWER_12')
    POWER_13 = PROPERTY_POWER.value(13, 'POWER_13')
    POWER_14 = PROPERTY_POWER.value(14, 'POWER_14')
    POWER_15 = PROPERTY_POWER.value(15, 'POWER_15')

    PROPERTY_SOUTH = EnumProperty('south'); ALL_PROPERTIES.append(PROPERTY_SOUTH)
    SOUTH_UP   = PROPERTY_SOUTH.value('up', 'SOUTH_UP')
    SOUTH_SIDE = PROPERTY_SOUTH.value('side', 'SOUTH_SIDE')
    SOUTH_NONE = PROPERTY_SOUTH.value('none', 'SOUTH_NONE')

    PROPERTY_WEST = EnumProperty('west'); ALL_PROPERTIES.append(PROPERTY_WEST)
    WEST_UP   = PROPERTY_WEST.value('up', 'WEST_UP')
    WEST_SIDE = PROPERTY_WEST.value('side', 'WEST_SIDE')
    WEST_NONE = PROPERTY_WEST.value('none', 'WEST_NONE')


class Reeds(BlockDefinition):
    def __init__(self):
        self.id = 83
        self.name = 'reeds'
        self.short_usage_str = 'block.REEDS'

    ALL_PROPERTIES = []

    PROPERTY_AGE = IntegerProperty('age'); ALL_PROPERTIES.append(PROPERTY_AGE)
    AGE_0  = PROPERTY_AGE.value(0, 'AGE_0')
    AGE_1  = PROPERTY_AGE.value(1, 'AGE_1')
    AGE_2  = PROPERTY_AGE.value(2, 'AGE_2')
    AGE_3  = PROPERTY_AGE.value(3, 'AGE_3')
    AGE_4  = PROPERTY_AGE.value(4, 'AGE_4')
    AGE_5  = PROPERTY_AGE.value(5, 'AGE_5')
    AGE_6  = PROPERTY_AGE.value(6, 'AGE_6')
    AGE_7  = PROPERTY_AGE.value(7, 'AGE_7')
    AGE_8  = PROPERTY_AGE.value(8, 'AGE_8')
    AGE_9  = PROPERTY_AGE.value(9, 'AGE_9')
    AGE_10 = PROPERTY_AGE.value(10, 'AGE_10')
    AGE_11 = PROPERTY_AGE.value(11, 'AGE_11')
    AGE_12 = PROPERTY_AGE.value(12, 'AGE_12')
    AGE_13 = PROPERTY_AGE.value(13, 'AGE_13')
    AGE_14 = PROPERTY_AGE.value(14, 'AGE_14')
    AGE_15 = PROPERTY_AGE.value(15, 'AGE_15')


class Sand(BlockDefinition):
    def __init__(self):
        self.id = 12
        self.name = 'sand'
        self.short_usage_str = 'block.SAND'

    ALL_PROPERTIES = []

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_SAND     = PROPERTY_VARIANT.value('sand', 'VARIANT_SAND')
    VARIANT_RED_SAND = PROPERTY_VARIANT.value('red_sand', 'VARIANT_RED_SAND')


class Sandstone(BlockDefinition):
    def __init__(self):
        self.id = 24
        self.name = 'sandstone'
        self.short_usage_str = 'block.SANDSTONE'

    ALL_PROPERTIES = []

    PROPERTY_TYPE = EnumProperty('type'); ALL_PROPERTIES.append(PROPERTY_TYPE)
    TYPE_SANDSTONE          = PROPERTY_TYPE.value('sandstone', 'TYPE_SANDSTONE')
    TYPE_CHISELED_SANDSTONE = PROPERTY_TYPE.value('chiseled_sandstone', 'TYPE_CHISELED_SANDSTONE')
    TYPE_SMOOTH_SANDSTONE   = PROPERTY_TYPE.value('smooth_sandstone', 'TYPE_SMOOTH_SANDSTONE')


class SandstoneStairs(BlockDefinition):
    def __init__(self):
        self.id = 128
        self.name = 'sandstone_stairs'
        self.short_usage_str = 'block.SANDSTONE_STAIRS'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_SHAPE = EnumProperty('shape'); ALL_PROPERTIES.append(PROPERTY_SHAPE)
    SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight', 'SHAPE_STRAIGHT')
    SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left', 'SHAPE_INNER_LEFT')
    SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right', 'SHAPE_INNER_RIGHT')
    SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left', 'SHAPE_OUTER_LEFT')
    SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right', 'SHAPE_OUTER_RIGHT')


class Sapling(BlockDefinition):
    def __init__(self):
        self.id = 6
        self.name = 'sapling'
        self.short_usage_str = 'block.SAPLING'

    ALL_PROPERTIES = []

    PROPERTY_STAGE = IntegerProperty('stage'); ALL_PROPERTIES.append(PROPERTY_STAGE)
    STAGE_0 = PROPERTY_STAGE.value(0, 'STAGE_0')
    STAGE_1 = PROPERTY_STAGE.value(1, 'STAGE_1')

    PROPERTY_TYPE = EnumProperty('type'); ALL_PROPERTIES.append(PROPERTY_TYPE)
    TYPE_OAK      = PROPERTY_TYPE.value('oak', 'TYPE_OAK')
    TYPE_SPRUCE   = PROPERTY_TYPE.value('spruce', 'TYPE_SPRUCE')
    TYPE_BIRCH    = PROPERTY_TYPE.value('birch', 'TYPE_BIRCH')
    TYPE_JUNGLE   = PROPERTY_TYPE.value('jungle', 'TYPE_JUNGLE')
    TYPE_ACACIA   = PROPERTY_TYPE.value('acacia', 'TYPE_ACACIA')
    TYPE_DARK_OAK = PROPERTY_TYPE.value('dark_oak', 'TYPE_DARK_OAK')


class SeaLantern(BlockDefinition):
    def __init__(self):
        self.id = 169
        self.name = 'sea_lantern'
        self.short_usage_str = 'block.SEA_LANTERN'

    ALL_PROPERTIES = []


class Skull(BlockDefinition):
    def __init__(self):
        self.id = 144
        self.name = 'skull'
        self.short_usage_str = 'block.SKULL'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_DOWN  = PROPERTY_FACING.value('down', 'FACING_DOWN')
    FACING_UP    = PROPERTY_FACING.value('up', 'FACING_UP')
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_NODROP = BooleanProperty('nodrop'); ALL_PROPERTIES.append(PROPERTY_NODROP)
    NODROP_TRUE  = PROPERTY_NODROP.value(True, 'NODROP_TRUE')
    NODROP_FALSE = PROPERTY_NODROP.value(False, 'NODROP_FALSE')


class Slime(BlockDefinition):
    def __init__(self):
        self.id = 165
        self.name = 'slime'
        self.short_usage_str = 'block.SLIME'

    ALL_PROPERTIES = []


class Snow(BlockDefinition):
    def __init__(self):
        self.id = 80
        self.name = 'snow'
        self.short_usage_str = 'block.SNOW'

    ALL_PROPERTIES = []


class SnowLayer(BlockDefinition):
    def __init__(self):
        self.id = 78
        self.name = 'snow_layer'
        self.short_usage_str = 'block.SNOW_LAYER'

    ALL_PROPERTIES = []

    PROPERTY_LAYERS = IntegerProperty('layers'); ALL_PROPERTIES.append(PROPERTY_LAYERS)
    LAYERS_1 = PROPERTY_LAYERS.value(1, 'LAYERS_1')
    LAYERS_2 = PROPERTY_LAYERS.value(2, 'LAYERS_2')
    LAYERS_3 = PROPERTY_LAYERS.value(3, 'LAYERS_3')
    LAYERS_4 = PROPERTY_LAYERS.value(4, 'LAYERS_4')
    LAYERS_5 = PROPERTY_LAYERS.value(5, 'LAYERS_5')
    LAYERS_6 = PROPERTY_LAYERS.value(6, 'LAYERS_6')
    LAYERS_7 = PROPERTY_LAYERS.value(7, 'LAYERS_7')
    LAYERS_8 = PROPERTY_LAYERS.value(8, 'LAYERS_8')


class SoulSand(BlockDefinition):
    def __init__(self):
        self.id = 88
        self.name = 'soul_sand'
        self.short_usage_str = 'block.SOUL_SAND'

    ALL_PROPERTIES = []


class Sponge(BlockDefinition):
    def __init__(self):
        self.id = 19
        self.name = 'sponge'
        self.short_usage_str = 'block.SPONGE'

    ALL_PROPERTIES = []

    PROPERTY_WET = BooleanProperty('wet'); ALL_PROPERTIES.append(PROPERTY_WET)
    WET_TRUE  = PROPERTY_WET.value(True, 'WET_TRUE')
    WET_FALSE = PROPERTY_WET.value(False, 'WET_FALSE')


class SpruceDoor(BlockDefinition):
    def __init__(self):
        self.id = 193
        self.name = 'spruce_door'
        self.short_usage_str = 'block.SPRUCE_DOOR'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_UPPER = PROPERTY_HALF.value('upper', 'HALF_UPPER')
    HALF_LOWER = PROPERTY_HALF.value('lower', 'HALF_LOWER')

    PROPERTY_HINGE = EnumProperty('hinge'); ALL_PROPERTIES.append(PROPERTY_HINGE)
    HINGE_LEFT  = PROPERTY_HINGE.value('left', 'HINGE_LEFT')
    HINGE_RIGHT = PROPERTY_HINGE.value('right', 'HINGE_RIGHT')

    PROPERTY_OPEN = BooleanProperty('open'); ALL_PROPERTIES.append(PROPERTY_OPEN)
    OPEN_TRUE  = PROPERTY_OPEN.value(True, 'OPEN_TRUE')
    OPEN_FALSE = PROPERTY_OPEN.value(False, 'OPEN_FALSE')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class SpruceFence(BlockDefinition):
    def __init__(self):
        self.id = 188
        self.name = 'spruce_fence'
        self.short_usage_str = 'block.SPRUCE_FENCE'

    ALL_PROPERTIES = []

    PROPERTY_EAST = BooleanProperty('east'); ALL_PROPERTIES.append(PROPERTY_EAST)
    EAST_TRUE  = PROPERTY_EAST.value(True, 'EAST_TRUE')
    EAST_FALSE = PROPERTY_EAST.value(False, 'EAST_FALSE')

    PROPERTY_NORTH = BooleanProperty('north'); ALL_PROPERTIES.append(PROPERTY_NORTH)
    NORTH_TRUE  = PROPERTY_NORTH.value(True, 'NORTH_TRUE')
    NORTH_FALSE = PROPERTY_NORTH.value(False, 'NORTH_FALSE')

    PROPERTY_SOUTH = BooleanProperty('south'); ALL_PROPERTIES.append(PROPERTY_SOUTH)
    SOUTH_TRUE  = PROPERTY_SOUTH.value(True, 'SOUTH_TRUE')
    SOUTH_FALSE = PROPERTY_SOUTH.value(False, 'SOUTH_FALSE')

    PROPERTY_WEST = BooleanProperty('west'); ALL_PROPERTIES.append(PROPERTY_WEST)
    WEST_TRUE  = PROPERTY_WEST.value(True, 'WEST_TRUE')
    WEST_FALSE = PROPERTY_WEST.value(False, 'WEST_FALSE')


class SpruceFenceGate(BlockDefinition):
    def __init__(self):
        self.id = 183
        self.name = 'spruce_fence_gate'
        self.short_usage_str = 'block.SPRUCE_FENCE_GATE'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_IN_WALL = BooleanProperty('in_wall'); ALL_PROPERTIES.append(PROPERTY_IN_WALL)
    IN_WALL_TRUE  = PROPERTY_IN_WALL.value(True, 'IN_WALL_TRUE')
    IN_WALL_FALSE = PROPERTY_IN_WALL.value(False, 'IN_WALL_FALSE')

    PROPERTY_OPEN = BooleanProperty('open'); ALL_PROPERTIES.append(PROPERTY_OPEN)
    OPEN_TRUE  = PROPERTY_OPEN.value(True, 'OPEN_TRUE')
    OPEN_FALSE = PROPERTY_OPEN.value(False, 'OPEN_FALSE')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class SpruceStairs(BlockDefinition):
    def __init__(self):
        self.id = 134
        self.name = 'spruce_stairs'
        self.short_usage_str = 'block.SPRUCE_STAIRS'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_SHAPE = EnumProperty('shape'); ALL_PROPERTIES.append(PROPERTY_SHAPE)
    SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight', 'SHAPE_STRAIGHT')
    SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left', 'SHAPE_INNER_LEFT')
    SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right', 'SHAPE_INNER_RIGHT')
    SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left', 'SHAPE_OUTER_LEFT')
    SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right', 'SHAPE_OUTER_RIGHT')


class StainedGlass(BlockDefinition):
    def __init__(self):
        self.id = 95
        self.name = 'stained_glass'
        self.short_usage_str = 'block.STAINED_GLASS'

    ALL_PROPERTIES = []

    PROPERTY_COLOR = EnumProperty('color'); ALL_PROPERTIES.append(PROPERTY_COLOR)
    COLOR_WHITE      = PROPERTY_COLOR.value('white', 'COLOR_WHITE')
    COLOR_ORANGE     = PROPERTY_COLOR.value('orange', 'COLOR_ORANGE')
    COLOR_MAGENTA    = PROPERTY_COLOR.value('magenta', 'COLOR_MAGENTA')
    COLOR_LIGHT_BLUE = PROPERTY_COLOR.value('light_blue', 'COLOR_LIGHT_BLUE')
    COLOR_YELLOW     = PROPERTY_COLOR.value('yellow', 'COLOR_YELLOW')
    COLOR_LIME       = PROPERTY_COLOR.value('lime', 'COLOR_LIME')
    COLOR_PINK       = PROPERTY_COLOR.value('pink', 'COLOR_PINK')
    COLOR_GRAY       = PROPERTY_COLOR.value('gray', 'COLOR_GRAY')
    COLOR_SILVER     = PROPERTY_COLOR.value('silver', 'COLOR_SILVER')
    COLOR_CYAN       = PROPERTY_COLOR.value('cyan', 'COLOR_CYAN')
    COLOR_PURPLE     = PROPERTY_COLOR.value('purple', 'COLOR_PURPLE')
    COLOR_BLUE       = PROPERTY_COLOR.value('blue', 'COLOR_BLUE')
    COLOR_BROWN      = PROPERTY_COLOR.value('brown', 'COLOR_BROWN')
    COLOR_GREEN      = PROPERTY_COLOR.value('green', 'COLOR_GREEN')
    COLOR_RED        = PROPERTY_COLOR.value('red', 'COLOR_RED')
    COLOR_BLACK      = PROPERTY_COLOR.value('black', 'COLOR_BLACK')


class StainedGlassPane(BlockDefinition):
    def __init__(self):
        self.id = 160
        self.name = 'stained_glass_pane'
        self.short_usage_str = 'block.STAINED_GLASS_PANE'

    ALL_PROPERTIES = []

    PROPERTY_COLOR = EnumProperty('color'); ALL_PROPERTIES.append(PROPERTY_COLOR)
    COLOR_WHITE      = PROPERTY_COLOR.value('white', 'COLOR_WHITE')
    COLOR_ORANGE     = PROPERTY_COLOR.value('orange', 'COLOR_ORANGE')
    COLOR_MAGENTA    = PROPERTY_COLOR.value('magenta', 'COLOR_MAGENTA')
    COLOR_LIGHT_BLUE = PROPERTY_COLOR.value('light_blue', 'COLOR_LIGHT_BLUE')
    COLOR_YELLOW     = PROPERTY_COLOR.value('yellow', 'COLOR_YELLOW')
    COLOR_LIME       = PROPERTY_COLOR.value('lime', 'COLOR_LIME')
    COLOR_PINK       = PROPERTY_COLOR.value('pink', 'COLOR_PINK')
    COLOR_GRAY       = PROPERTY_COLOR.value('gray', 'COLOR_GRAY')
    COLOR_SILVER     = PROPERTY_COLOR.value('silver', 'COLOR_SILVER')
    COLOR_CYAN       = PROPERTY_COLOR.value('cyan', 'COLOR_CYAN')
    COLOR_PURPLE     = PROPERTY_COLOR.value('purple', 'COLOR_PURPLE')
    COLOR_BLUE       = PROPERTY_COLOR.value('blue', 'COLOR_BLUE')
    COLOR_BROWN      = PROPERTY_COLOR.value('brown', 'COLOR_BROWN')
    COLOR_GREEN      = PROPERTY_COLOR.value('green', 'COLOR_GREEN')
    COLOR_RED        = PROPERTY_COLOR.value('red', 'COLOR_RED')
    COLOR_BLACK      = PROPERTY_COLOR.value('black', 'COLOR_BLACK')

    PROPERTY_EAST = BooleanProperty('east'); ALL_PROPERTIES.append(PROPERTY_EAST)
    EAST_TRUE  = PROPERTY_EAST.value(True, 'EAST_TRUE')
    EAST_FALSE = PROPERTY_EAST.value(False, 'EAST_FALSE')

    PROPERTY_NORTH = BooleanProperty('north'); ALL_PROPERTIES.append(PROPERTY_NORTH)
    NORTH_TRUE  = PROPERTY_NORTH.value(True, 'NORTH_TRUE')
    NORTH_FALSE = PROPERTY_NORTH.value(False, 'NORTH_FALSE')

    PROPERTY_SOUTH = BooleanProperty('south'); ALL_PROPERTIES.append(PROPERTY_SOUTH)
    SOUTH_TRUE  = PROPERTY_SOUTH.value(True, 'SOUTH_TRUE')
    SOUTH_FALSE = PROPERTY_SOUTH.value(False, 'SOUTH_FALSE')

    PROPERTY_WEST = BooleanProperty('west'); ALL_PROPERTIES.append(PROPERTY_WEST)
    WEST_TRUE  = PROPERTY_WEST.value(True, 'WEST_TRUE')
    WEST_FALSE = PROPERTY_WEST.value(False, 'WEST_FALSE')


class StainedHardenedClay(BlockDefinition):
    def __init__(self):
        self.id = 159
        self.name = 'stained_hardened_clay'
        self.short_usage_str = 'block.STAINED_HARDENED_CLAY'

    ALL_PROPERTIES = []

    PROPERTY_COLOR = EnumProperty('color'); ALL_PROPERTIES.append(PROPERTY_COLOR)
    COLOR_WHITE      = PROPERTY_COLOR.value('white', 'COLOR_WHITE')
    COLOR_ORANGE     = PROPERTY_COLOR.value('orange', 'COLOR_ORANGE')
    COLOR_MAGENTA    = PROPERTY_COLOR.value('magenta', 'COLOR_MAGENTA')
    COLOR_LIGHT_BLUE = PROPERTY_COLOR.value('light_blue', 'COLOR_LIGHT_BLUE')
    COLOR_YELLOW     = PROPERTY_COLOR.value('yellow', 'COLOR_YELLOW')
    COLOR_LIME       = PROPERTY_COLOR.value('lime', 'COLOR_LIME')
    COLOR_PINK       = PROPERTY_COLOR.value('pink', 'COLOR_PINK')
    COLOR_GRAY       = PROPERTY_COLOR.value('gray', 'COLOR_GRAY')
    COLOR_SILVER     = PROPERTY_COLOR.value('silver', 'COLOR_SILVER')
    COLOR_CYAN       = PROPERTY_COLOR.value('cyan', 'COLOR_CYAN')
    COLOR_PURPLE     = PROPERTY_COLOR.value('purple', 'COLOR_PURPLE')
    COLOR_BLUE       = PROPERTY_COLOR.value('blue', 'COLOR_BLUE')
    COLOR_BROWN      = PROPERTY_COLOR.value('brown', 'COLOR_BROWN')
    COLOR_GREEN      = PROPERTY_COLOR.value('green', 'COLOR_GREEN')
    COLOR_RED        = PROPERTY_COLOR.value('red', 'COLOR_RED')
    COLOR_BLACK      = PROPERTY_COLOR.value('black', 'COLOR_BLACK')


class StandingBanner(BlockDefinition):
    def __init__(self):
        self.id = 176
        self.name = 'standing_banner'
        self.short_usage_str = 'block.STANDING_BANNER'

    ALL_PROPERTIES = []

    PROPERTY_ROTATION = IntegerProperty('rotation'); ALL_PROPERTIES.append(PROPERTY_ROTATION)
    ROTATION_0  = PROPERTY_ROTATION.value(0, 'ROTATION_0')
    ROTATION_1  = PROPERTY_ROTATION.value(1, 'ROTATION_1')
    ROTATION_2  = PROPERTY_ROTATION.value(2, 'ROTATION_2')
    ROTATION_3  = PROPERTY_ROTATION.value(3, 'ROTATION_3')
    ROTATION_4  = PROPERTY_ROTATION.value(4, 'ROTATION_4')
    ROTATION_5  = PROPERTY_ROTATION.value(5, 'ROTATION_5')
    ROTATION_6  = PROPERTY_ROTATION.value(6, 'ROTATION_6')
    ROTATION_7  = PROPERTY_ROTATION.value(7, 'ROTATION_7')
    ROTATION_8  = PROPERTY_ROTATION.value(8, 'ROTATION_8')
    ROTATION_9  = PROPERTY_ROTATION.value(9, 'ROTATION_9')
    ROTATION_10 = PROPERTY_ROTATION.value(10, 'ROTATION_10')
    ROTATION_11 = PROPERTY_ROTATION.value(11, 'ROTATION_11')
    ROTATION_12 = PROPERTY_ROTATION.value(12, 'ROTATION_12')
    ROTATION_13 = PROPERTY_ROTATION.value(13, 'ROTATION_13')
    ROTATION_14 = PROPERTY_ROTATION.value(14, 'ROTATION_14')
    ROTATION_15 = PROPERTY_ROTATION.value(15, 'ROTATION_15')


class StandingSign(BlockDefinition):
    def __init__(self):
        self.id = 63
        self.name = 'standing_sign'
        self.short_usage_str = 'block.STANDING_SIGN'

    ALL_PROPERTIES = []

    PROPERTY_ROTATION = IntegerProperty('rotation'); ALL_PROPERTIES.append(PROPERTY_ROTATION)
    ROTATION_0  = PROPERTY_ROTATION.value(0, 'ROTATION_0')
    ROTATION_1  = PROPERTY_ROTATION.value(1, 'ROTATION_1')
    ROTATION_2  = PROPERTY_ROTATION.value(2, 'ROTATION_2')
    ROTATION_3  = PROPERTY_ROTATION.value(3, 'ROTATION_3')
    ROTATION_4  = PROPERTY_ROTATION.value(4, 'ROTATION_4')
    ROTATION_5  = PROPERTY_ROTATION.value(5, 'ROTATION_5')
    ROTATION_6  = PROPERTY_ROTATION.value(6, 'ROTATION_6')
    ROTATION_7  = PROPERTY_ROTATION.value(7, 'ROTATION_7')
    ROTATION_8  = PROPERTY_ROTATION.value(8, 'ROTATION_8')
    ROTATION_9  = PROPERTY_ROTATION.value(9, 'ROTATION_9')
    ROTATION_10 = PROPERTY_ROTATION.value(10, 'ROTATION_10')
    ROTATION_11 = PROPERTY_ROTATION.value(11, 'ROTATION_11')
    ROTATION_12 = PROPERTY_ROTATION.value(12, 'ROTATION_12')
    ROTATION_13 = PROPERTY_ROTATION.value(13, 'ROTATION_13')
    ROTATION_14 = PROPERTY_ROTATION.value(14, 'ROTATION_14')
    ROTATION_15 = PROPERTY_ROTATION.value(15, 'ROTATION_15')


class StickyPiston(BlockDefinition):
    def __init__(self):
        self.id = 29
        self.name = 'sticky_piston'
        self.short_usage_str = 'block.STICKY_PISTON'

    ALL_PROPERTIES = []

    PROPERTY_EXTENDED = BooleanProperty('extended'); ALL_PROPERTIES.append(PROPERTY_EXTENDED)
    EXTENDED_TRUE  = PROPERTY_EXTENDED.value(True, 'EXTENDED_TRUE')
    EXTENDED_FALSE = PROPERTY_EXTENDED.value(False, 'EXTENDED_FALSE')

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_DOWN  = PROPERTY_FACING.value('down', 'FACING_DOWN')
    FACING_UP    = PROPERTY_FACING.value('up', 'FACING_UP')
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class Stone(BlockDefinition):
    def __init__(self):
        self.id = 1
        self.name = 'stone'
        self.short_usage_str = 'block.STONE'

    ALL_PROPERTIES = []

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_STONE           = PROPERTY_VARIANT.value('stone', 'VARIANT_STONE')
    VARIANT_GRANITE         = PROPERTY_VARIANT.value('granite', 'VARIANT_GRANITE')
    VARIANT_SMOOTH_GRANITE  = PROPERTY_VARIANT.value('smooth_granite', 'VARIANT_SMOOTH_GRANITE')
    VARIANT_DIORITE         = PROPERTY_VARIANT.value('diorite', 'VARIANT_DIORITE')
    VARIANT_SMOOTH_DIORITE  = PROPERTY_VARIANT.value('smooth_diorite', 'VARIANT_SMOOTH_DIORITE')
    VARIANT_ANDESITE        = PROPERTY_VARIANT.value('andesite', 'VARIANT_ANDESITE')
    VARIANT_SMOOTH_ANDESITE = PROPERTY_VARIANT.value('smooth_andesite', 'VARIANT_SMOOTH_ANDESITE')


class StoneBrickStairs(BlockDefinition):
    def __init__(self):
        self.id = 109
        self.name = 'stone_brick_stairs'
        self.short_usage_str = 'block.STONE_BRICK_STAIRS'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_SHAPE = EnumProperty('shape'); ALL_PROPERTIES.append(PROPERTY_SHAPE)
    SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight', 'SHAPE_STRAIGHT')
    SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left', 'SHAPE_INNER_LEFT')
    SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right', 'SHAPE_INNER_RIGHT')
    SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left', 'SHAPE_OUTER_LEFT')
    SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right', 'SHAPE_OUTER_RIGHT')


class StoneButton(BlockDefinition):
    def __init__(self):
        self.id = 77
        self.name = 'stone_button'
        self.short_usage_str = 'block.STONE_BUTTON'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_DOWN  = PROPERTY_FACING.value('down', 'FACING_DOWN')
    FACING_UP    = PROPERTY_FACING.value('up', 'FACING_UP')
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class StonePressurePlate(BlockDefinition):
    def __init__(self):
        self.id = 70
        self.name = 'stone_pressure_plate'
        self.short_usage_str = 'block.STONE_PRESSURE_PLATE'

    ALL_PROPERTIES = []

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class StoneSlab(BlockDefinition):
    def __init__(self):
        self.id = 44
        self.name = 'stone_slab'
        self.short_usage_str = 'block.STONE_SLAB'

    ALL_PROPERTIES = []

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_STONE        = PROPERTY_VARIANT.value('stone', 'VARIANT_STONE')
    VARIANT_SANDSTONE    = PROPERTY_VARIANT.value('sandstone', 'VARIANT_SANDSTONE')
    VARIANT_WOOD_OLD     = PROPERTY_VARIANT.value('wood_old', 'VARIANT_WOOD_OLD')
    VARIANT_COBBLESTONE  = PROPERTY_VARIANT.value('cobblestone', 'VARIANT_COBBLESTONE')
    VARIANT_BRICK        = PROPERTY_VARIANT.value('brick', 'VARIANT_BRICK')
    VARIANT_STONE_BRICK  = PROPERTY_VARIANT.value('stone_brick', 'VARIANT_STONE_BRICK')
    VARIANT_NETHER_BRICK = PROPERTY_VARIANT.value('nether_brick', 'VARIANT_NETHER_BRICK')
    VARIANT_QUARTZ       = PROPERTY_VARIANT.value('quartz', 'VARIANT_QUARTZ')


class StoneSlab2(BlockDefinition):
    def __init__(self):
        self.id = 182
        self.name = 'stone_slab2'
        self.short_usage_str = 'block.STONE_SLAB2'

    ALL_PROPERTIES = []

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_RED_SANDSTONE = PROPERTY_VARIANT.value('red_sandstone', 'VARIANT_RED_SANDSTONE')


class StoneStairs(BlockDefinition):
    def __init__(self):
        self.id = 67
        self.name = 'stone_stairs'
        self.short_usage_str = 'block.STONE_STAIRS'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_SHAPE = EnumProperty('shape'); ALL_PROPERTIES.append(PROPERTY_SHAPE)
    SHAPE_STRAIGHT    = PROPERTY_SHAPE.value('straight', 'SHAPE_STRAIGHT')
    SHAPE_INNER_LEFT  = PROPERTY_SHAPE.value('inner_left', 'SHAPE_INNER_LEFT')
    SHAPE_INNER_RIGHT = PROPERTY_SHAPE.value('inner_right', 'SHAPE_INNER_RIGHT')
    SHAPE_OUTER_LEFT  = PROPERTY_SHAPE.value('outer_left', 'SHAPE_OUTER_LEFT')
    SHAPE_OUTER_RIGHT = PROPERTY_SHAPE.value('outer_right', 'SHAPE_OUTER_RIGHT')


class Stonebrick(BlockDefinition):
    def __init__(self):
        self.id = 98
        self.name = 'stonebrick'
        self.short_usage_str = 'block.STONEBRICK'

    ALL_PROPERTIES = []

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_STONEBRICK          = PROPERTY_VARIANT.value('stonebrick', 'VARIANT_STONEBRICK')
    VARIANT_MOSSY_STONEBRICK    = PROPERTY_VARIANT.value('mossy_stonebrick', 'VARIANT_MOSSY_STONEBRICK')
    VARIANT_CRACKED_STONEBRICK  = PROPERTY_VARIANT.value('cracked_stonebrick', 'VARIANT_CRACKED_STONEBRICK')
    VARIANT_CHISELED_STONEBRICK = PROPERTY_VARIANT.value('chiseled_stonebrick', 'VARIANT_CHISELED_STONEBRICK')


class Tallgrass(BlockDefinition):
    def __init__(self):
        self.id = 31
        self.name = 'tallgrass'
        self.short_usage_str = 'block.TALLGRASS'

    ALL_PROPERTIES = []

    PROPERTY_TYPE = EnumProperty('type'); ALL_PROPERTIES.append(PROPERTY_TYPE)
    TYPE_DEAD_BUSH  = PROPERTY_TYPE.value('dead_bush', 'TYPE_DEAD_BUSH')
    TYPE_TALL_GRASS = PROPERTY_TYPE.value('tall_grass', 'TYPE_TALL_GRASS')
    TYPE_FERN       = PROPERTY_TYPE.value('fern', 'TYPE_FERN')


class Tnt(BlockDefinition):
    def __init__(self):
        self.id = 46
        self.name = 'tnt'
        self.short_usage_str = 'block.TNT'

    ALL_PROPERTIES = []

    PROPERTY_EXPLODE = BooleanProperty('explode'); ALL_PROPERTIES.append(PROPERTY_EXPLODE)
    EXPLODE_TRUE  = PROPERTY_EXPLODE.value(True, 'EXPLODE_TRUE')
    EXPLODE_FALSE = PROPERTY_EXPLODE.value(False, 'EXPLODE_FALSE')


class Torch(BlockDefinition):
    def __init__(self):
        self.id = 50
        self.name = 'torch'
        self.short_usage_str = 'block.TORCH'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_UP    = PROPERTY_FACING.value('up', 'FACING_UP')
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class Trapdoor(BlockDefinition):
    def __init__(self):
        self.id = 96
        self.name = 'trapdoor'
        self.short_usage_str = 'block.TRAPDOOR'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_OPEN = BooleanProperty('open'); ALL_PROPERTIES.append(PROPERTY_OPEN)
    OPEN_TRUE  = PROPERTY_OPEN.value(True, 'OPEN_TRUE')
    OPEN_FALSE = PROPERTY_OPEN.value(False, 'OPEN_FALSE')


class TrappedChest(BlockDefinition):
    def __init__(self):
        self.id = 146
        self.name = 'trapped_chest'
        self.short_usage_str = 'block.TRAPPED_CHEST'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class Tripwire(BlockDefinition):
    def __init__(self):
        self.id = 132
        self.name = 'tripwire'
        self.short_usage_str = 'block.TRIPWIRE'

    ALL_PROPERTIES = []

    PROPERTY_ATTACHED = BooleanProperty('attached'); ALL_PROPERTIES.append(PROPERTY_ATTACHED)
    ATTACHED_TRUE  = PROPERTY_ATTACHED.value(True, 'ATTACHED_TRUE')
    ATTACHED_FALSE = PROPERTY_ATTACHED.value(False, 'ATTACHED_FALSE')

    PROPERTY_DISARMED = BooleanProperty('disarmed'); ALL_PROPERTIES.append(PROPERTY_DISARMED)
    DISARMED_TRUE  = PROPERTY_DISARMED.value(True, 'DISARMED_TRUE')
    DISARMED_FALSE = PROPERTY_DISARMED.value(False, 'DISARMED_FALSE')

    PROPERTY_EAST = BooleanProperty('east'); ALL_PROPERTIES.append(PROPERTY_EAST)
    EAST_TRUE  = PROPERTY_EAST.value(True, 'EAST_TRUE')
    EAST_FALSE = PROPERTY_EAST.value(False, 'EAST_FALSE')

    PROPERTY_NORTH = BooleanProperty('north'); ALL_PROPERTIES.append(PROPERTY_NORTH)
    NORTH_TRUE  = PROPERTY_NORTH.value(True, 'NORTH_TRUE')
    NORTH_FALSE = PROPERTY_NORTH.value(False, 'NORTH_FALSE')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')

    PROPERTY_SOUTH = BooleanProperty('south'); ALL_PROPERTIES.append(PROPERTY_SOUTH)
    SOUTH_TRUE  = PROPERTY_SOUTH.value(True, 'SOUTH_TRUE')
    SOUTH_FALSE = PROPERTY_SOUTH.value(False, 'SOUTH_FALSE')

    PROPERTY_SUSPENDED = BooleanProperty('suspended'); ALL_PROPERTIES.append(PROPERTY_SUSPENDED)
    SUSPENDED_TRUE  = PROPERTY_SUSPENDED.value(True, 'SUSPENDED_TRUE')
    SUSPENDED_FALSE = PROPERTY_SUSPENDED.value(False, 'SUSPENDED_FALSE')

    PROPERTY_WEST = BooleanProperty('west'); ALL_PROPERTIES.append(PROPERTY_WEST)
    WEST_TRUE  = PROPERTY_WEST.value(True, 'WEST_TRUE')
    WEST_FALSE = PROPERTY_WEST.value(False, 'WEST_FALSE')


class TripwireHook(BlockDefinition):
    def __init__(self):
        self.id = 131
        self.name = 'tripwire_hook'
        self.short_usage_str = 'block.TRIPWIRE_HOOK'

    ALL_PROPERTIES = []

    PROPERTY_ATTACHED = BooleanProperty('attached'); ALL_PROPERTIES.append(PROPERTY_ATTACHED)
    ATTACHED_TRUE  = PROPERTY_ATTACHED.value(True, 'ATTACHED_TRUE')
    ATTACHED_FALSE = PROPERTY_ATTACHED.value(False, 'ATTACHED_FALSE')

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')

    PROPERTY_SUSPENDED = BooleanProperty('suspended'); ALL_PROPERTIES.append(PROPERTY_SUSPENDED)
    SUSPENDED_TRUE  = PROPERTY_SUSPENDED.value(True, 'SUSPENDED_TRUE')
    SUSPENDED_FALSE = PROPERTY_SUSPENDED.value(False, 'SUSPENDED_FALSE')


class UnlitRedstoneTorch(BlockDefinition):
    def __init__(self):
        self.id = 75
        self.name = 'unlit_redstone_torch'
        self.short_usage_str = 'block.UNLIT_REDSTONE_TORCH'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_UP    = PROPERTY_FACING.value('up', 'FACING_UP')
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class UnpoweredComparator(BlockDefinition):
    def __init__(self):
        self.id = 149
        self.name = 'unpowered_comparator'
        self.short_usage_str = 'block.UNPOWERED_COMPARATOR'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_MODE = EnumProperty('mode'); ALL_PROPERTIES.append(PROPERTY_MODE)
    MODE_COMPARE  = PROPERTY_MODE.value('compare', 'MODE_COMPARE')
    MODE_SUBTRACT = PROPERTY_MODE.value('subtract', 'MODE_SUBTRACT')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class UnpoweredRepeater(BlockDefinition):
    def __init__(self):
        self.id = 93
        self.name = 'unpowered_repeater'
        self.short_usage_str = 'block.UNPOWERED_REPEATER'

    ALL_PROPERTIES = []

    PROPERTY_DELAY = IntegerProperty('delay'); ALL_PROPERTIES.append(PROPERTY_DELAY)
    DELAY_1 = PROPERTY_DELAY.value(1, 'DELAY_1')
    DELAY_2 = PROPERTY_DELAY.value(2, 'DELAY_2')
    DELAY_3 = PROPERTY_DELAY.value(3, 'DELAY_3')
    DELAY_4 = PROPERTY_DELAY.value(4, 'DELAY_4')

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_LOCKED = BooleanProperty('locked'); ALL_PROPERTIES.append(PROPERTY_LOCKED)
    LOCKED_TRUE  = PROPERTY_LOCKED.value(True, 'LOCKED_TRUE')
    LOCKED_FALSE = PROPERTY_LOCKED.value(False, 'LOCKED_FALSE')


class Vine(BlockDefinition):
    def __init__(self):
        self.id = 106
        self.name = 'vine'
        self.short_usage_str = 'block.VINE'

    ALL_PROPERTIES = []

    PROPERTY_EAST = BooleanProperty('east'); ALL_PROPERTIES.append(PROPERTY_EAST)
    EAST_TRUE  = PROPERTY_EAST.value(True, 'EAST_TRUE')
    EAST_FALSE = PROPERTY_EAST.value(False, 'EAST_FALSE')

    PROPERTY_NORTH = BooleanProperty('north'); ALL_PROPERTIES.append(PROPERTY_NORTH)
    NORTH_TRUE  = PROPERTY_NORTH.value(True, 'NORTH_TRUE')
    NORTH_FALSE = PROPERTY_NORTH.value(False, 'NORTH_FALSE')

    PROPERTY_SOUTH = BooleanProperty('south'); ALL_PROPERTIES.append(PROPERTY_SOUTH)
    SOUTH_TRUE  = PROPERTY_SOUTH.value(True, 'SOUTH_TRUE')
    SOUTH_FALSE = PROPERTY_SOUTH.value(False, 'SOUTH_FALSE')

    PROPERTY_UP = BooleanProperty('up'); ALL_PROPERTIES.append(PROPERTY_UP)
    UP_TRUE  = PROPERTY_UP.value(True, 'UP_TRUE')
    UP_FALSE = PROPERTY_UP.value(False, 'UP_FALSE')

    PROPERTY_WEST = BooleanProperty('west'); ALL_PROPERTIES.append(PROPERTY_WEST)
    WEST_TRUE  = PROPERTY_WEST.value(True, 'WEST_TRUE')
    WEST_FALSE = PROPERTY_WEST.value(False, 'WEST_FALSE')


class WallBanner(BlockDefinition):
    def __init__(self):
        self.id = 177
        self.name = 'wall_banner'
        self.short_usage_str = 'block.WALL_BANNER'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class WallSign(BlockDefinition):
    def __init__(self):
        self.id = 68
        self.name = 'wall_sign'
        self.short_usage_str = 'block.WALL_SIGN'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')


class Water(BlockDefinition):
    def __init__(self):
        self.id = 9
        self.name = 'water'
        self.short_usage_str = 'block.WATER'

    ALL_PROPERTIES = []

    PROPERTY_LEVEL = IntegerProperty('level'); ALL_PROPERTIES.append(PROPERTY_LEVEL)
    LEVEL_0  = PROPERTY_LEVEL.value(0, 'LEVEL_0')
    LEVEL_1  = PROPERTY_LEVEL.value(1, 'LEVEL_1')
    LEVEL_2  = PROPERTY_LEVEL.value(2, 'LEVEL_2')
    LEVEL_3  = PROPERTY_LEVEL.value(3, 'LEVEL_3')
    LEVEL_4  = PROPERTY_LEVEL.value(4, 'LEVEL_4')
    LEVEL_5  = PROPERTY_LEVEL.value(5, 'LEVEL_5')
    LEVEL_6  = PROPERTY_LEVEL.value(6, 'LEVEL_6')
    LEVEL_7  = PROPERTY_LEVEL.value(7, 'LEVEL_7')
    LEVEL_8  = PROPERTY_LEVEL.value(8, 'LEVEL_8')
    LEVEL_9  = PROPERTY_LEVEL.value(9, 'LEVEL_9')
    LEVEL_10 = PROPERTY_LEVEL.value(10, 'LEVEL_10')
    LEVEL_11 = PROPERTY_LEVEL.value(11, 'LEVEL_11')
    LEVEL_12 = PROPERTY_LEVEL.value(12, 'LEVEL_12')
    LEVEL_13 = PROPERTY_LEVEL.value(13, 'LEVEL_13')
    LEVEL_14 = PROPERTY_LEVEL.value(14, 'LEVEL_14')
    LEVEL_15 = PROPERTY_LEVEL.value(15, 'LEVEL_15')


class Waterlily(BlockDefinition):
    def __init__(self):
        self.id = 111
        self.name = 'waterlily'
        self.short_usage_str = 'block.WATERLILY'

    ALL_PROPERTIES = []


class Web(BlockDefinition):
    def __init__(self):
        self.id = 30
        self.name = 'web'
        self.short_usage_str = 'block.WEB'

    ALL_PROPERTIES = []


class Wheat(BlockDefinition):
    def __init__(self):
        self.id = 59
        self.name = 'wheat'
        self.short_usage_str = 'block.WHEAT'

    ALL_PROPERTIES = []

    PROPERTY_AGE = IntegerProperty('age'); ALL_PROPERTIES.append(PROPERTY_AGE)
    AGE_0 = PROPERTY_AGE.value(0, 'AGE_0')
    AGE_1 = PROPERTY_AGE.value(1, 'AGE_1')
    AGE_2 = PROPERTY_AGE.value(2, 'AGE_2')
    AGE_3 = PROPERTY_AGE.value(3, 'AGE_3')
    AGE_4 = PROPERTY_AGE.value(4, 'AGE_4')
    AGE_5 = PROPERTY_AGE.value(5, 'AGE_5')
    AGE_6 = PROPERTY_AGE.value(6, 'AGE_6')
    AGE_7 = PROPERTY_AGE.value(7, 'AGE_7')


class WoodenButton(BlockDefinition):
    def __init__(self):
        self.id = 143
        self.name = 'wooden_button'
        self.short_usage_str = 'block.WOODEN_BUTTON'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_DOWN  = PROPERTY_FACING.value('down', 'FACING_DOWN')
    FACING_UP    = PROPERTY_FACING.value('up', 'FACING_UP')
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class WoodenDoor(BlockDefinition):
    def __init__(self):
        self.id = 64
        self.name = 'wooden_door'
        self.short_usage_str = 'block.WOODEN_DOOR'

    ALL_PROPERTIES = []

    PROPERTY_FACING = EnumProperty('facing'); ALL_PROPERTIES.append(PROPERTY_FACING)
    FACING_NORTH = PROPERTY_FACING.value('north', 'FACING_NORTH')
    FACING_SOUTH = PROPERTY_FACING.value('south', 'FACING_SOUTH')
    FACING_WEST  = PROPERTY_FACING.value('west', 'FACING_WEST')
    FACING_EAST  = PROPERTY_FACING.value('east', 'FACING_EAST')

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_UPPER = PROPERTY_HALF.value('upper', 'HALF_UPPER')
    HALF_LOWER = PROPERTY_HALF.value('lower', 'HALF_LOWER')

    PROPERTY_HINGE = EnumProperty('hinge'); ALL_PROPERTIES.append(PROPERTY_HINGE)
    HINGE_LEFT  = PROPERTY_HINGE.value('left', 'HINGE_LEFT')
    HINGE_RIGHT = PROPERTY_HINGE.value('right', 'HINGE_RIGHT')

    PROPERTY_OPEN = BooleanProperty('open'); ALL_PROPERTIES.append(PROPERTY_OPEN)
    OPEN_TRUE  = PROPERTY_OPEN.value(True, 'OPEN_TRUE')
    OPEN_FALSE = PROPERTY_OPEN.value(False, 'OPEN_FALSE')

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class WoodenPressurePlate(BlockDefinition):
    def __init__(self):
        self.id = 72
        self.name = 'wooden_pressure_plate'
        self.short_usage_str = 'block.WOODEN_PRESSURE_PLATE'

    ALL_PROPERTIES = []

    PROPERTY_POWERED = BooleanProperty('powered'); ALL_PROPERTIES.append(PROPERTY_POWERED)
    POWERED_TRUE  = PROPERTY_POWERED.value(True, 'POWERED_TRUE')
    POWERED_FALSE = PROPERTY_POWERED.value(False, 'POWERED_FALSE')


class WoodenSlab(BlockDefinition):
    def __init__(self):
        self.id = 126
        self.name = 'wooden_slab'
        self.short_usage_str = 'block.WOODEN_SLAB'

    ALL_PROPERTIES = []

    PROPERTY_HALF = EnumProperty('half'); ALL_PROPERTIES.append(PROPERTY_HALF)
    HALF_TOP    = PROPERTY_HALF.value('top', 'HALF_TOP')
    HALF_BOTTOM = PROPERTY_HALF.value('bottom', 'HALF_BOTTOM')

    PROPERTY_VARIANT = EnumProperty('variant'); ALL_PROPERTIES.append(PROPERTY_VARIANT)
    VARIANT_OAK      = PROPERTY_VARIANT.value('oak', 'VARIANT_OAK')
    VARIANT_SPRUCE   = PROPERTY_VARIANT.value('spruce', 'VARIANT_SPRUCE')
    VARIANT_BIRCH    = PROPERTY_VARIANT.value('birch', 'VARIANT_BIRCH')
    VARIANT_JUNGLE   = PROPERTY_VARIANT.value('jungle', 'VARIANT_JUNGLE')
    VARIANT_ACACIA   = PROPERTY_VARIANT.value('acacia', 'VARIANT_ACACIA')
    VARIANT_DARK_OAK = PROPERTY_VARIANT.value('dark_oak', 'VARIANT_DARK_OAK')


class Wool(BlockDefinition):
    def __init__(self):
        self.id = 35
        self.name = 'wool'
        self.short_usage_str = 'block.WOOL'

    ALL_PROPERTIES = []

    PROPERTY_COLOR = EnumProperty('color'); ALL_PROPERTIES.append(PROPERTY_COLOR)
    COLOR_WHITE      = PROPERTY_COLOR.value('white', 'COLOR_WHITE')
    COLOR_ORANGE     = PROPERTY_COLOR.value('orange', 'COLOR_ORANGE')
    COLOR_MAGENTA    = PROPERTY_COLOR.value('magenta', 'COLOR_MAGENTA')
    COLOR_LIGHT_BLUE = PROPERTY_COLOR.value('light_blue', 'COLOR_LIGHT_BLUE')
    COLOR_YELLOW     = PROPERTY_COLOR.value('yellow', 'COLOR_YELLOW')
    COLOR_LIME       = PROPERTY_COLOR.value('lime', 'COLOR_LIME')
    COLOR_PINK       = PROPERTY_COLOR.value('pink', 'COLOR_PINK')
    COLOR_GRAY       = PROPERTY_COLOR.value('gray', 'COLOR_GRAY')
    COLOR_SILVER     = PROPERTY_COLOR.value('silver', 'COLOR_SILVER')
    COLOR_CYAN       = PROPERTY_COLOR.value('cyan', 'COLOR_CYAN')
    COLOR_PURPLE     = PROPERTY_COLOR.value('purple', 'COLOR_PURPLE')
    COLOR_BLUE       = PROPERTY_COLOR.value('blue', 'COLOR_BLUE')
    COLOR_BROWN      = PROPERTY_COLOR.value('brown', 'COLOR_BROWN')
    COLOR_GREEN      = PROPERTY_COLOR.value('green', 'COLOR_GREEN')
    COLOR_RED        = PROPERTY_COLOR.value('red', 'COLOR_RED')
    COLOR_BLACK      = PROPERTY_COLOR.value('black', 'COLOR_BLACK')


class YellowFlower(BlockDefinition):
    def __init__(self):
        self.id = 37
        self.name = 'yellow_flower'
        self.short_usage_str = 'block.YELLOW_FLOWER'

    ALL_PROPERTIES = []

    PROPERTY_TYPE = EnumProperty('type'); ALL_PROPERTIES.append(PROPERTY_TYPE)
    TYPE_DANDELION = PROPERTY_TYPE.value('dandelion', 'TYPE_DANDELION')

