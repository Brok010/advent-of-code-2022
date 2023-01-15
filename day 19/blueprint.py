#Read input, parse and load data into the class
#Read
descriptions = []
with open("input.txt") as file:
    for row in file:
        descriptions.append(row.strip())

class Blueprint:
    def __init__(self, num, ore_robot_cost, clay_robot_cost, obsidian_robot_cost, geode_robot_cost):
        self.num = num
        self.ore_robot_cost = ore_robot_cost
        self.clay_robot_cost = clay_robot_cost
        self.obsidian_robot_cost = obsidian_robot_cost
        self.geode_robot_cost = geode_robot_cost

    #to print all
    def get_attributes(self):
        attributes = {'number': self.num, 'ore_cost': self.ore_robot_cost, 'clay_cost': self.clay_robot_cost, 'obsidian_cost': obsidian_robot_cost, 'geode_cost': geode_robot_cost}
        return attributes

#list to store all class instances
blueprints = []

#Parsing
#Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 5 clay. Each geode robot costs 3 ore and 15 obsidian.
for description in descriptions:
    num, ore_robot_cost, clay_robot_cost, obsidian_robot_cost, geode_robot_cost = 0, 0, 0, [0, 0], [0, 0]
    words = description.split() #splits string into words
       
# extract robot cost information
    for i in range(len(words)):

        #get Blueprint number
        if words[i] == "Blueprint":
            num_str = words[i + 1]
            num_str = num_str.replace(":", "") #removes the colon
            num = int(num_str)

        #gets the ore cost of the ore robot
        elif words[i] == "ore" and words[i + 1] == "robot":
            ore_robot_cost = int(words[i + 3])

        #gets the ore cost of the clay robot
        elif words[i] == "clay" and words[i + 1] == "robot":
            clay_robot_cost = int(words[i + 3])
        
        #gets the ore cost and clay cost of the obsidian robot
        elif words[i] == "obsidian" and words[i + 1] == "robot":
            obsidian_robot_cost[0] = int(words[i + 3])
            obsidian_robot_cost[1] = int(words[i + 6])

        #gets the ore cost and clay cost of the geode robot
        elif words[i] == "geode" and words[i + 1] == "robot":
            geode_robot_cost[0] = int(words[i + 3])
            geode_robot_cost[1] = int(words[i + 6])
    
    #still in the parsing loop - for each description, i make and append a blueprint
    blueprint = Blueprint(num, ore_robot_cost, clay_robot_cost, obsidian_robot_cost, geode_robot_cost)
    blueprints.append(blueprint)
    
#prints all
def print_blueprint():
    for blueprint in blueprints:
        print(blueprint.get_attributes())