#badly optimized, but algorithm works
#posible opt - it doesnt make sense to buy a robot the next round if we have
#       enough material and are not building a robot current loop - so
#       delete those branches too

from blueprint import blueprints
import copy

#load dictionaries to list
bp = []
for blueprint in blueprints:
    bp.append(blueprint.get_attributes())
# print(bp)

def logic(BP, Depth):
    #inicialization
    stack = []
    path = []
    ores = [1,0,0,0]
    robots = [1,0,0,0]
    cur_depth = 1
    till_end = Depth - cur_depth - 1
    choices = get_choices(BP, ores, robots, till_end)
    stack.append({'path': path, 'depth': cur_depth, 'robots': robots, 'ores': ores, 'choices': choices})
    
    #dfs - stack creation
    while cur_depth < Depth:
        cur_depth += 1
        till_end = Depth - cur_depth - 1
        for i in reversed(range(len(stack))):
            dic_depth = stack[i]['depth']
            if dic_depth == cur_depth - 1:
                for choice in stack[i]['choices']:
                    path = stack[i]['path'].copy()
                    path.append(choice)
                    ores = ore_update(stack[i]['ores'].copy(), stack[i]['robots'].copy())
                    robots, ores = choice_processing(choice, stack[i]['robots'].copy(), ores, BP)
                    choices = get_choices(BP, ores, robots, till_end)
                    node = {'path': path, 'depth': cur_depth, 'robots': robots, 'ores': ores, 'choices': choices}
                    stack.append(node)
            
            elif dic_depth < cur_depth - 1:
                stack.remove(stack[i])
                
    #result gather
    geode_dic = {}
    geode_max = 0
    for dic in stack:
        if dic['depth'] == Depth and dic['ores'][-1] > geode_max:
            geode_ore = dic['ores'][-1]
            geode_max = geode_ore
            path = dic['path'].copy()
            geode_dic = {'geode_count': geode_ore, 'path': path}
    return geode_dic

def ore_update(o, r):
    for i in range(4):
        o[i] += r[i]
    return o

#robot update
def choice_processing(arg, r, o, bp):
    if arg >= 0 and arg < 4:
        r[arg] += 1
        if arg == 0:
            o[0] -= bp['ore_cost']
        elif arg == 1:
            o[0] -= bp['clay_cost']
        elif arg == 2:
            o[0] -= bp['obsidian_cost'][0]
            o[1] -= bp['obsidian_cost'][1]
        elif arg == 3:
            o[0] -= bp['geode_cost'][0]
            o[2] -= bp['geode_cost'][1]
        return r, o
    elif arg == 4:
        return r, o
    else:
        print('error choice is not in range')


#returns a list of choices [0,1,2,3,4] - buy ore robot, clay robot, obsidian robot, geode robot, none
def get_choices(blueprint, ore, robot, till_end):
    choices = [0, 1, 2, 3, 4]
    basic_ore_costs = []
    basic_ore_costs = blueprint['ore_cost'],blueprint['clay_cost'], blueprint['obsidian_cost'][0], blueprint['geode_cost'][0]

    #variables for ore values
    basic_ore, clay, obsidian, geode = ore[0], ore[1], ore[2], ore[3]
    
    #variables for ore costs
    ore_robot_cost = blueprint['ore_cost']
    clay_robot_cost = blueprint['clay_cost']
    obsidian_robot_cost = blueprint['obsidian_cost']
    geode_robot_cost = blueprint['geode_cost']
    
    #if i cant afford anything, buy nothing
    if basic_ore < min(basic_ore_costs) and clay < obsidian_robot_cost[1] and obsidian < geode_robot_cost[1]:
        return [4]
    #if i can buy a geode robot, its optimal to do so
    elif basic_ore >= geode_robot_cost[0] and obsidian >=  geode_robot_cost[1]:
        return [3]
    
    #it never makes sense to buy more robots that the max cost of any robot
    if robot[0] >= max(basic_ore_costs):
        try:
            choices.remove(0)
        except ValueError:
            pass
    if robot[1] >= obsidian_robot_cost[1]:
        try:
            choices.remove(1)
        except ValueError:
            pass
    if robot[2] >= geode_robot_cost[1]:
        try:
            choices.remove(2)
        except ValueError:
            pass
    
    #it never makes sense to buy a robot of an ore of which we have more than we can use till the end of process
    if basic_ore >= max(basic_ore_costs) * till_end:
        try:
            choices.remove(0)
        except ValueError:
            pass
    if clay >= obsidian_robot_cost[1] * till_end:
        try:
            choices.remove(1)
        except ValueError:
            pass
    if obsidian >= geode_robot_cost[1] * till_end:
        try:
            choices.remove(2)
        except ValueError:
            pass

    #if i cant afford to buy i wont
    if basic_ore < ore_robot_cost:
        try:
            choices.remove(0)
        except ValueError:
            pass
    if basic_ore < clay_robot_cost:
        try:
            choices.remove(1)
        except ValueError:
            pass
    if basic_ore < obsidian_robot_cost[0] or clay < obsidian_robot_cost[1]:
        try:
            choices.remove(2)
        except ValueError:
            pass
    if basic_ore < geode_robot_cost[0] or obsidian < geode_robot_cost[1]:
        try:
            choices.remove(3)
        except ValueError:
            pass

    return choices

for each in bp:
    print(logic(each, 15))