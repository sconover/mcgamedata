class LivingDefinition():
    def __str__(self):
        return self.short_usage_str

class EntityTask():
    def __init__(self, entity_name, task_name):
        self.entity_name = entity_name
        self.task_name = task_name


class Any(LivingDefinition):
    def __init__(self):
        self.name = 'any'
        self.short_usage_str = 'living.ANY'

    ATTACK_ON_COLLIDE             = EntityTask('any' ,'attack_on_collide')
    ATTACK_WITH_ARROW             = EntityTask('any' ,'attack_with_arrow')
    AVOID                         = EntityTask('any' ,'avoid')
    AVOID_DOORS                   = EntityTask('any' ,'avoid_doors')
    AVOID_SUN                     = EntityTask('any' ,'avoid_sun')
    BEG                           = EntityTask('any' ,'beg')
    BLAZE_FIREBALL_ATTACK         = EntityTask('any' ,'blaze_fireball_attack')
    EAT_GRASS                     = EntityTask('any' ,'eat_grass')
    ENDERMAN_PLACE_BLOCK          = EntityTask('any' ,'enderman_place_block')
    ENDERMAN_TAKE_BLOCK           = EntityTask('any' ,'enderman_take_block')
    FLEE_SUN                      = EntityTask('any' ,'flee_sun')
    FOLLOW_GOLEM                  = EntityTask('any' ,'follow_golem')
    FOLLOW_OWNER                  = EntityTask('any' ,'follow_owner')
    FOLLOW_PARENT                 = EntityTask('any' ,'follow_parent')
    GHAST_FIREBALL_ATTACK         = EntityTask('any' ,'ghast_fireball_attack')
    GHAST_FLY                     = EntityTask('any' ,'ghast_fly')
    GHAST_LOOK_AROUND             = EntityTask('any' ,'ghast_look_around')
    GUARDIAN_ATTACK               = EntityTask('any' ,'guardian_attack')
    INTERACT_WITH_OTHER_VILLAGERS = EntityTask('any' ,'interact_with_other_villagers')
    LEAP_AT_TARGET                = EntityTask('any' ,'leap_at_target')
    LOOK_AT_TRADE_PLAYER          = EntityTask('any' ,'look_at_trade_player')
    LOOK_AT_VILLAGER              = EntityTask('any' ,'look_at_villager')
    LOOK_IDLE                     = EntityTask('any' ,'look_idle')
    MATE                          = EntityTask('any' ,'mate')
    MATE_WITH_OTHER_VILLAGER      = EntityTask('any' ,'mate_with_other_villager')
    MOVE_INDOOR                   = EntityTask('any' ,'move_indoor')
    MOVE_THROUGH_VILLAGE          = EntityTask('any' ,'move_through_village')
    MOVE_TOWARDS_RESTRICTION      = EntityTask('any' ,'move_towards_restriction')
    MOVE_TOWARDS_TARGET           = EntityTask('any' ,'move_towards_target')
    OCELOT_ATTACK                 = EntityTask('any' ,'ocelot_attack')
    OCELOT_SIT                    = EntityTask('any' ,'ocelot_sit')
    OPEN_DOOR                     = EntityTask('any' ,'open_door')
    PANIC                         = EntityTask('any' ,'panic')
    PLAYER_CONTROL                = EntityTask('any' ,'player_control')
    RABBIT_AVOID_WOLVES           = EntityTask('any' ,'rabbit_avoid_wolves')
    RABBIT_PANIC                  = EntityTask('any' ,'rabbit_panic')
    RABBIT_RAID_FARM              = EntityTask('any' ,'rabbit_raid_farm')
    RUN_AROUND_LIKE_CRAZY         = EntityTask('any' ,'run_around_like_crazy')
    SILVERFISH_HIDE_IN_STONE      = EntityTask('any' ,'silverfish_hide_in_stone')
    SIT                           = EntityTask('any' ,'sit')
    SLIME_ATTACK                  = EntityTask('any' ,'slime_attack')
    SLIME_FACE_RANDOM             = EntityTask('any' ,'slime_face_random')
    SLIME_FLOAT                   = EntityTask('any' ,'slime_float')
    SLIME_HOP                     = EntityTask('any' ,'slime_hop')
    SPIDER_ATTACK                 = EntityTask('any' ,'spider_attack')
    SQUID_MOVE_RANDOM             = EntityTask('any' ,'squid_move_random')
    SUMMON_SILVERFISH             = EntityTask('any' ,'summon_silverfish')
    SWELL_CREEPER                 = EntityTask('any' ,'swell_creeper')
    SWIM                          = EntityTask('any' ,'swim')
    TEMPT                         = EntityTask('any' ,'tempt')
    TRADE_WITH_PLAYER             = EntityTask('any' ,'trade_with_player')
    WANDER                        = EntityTask('any' ,'wander')
    WATCH_CLOSEST                 = EntityTask('any' ,'watch_closest')
    WATCH_CLOSEST_2               = EntityTask('any' ,'watch_closest_2')


class Bat(LivingDefinition):
    def __init__(self):
        self.name = 'bat'
        self.short_usage_str = 'living.BAT'



class Blaze(LivingDefinition):
    def __init__(self):
        self.name = 'blaze'
        self.short_usage_str = 'living.BLAZE'

    BLAZE_FIREBALL_ATTACK    = EntityTask('blaze' ,'blaze_fireball_attack')
    MOVE_TOWARDS_RESTRICTION = EntityTask('blaze' ,'move_towards_restriction')
    WANDER                   = EntityTask('blaze' ,'wander')
    WATCH_CLOSEST            = EntityTask('blaze' ,'watch_closest')
    LOOK_IDLE                = EntityTask('blaze' ,'look_idle')


class CaveSpider(LivingDefinition):
    def __init__(self):
        self.name = 'cave_spider'
        self.short_usage_str = 'living.CAVE_SPIDER'

    SWIM           = EntityTask('cave_spider' ,'swim')
    AVOID          = EntityTask('cave_spider' ,'avoid')
    LEAP_AT_TARGET = EntityTask('cave_spider' ,'leap_at_target')
    SPIDER_ATTACK  = EntityTask('cave_spider' ,'spider_attack')
    SPIDER_ATTACK  = EntityTask('cave_spider' ,'spider_attack')
    WANDER         = EntityTask('cave_spider' ,'wander')
    WATCH_CLOSEST  = EntityTask('cave_spider' ,'watch_closest')
    LOOK_IDLE      = EntityTask('cave_spider' ,'look_idle')


class Chicken(LivingDefinition):
    def __init__(self):
        self.name = 'chicken'
        self.short_usage_str = 'living.CHICKEN'

    SWIM          = EntityTask('chicken' ,'swim')
    PANIC         = EntityTask('chicken' ,'panic')
    MATE          = EntityTask('chicken' ,'mate')
    TEMPT         = EntityTask('chicken' ,'tempt')
    FOLLOW_PARENT = EntityTask('chicken' ,'follow_parent')
    WANDER        = EntityTask('chicken' ,'wander')
    WATCH_CLOSEST = EntityTask('chicken' ,'watch_closest')
    LOOK_IDLE     = EntityTask('chicken' ,'look_idle')


class Cow(LivingDefinition):
    def __init__(self):
        self.name = 'cow'
        self.short_usage_str = 'living.COW'

    SWIM          = EntityTask('cow' ,'swim')
    PANIC         = EntityTask('cow' ,'panic')
    MATE          = EntityTask('cow' ,'mate')
    TEMPT         = EntityTask('cow' ,'tempt')
    FOLLOW_PARENT = EntityTask('cow' ,'follow_parent')
    WANDER        = EntityTask('cow' ,'wander')
    WATCH_CLOSEST = EntityTask('cow' ,'watch_closest')
    LOOK_IDLE     = EntityTask('cow' ,'look_idle')


class Creeper(LivingDefinition):
    def __init__(self):
        self.name = 'creeper'
        self.short_usage_str = 'living.CREEPER'

    SWIM              = EntityTask('creeper' ,'swim')
    SWELL_CREEPER     = EntityTask('creeper' ,'swell_creeper')
    AVOID             = EntityTask('creeper' ,'avoid')
    AVOID             = EntityTask('creeper' ,'avoid')
    ATTACK_ON_COLLIDE = EntityTask('creeper' ,'attack_on_collide')
    WANDER            = EntityTask('creeper' ,'wander')
    WATCH_CLOSEST     = EntityTask('creeper' ,'watch_closest')
    LOOK_IDLE         = EntityTask('creeper' ,'look_idle')


class EnderDragon(LivingDefinition):
    def __init__(self):
        self.name = 'ender_dragon'
        self.short_usage_str = 'living.ENDER_DRAGON'



class Enderman(LivingDefinition):
    def __init__(self):
        self.name = 'enderman'
        self.short_usage_str = 'living.ENDERMAN'

    SWIM                 = EntityTask('enderman' ,'swim')
    ATTACK_ON_COLLIDE    = EntityTask('enderman' ,'attack_on_collide')
    WANDER               = EntityTask('enderman' ,'wander')
    WATCH_CLOSEST        = EntityTask('enderman' ,'watch_closest')
    LOOK_IDLE            = EntityTask('enderman' ,'look_idle')
    ENDERMAN_PLACE_BLOCK = EntityTask('enderman' ,'enderman_place_block')
    ENDERMAN_TAKE_BLOCK  = EntityTask('enderman' ,'enderman_take_block')


class Endermite(LivingDefinition):
    def __init__(self):
        self.name = 'endermite'
        self.short_usage_str = 'living.ENDERMITE'

    SWIM              = EntityTask('endermite' ,'swim')
    ATTACK_ON_COLLIDE = EntityTask('endermite' ,'attack_on_collide')
    WANDER            = EntityTask('endermite' ,'wander')
    WATCH_CLOSEST     = EntityTask('endermite' ,'watch_closest')
    LOOK_IDLE         = EntityTask('endermite' ,'look_idle')


class Ghast(LivingDefinition):
    def __init__(self):
        self.name = 'ghast'
        self.short_usage_str = 'living.GHAST'

    GHAST_FLY             = EntityTask('ghast' ,'ghast_fly')
    GHAST_LOOK_AROUND     = EntityTask('ghast' ,'ghast_look_around')
    GHAST_FIREBALL_ATTACK = EntityTask('ghast' ,'ghast_fireball_attack')


class Giant(LivingDefinition):
    def __init__(self):
        self.name = 'giant'
        self.short_usage_str = 'living.GIANT'



class Guardian(LivingDefinition):
    def __init__(self):
        self.name = 'guardian'
        self.short_usage_str = 'living.GUARDIAN'

    GUARDIAN_ATTACK          = EntityTask('guardian' ,'guardian_attack')
    MOVE_TOWARDS_RESTRICTION = EntityTask('guardian' ,'move_towards_restriction')
    WANDER                   = EntityTask('guardian' ,'wander')
    WATCH_CLOSEST            = EntityTask('guardian' ,'watch_closest')
    WATCH_CLOSEST            = EntityTask('guardian' ,'watch_closest')
    LOOK_IDLE                = EntityTask('guardian' ,'look_idle')


class Horse(LivingDefinition):
    def __init__(self):
        self.name = 'horse'
        self.short_usage_str = 'living.HORSE'

    SWIM                  = EntityTask('horse' ,'swim')
    PANIC                 = EntityTask('horse' ,'panic')
    RUN_AROUND_LIKE_CRAZY = EntityTask('horse' ,'run_around_like_crazy')
    MATE                  = EntityTask('horse' ,'mate')
    FOLLOW_PARENT         = EntityTask('horse' ,'follow_parent')
    WANDER                = EntityTask('horse' ,'wander')
    WATCH_CLOSEST         = EntityTask('horse' ,'watch_closest')
    LOOK_IDLE             = EntityTask('horse' ,'look_idle')


class Human(LivingDefinition):
    def __init__(self):
        self.name = 'human'
        self.short_usage_str = 'living.HUMAN'



class IronGolem(LivingDefinition):
    def __init__(self):
        self.name = 'iron_golem'
        self.short_usage_str = 'living.IRON_GOLEM'

    ATTACK_ON_COLLIDE        = EntityTask('iron_golem' ,'attack_on_collide')
    MOVE_TOWARDS_TARGET      = EntityTask('iron_golem' ,'move_towards_target')
    MOVE_THROUGH_VILLAGE     = EntityTask('iron_golem' ,'move_through_village')
    MOVE_TOWARDS_RESTRICTION = EntityTask('iron_golem' ,'move_towards_restriction')
    LOOK_AT_VILLAGER         = EntityTask('iron_golem' ,'look_at_villager')
    WANDER                   = EntityTask('iron_golem' ,'wander')
    WATCH_CLOSEST            = EntityTask('iron_golem' ,'watch_closest')
    LOOK_IDLE                = EntityTask('iron_golem' ,'look_idle')


class MagmaCube(LivingDefinition):
    def __init__(self):
        self.name = 'magma_cube'
        self.short_usage_str = 'living.MAGMA_CUBE'

    SLIME_FLOAT       = EntityTask('magma_cube' ,'slime_float')
    SLIME_ATTACK      = EntityTask('magma_cube' ,'slime_attack')
    SLIME_FACE_RANDOM = EntityTask('magma_cube' ,'slime_face_random')
    SLIME_HOP         = EntityTask('magma_cube' ,'slime_hop')


class MushroomCow(LivingDefinition):
    def __init__(self):
        self.name = 'mushroom_cow'
        self.short_usage_str = 'living.MUSHROOM_COW'

    SWIM          = EntityTask('mushroom_cow' ,'swim')
    PANIC         = EntityTask('mushroom_cow' ,'panic')
    MATE          = EntityTask('mushroom_cow' ,'mate')
    TEMPT         = EntityTask('mushroom_cow' ,'tempt')
    FOLLOW_PARENT = EntityTask('mushroom_cow' ,'follow_parent')
    WANDER        = EntityTask('mushroom_cow' ,'wander')
    WATCH_CLOSEST = EntityTask('mushroom_cow' ,'watch_closest')
    LOOK_IDLE     = EntityTask('mushroom_cow' ,'look_idle')


class Ocelot(LivingDefinition):
    def __init__(self):
        self.name = 'ocelot'
        self.short_usage_str = 'living.OCELOT'

    AVOID          = EntityTask('ocelot' ,'avoid')
    SWIM           = EntityTask('ocelot' ,'swim')
    SIT            = EntityTask('ocelot' ,'sit')
    TEMPT          = EntityTask('ocelot' ,'tempt')
    FOLLOW_OWNER   = EntityTask('ocelot' ,'follow_owner')
    OCELOT_SIT     = EntityTask('ocelot' ,'ocelot_sit')
    LEAP_AT_TARGET = EntityTask('ocelot' ,'leap_at_target')
    OCELOT_ATTACK  = EntityTask('ocelot' ,'ocelot_attack')
    MATE           = EntityTask('ocelot' ,'mate')
    WANDER         = EntityTask('ocelot' ,'wander')
    WATCH_CLOSEST  = EntityTask('ocelot' ,'watch_closest')


class Pig(LivingDefinition):
    def __init__(self):
        self.name = 'pig'
        self.short_usage_str = 'living.PIG'

    SWIM           = EntityTask('pig' ,'swim')
    PANIC          = EntityTask('pig' ,'panic')
    PLAYER_CONTROL = EntityTask('pig' ,'player_control')
    MATE           = EntityTask('pig' ,'mate')
    TEMPT          = EntityTask('pig' ,'tempt')
    TEMPT          = EntityTask('pig' ,'tempt')
    FOLLOW_PARENT  = EntityTask('pig' ,'follow_parent')
    WANDER         = EntityTask('pig' ,'wander')
    WATCH_CLOSEST  = EntityTask('pig' ,'watch_closest')
    LOOK_IDLE      = EntityTask('pig' ,'look_idle')


class PigZombie(LivingDefinition):
    def __init__(self):
        self.name = 'pig_zombie'
        self.short_usage_str = 'living.PIG_ZOMBIE'

    SWIM                     = EntityTask('pig_zombie' ,'swim')
    ATTACK_ON_COLLIDE        = EntityTask('pig_zombie' ,'attack_on_collide')
    AVOID                    = EntityTask('pig_zombie' ,'avoid')
    MOVE_TOWARDS_RESTRICTION = EntityTask('pig_zombie' ,'move_towards_restriction')
    WANDER                   = EntityTask('pig_zombie' ,'wander')
    WATCH_CLOSEST            = EntityTask('pig_zombie' ,'watch_closest')
    LOOK_IDLE                = EntityTask('pig_zombie' ,'look_idle')


class Rabbit(LivingDefinition):
    def __init__(self):
        self.name = 'rabbit'
        self.short_usage_str = 'living.RABBIT'

    SWIM                = EntityTask('rabbit' ,'swim')
    RABBIT_PANIC        = EntityTask('rabbit' ,'rabbit_panic')
    TEMPT               = EntityTask('rabbit' ,'tempt')
    MATE                = EntityTask('rabbit' ,'mate')
    RABBIT_RAID_FARM    = EntityTask('rabbit' ,'rabbit_raid_farm')
    WANDER              = EntityTask('rabbit' ,'wander')
    WATCH_CLOSEST       = EntityTask('rabbit' ,'watch_closest')
    RABBIT_AVOID_WOLVES = EntityTask('rabbit' ,'rabbit_avoid_wolves')


class Sheep(LivingDefinition):
    def __init__(self):
        self.name = 'sheep'
        self.short_usage_str = 'living.SHEEP'

    SWIM          = EntityTask('sheep' ,'swim')
    PANIC         = EntityTask('sheep' ,'panic')
    MATE          = EntityTask('sheep' ,'mate')
    TEMPT         = EntityTask('sheep' ,'tempt')
    FOLLOW_PARENT = EntityTask('sheep' ,'follow_parent')
    EAT_GRASS     = EntityTask('sheep' ,'eat_grass')
    WANDER        = EntityTask('sheep' ,'wander')
    WATCH_CLOSEST = EntityTask('sheep' ,'watch_closest')
    LOOK_IDLE     = EntityTask('sheep' ,'look_idle')


class Silverfish(LivingDefinition):
    def __init__(self):
        self.name = 'silverfish'
        self.short_usage_str = 'living.SILVERFISH'

    SWIM                     = EntityTask('silverfish' ,'swim')
    SUMMON_SILVERFISH        = EntityTask('silverfish' ,'summon_silverfish')
    ATTACK_ON_COLLIDE        = EntityTask('silverfish' ,'attack_on_collide')
    SILVERFISH_HIDE_IN_STONE = EntityTask('silverfish' ,'silverfish_hide_in_stone')


class Skeleton(LivingDefinition):
    def __init__(self):
        self.name = 'skeleton'
        self.short_usage_str = 'living.SKELETON'

    SWIM              = EntityTask('skeleton' ,'swim')
    AVOID_SUN         = EntityTask('skeleton' ,'avoid_sun')
    AVOID             = EntityTask('skeleton' ,'avoid')
    FLEE_SUN          = EntityTask('skeleton' ,'flee_sun')
    AVOID             = EntityTask('skeleton' ,'avoid')
    WANDER            = EntityTask('skeleton' ,'wander')
    WATCH_CLOSEST     = EntityTask('skeleton' ,'watch_closest')
    LOOK_IDLE         = EntityTask('skeleton' ,'look_idle')
    ATTACK_ON_COLLIDE = EntityTask('skeleton' ,'attack_on_collide')


class Slime(LivingDefinition):
    def __init__(self):
        self.name = 'slime'
        self.short_usage_str = 'living.SLIME'

    SLIME_FLOAT       = EntityTask('slime' ,'slime_float')
    SLIME_ATTACK      = EntityTask('slime' ,'slime_attack')
    SLIME_FACE_RANDOM = EntityTask('slime' ,'slime_face_random')
    SLIME_HOP         = EntityTask('slime' ,'slime_hop')


class Snowman(LivingDefinition):
    def __init__(self):
        self.name = 'snowman'
        self.short_usage_str = 'living.SNOWMAN'

    ATTACK_WITH_ARROW = EntityTask('snowman' ,'attack_with_arrow')
    WANDER            = EntityTask('snowman' ,'wander')
    WATCH_CLOSEST     = EntityTask('snowman' ,'watch_closest')
    LOOK_IDLE         = EntityTask('snowman' ,'look_idle')


class Spider(LivingDefinition):
    def __init__(self):
        self.name = 'spider'
        self.short_usage_str = 'living.SPIDER'

    SWIM           = EntityTask('spider' ,'swim')
    AVOID          = EntityTask('spider' ,'avoid')
    LEAP_AT_TARGET = EntityTask('spider' ,'leap_at_target')
    SPIDER_ATTACK  = EntityTask('spider' ,'spider_attack')
    SPIDER_ATTACK  = EntityTask('spider' ,'spider_attack')
    WANDER         = EntityTask('spider' ,'wander')
    WATCH_CLOSEST  = EntityTask('spider' ,'watch_closest')
    LOOK_IDLE      = EntityTask('spider' ,'look_idle')


class Squid(LivingDefinition):
    def __init__(self):
        self.name = 'squid'
        self.short_usage_str = 'living.SQUID'

    SQUID_MOVE_RANDOM = EntityTask('squid' ,'squid_move_random')


class Villager(LivingDefinition):
    def __init__(self):
        self.name = 'villager'
        self.short_usage_str = 'living.VILLAGER'

    SWIM                          = EntityTask('villager' ,'swim')
    AVOID                         = EntityTask('villager' ,'avoid')
    TRADE_WITH_PLAYER             = EntityTask('villager' ,'trade_with_player')
    LOOK_AT_TRADE_PLAYER          = EntityTask('villager' ,'look_at_trade_player')
    MOVE_INDOOR                   = EntityTask('villager' ,'move_indoor')
    AVOID_DOORS                   = EntityTask('villager' ,'avoid_doors')
    OPEN_DOOR                     = EntityTask('villager' ,'open_door')
    MOVE_TOWARDS_RESTRICTION      = EntityTask('villager' ,'move_towards_restriction')
    MATE_WITH_OTHER_VILLAGER      = EntityTask('villager' ,'mate_with_other_villager')
    FOLLOW_GOLEM                  = EntityTask('villager' ,'follow_golem')
    WATCH_CLOSEST_2               = EntityTask('villager' ,'watch_closest_2')
    INTERACT_WITH_OTHER_VILLAGERS = EntityTask('villager' ,'interact_with_other_villagers')
    WANDER                        = EntityTask('villager' ,'wander')
    WATCH_CLOSEST                 = EntityTask('villager' ,'watch_closest')


class Witch(LivingDefinition):
    def __init__(self):
        self.name = 'witch'
        self.short_usage_str = 'living.WITCH'

    SWIM              = EntityTask('witch' ,'swim')
    ATTACK_WITH_ARROW = EntityTask('witch' ,'attack_with_arrow')
    WANDER            = EntityTask('witch' ,'wander')
    AVOID             = EntityTask('witch' ,'avoid')
    WATCH_CLOSEST     = EntityTask('witch' ,'watch_closest')
    LOOK_IDLE         = EntityTask('witch' ,'look_idle')


class Wither(LivingDefinition):
    def __init__(self):
        self.name = 'wither'
        self.short_usage_str = 'living.WITHER'

    SWIM              = EntityTask('wither' ,'swim')
    ATTACK_WITH_ARROW = EntityTask('wither' ,'attack_with_arrow')
    WANDER            = EntityTask('wither' ,'wander')
    WATCH_CLOSEST     = EntityTask('wither' ,'watch_closest')
    LOOK_IDLE         = EntityTask('wither' ,'look_idle')


class Wolf(LivingDefinition):
    def __init__(self):
        self.name = 'wolf'
        self.short_usage_str = 'living.WOLF'

    SWIM              = EntityTask('wolf' ,'swim')
    SIT               = EntityTask('wolf' ,'sit')
    LEAP_AT_TARGET    = EntityTask('wolf' ,'leap_at_target')
    ATTACK_ON_COLLIDE = EntityTask('wolf' ,'attack_on_collide')
    FOLLOW_OWNER      = EntityTask('wolf' ,'follow_owner')
    MATE              = EntityTask('wolf' ,'mate')
    WANDER            = EntityTask('wolf' ,'wander')
    BEG               = EntityTask('wolf' ,'beg')
    WATCH_CLOSEST     = EntityTask('wolf' ,'watch_closest')
    LOOK_IDLE         = EntityTask('wolf' ,'look_idle')


class Zombie(LivingDefinition):
    def __init__(self):
        self.name = 'zombie'
        self.short_usage_str = 'living.ZOMBIE'

    SWIM                     = EntityTask('zombie' ,'swim')
    ATTACK_ON_COLLIDE        = EntityTask('zombie' ,'attack_on_collide')
    AVOID                    = EntityTask('zombie' ,'avoid')
    MOVE_TOWARDS_RESTRICTION = EntityTask('zombie' ,'move_towards_restriction')
    WANDER                   = EntityTask('zombie' ,'wander')
    WATCH_CLOSEST            = EntityTask('zombie' ,'watch_closest')
    LOOK_IDLE                = EntityTask('zombie' ,'look_idle')
    ATTACK_ON_COLLIDE        = EntityTask('zombie' ,'attack_on_collide')
    ATTACK_ON_COLLIDE        = EntityTask('zombie' ,'attack_on_collide')
    MOVE_THROUGH_VILLAGE     = EntityTask('zombie' ,'move_through_village')

