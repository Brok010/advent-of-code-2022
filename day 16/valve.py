input = []
file = open('input.txt')
for row in file:
    input.append(row.strip())

class Valve:
    def __init__(self, name, flow_rate, tunnels):
        self.name = name
        self.flow_rate = flow_rate
        self.tunnels = tunnels
    
    #to print all
    def get_attributes(self):
        attributes = {'name': self.name, 'flow-rate': self.flow_rate, 'tunnels': self.tunnels}
        return attributes

valves = []

name, flow_rate, tunnels = '', 0, []
for row in input:
    row = row.split()
    length = len(row)
    name = row[1]
    flow_rate = row[4][5:].replace(';', '')
    tunnels = []
    tunnels.append(row[-1])
    i = 2
    while length > 10:
        tunnels.append(row[-i].replace(',',''))
        i += 1
        length -= 1
    valve = Valve(name, flow_rate, tunnels)
    valves.append(valve)