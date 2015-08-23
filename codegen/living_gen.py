import os
import sys
import json
import string
import types

# TODO: ANY
# TODO: type the individual tasks
# TODO: in the api, when creating an entity, set the current player, or nearest player, as the owner



# might be worth building up to these methods...and teach iteration.
#     having a whole bunch of animals sit and stand makes an impression

# for thing in my_path():
#        if type(thing) == living.OCELOT:
#                start_task(living.OCELOT.FOLLOW_OWNER, target=thing) # type check - server error if can't apply this...

# for thing in my_path():
#        if type(thing) == living.OCELOT:
#                reset_task(living.OCELOT.FOLLOW_OWNER, target=thing)

# pen_down(living.OCELOT)
# start_task(living.ANY.FOLLOW_OWNER) # implicit select of things that have this task
# start_task(living.OCELOT.FOLLOW_OWNER) # implicit select of ocelots
# start_task(living.OCELOT.FOLLOW_OWNER, select=recent(living.OCELOT))
# start_task(living.OCELOT.FOLLOW_OWNER, select=recent(living.OCELOT, offset))
# start_task(living.OCELOT.FOLLOW_OWNER, select=recent(living.OCELOT, range))
# start_task(living.OCELOT.FOLLOW_OWNER, select=beginning(living.OCELOT, offset))
# start_task(living.OCELOT.FOLLOW_OWNER, select=beginning(living.OCELOT, range))

# reset_task(living.OCELOT.FOLLOW_OWNER)


# TODO: generate markdown docs
#     transform to ipython

# TODO: do something similar for entities
#     enumerate entity tasks...
# entity.startTask(uuid (or array...?), tasks.OCELOT_SIT)
# entity.startTask(uuid, tasks.OCELOT_FOLLOW_OWNER)
# entity.stopTask(uuid, tasks.OCELOT_FOLLOW_OWNER)
# ...will need lots of error checking / help...
# also use type to determine whether task was mis-applied
# entity.create(x, y, z, entity.OCELOT) : uuid
# entity.getNearest(x, y, z, entity.OCELOT, 7) : uuid[]

# pendown(entity.OCELOT)
# penup()
# turtle/functional method...
# start(tasks.OCELOT_FOLLOW_OWNER, select(entity.OCELOT, trail())
# ...or just match only things created that task would apply to (default select)
# ...and trail() is implicit too
# start(tasks.OCELOT_FOLLOW_OWNER)
# start(tasks.OCELOT_FOLLOW_OWNER, select=entity.OCELOT)
# start(tasks.OCELOT_FOLLOW_OWNER, select=first(entity.OCELOT))
# start(tasks.OCELOT_FOLLOW_OWNER, select=last(entity.OCELOT))
# stop(tasks.OCELOT_FOLLOW_OWNER)
# start(tasks.OCELOT_MATE)
# start(tasks.OCELOT_ATTACK)
# select_distance(entity.OCELOT, 100, uuid=reference)
# select_distance(entity.OCELOT, 100, x= y= z=)

INDENT = "    "

this_dir = os.path.dirname(os.path.realpath(__file__))
livings = json.loads(open(os.path.join(this_dir, "living_metadata.json")).read())
livings = sorted(livings, key=lambda l: l["name"])

# we're optimizing for decent tab completion. split the definition and livings in to separate files.
target_definition_file = os.path.join(this_dir, "../mcgamedata/living_definition.py")
target_living_file = os.path.join(this_dir, "../mcgamedata/living.py")

living_definition_lines = [
    "class LivingDefinition():",
    "    pass",
    "",
    "class EntityTask():",
    INDENT + "def __init__(self, entity_name, task_name):",
    INDENT + INDENT + "self.entity_name = entity_name",
    INDENT + INDENT + "self.task_name = task_name",
    ""
]

    # {
    #     "name": "ocelot",
    #     "tasks": [
    #         "avoid",
    #         "swim",
    #         "sit",
    #         "tempt",
    #         "follow_owner",
    #         "ocelot_sit",
    #         "leap_at_target",
    #         "ocelot_attack",
    #         "mate",
    #         "wander",
    #         "watch_closest"
    #     ]
    # }

all_living = []
all_tasks = []

for living in livings:
    for task in living["tasks"]:
        if task not in all_tasks:
            all_tasks.append(task)

all_tasks = sorted(all_tasks)
livings.insert(0, {"name": "any", "tasks": all_tasks})

for living in livings:
    lowercase_living_name = living["name"]
    uppercase_living_name = lowercase_living_name.upper()
    upper_camel_living_name = string.capwords(lowercase_living_name, "_").replace("_", "")

    all_living.append({'upper':uppercase_living_name, 'camel':upper_camel_living_name})

    living_definition_lines.extend([
        "",
        "class " + upper_camel_living_name + "(LivingDefinition):",
        INDENT + "def __init__(self):",
        INDENT + INDENT + "self.name = '" + lowercase_living_name + "'",
        ""
    ])

    task_value_lines = []
    max_task_value_name_length = 0

    for task in living["tasks"]:
        lowercase_task_name = task
        uppercase_task_name = task.upper()

        task_value_lines.append([uppercase_task_name, "'" + task + "'"])
        if len(uppercase_task_name) > max_task_value_name_length:
            max_task_value_name_length = len(uppercase_task_name)

    for line in task_value_lines:
        value_line = line[0].ljust(max_task_value_name_length) + " = " + \
            "EntityTask('" + lowercase_living_name + "' ," + line[1] + ")"
        living_definition_lines.append(INDENT + value_line)

    living_definition_lines.append("")

body = "\n".join(living_definition_lines) + "\n"
print body
f = open(target_definition_file, 'w')
f.write(body)
f.close()

living_lines = [
    "import living_definition",
    "",
    "ALL = []",
    ""
]

max_living_name_length = 0
for living in all_living:
    if len(living['upper']) > max_living_name_length:
        max_living_name_length = len(living['upper'])

for living in all_living:
    living_lines.append(living['upper'].ljust(max_living_name_length) + " = living_definition." + \
        living['camel'] + "(); ALL.append(" + living['upper'] + ")")

body = "\n".join(living_lines) + "\n"
print body
f = open(target_living_file, 'w')
f.write(body)
f.close()
