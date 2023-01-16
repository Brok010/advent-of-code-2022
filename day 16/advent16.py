from valve import valves

Valves = [] #dic of classes
for valve in valves:
    Valves.append(valve.get_attributes())

def logic(minutes, destinations):
    #inicialization
    for dic in destinations:
        dic['cost'] = 0
        dic['prio'] = 0
        if dic['name'] == 'AA':
            start = dic
    
    #logic
    pressure_released = 0
    while minutes > 0:
        c, p = alg(minutes, destinations, start)
        minutes -= c + 1 #1 min for opening a valve
        pressure_released += p #minutes left
    
    return pressure_released
    
def alg(minutes, destinations, start):   #dijkstras alg
    #inicializations
    stack = []
    stack.append(start)
    visited = []
    paths = [{'name': start['name'], 'cost': start['cost'], 'prio': start['prio']}]

    #finding paths
    while stack != []:
        dic = stack.pop()
        visited.append(dic) #here?
        neighbours = dic['tunnels']
        for neighbour in neighbours:
            for d in destinations:
                if d['name'] == neighbour:
                    flow_rate = d['flow-rate']
                    break
            cost = dic['cost'] + 1
            prio = (minutes - cost - 1) * int(flow_rate) #the neighbours flow rate
            temp = {'name': neighbour, 'cost': cost, 'prio': prio}
            
            #puting neighbours in paths
            flag = False
            if paths != []:   
                for i in reversed(range(len(paths))):
                    if paths[i]['name'] == neighbour and paths[i]['cost'] > cost:
                        paths.remove(paths[i])
                        paths.append(temp)
                        flag = True
                        break
                    elif paths[i]['name'] == neighbour and paths[i]['cost'] <= cost:
                        flag = True
                        break
                if flag == False:
                    paths.append(temp)
            else:
                paths.append(temp)
            
            #repopulating stack
            if neighbour not in [d["name"] for d in visited]:
                for d in destinations:
                    if d['name'] == neighbour:
                        d['cost'] = cost
                        d['prio'] = prio
                        break

                if neighbour not in [d["name"] for d in stack]:
                    stack.append(d)
                
                #if the neigbour has an instance inside of the paths already
                else:
                    for i in reversed(range(len(stack))):
                        if stack[i]['name'] == neighbour and stack[i]['cost'] > d['cost']:
                            stack.remove(paths[i])
                            stack.append(d)
                            break
    
    #remove paths that have cost > minutes - 1
    for i in reversed(range(len(paths))):
        if paths[i]['cost'] > minutes - 1:
            paths.remove(paths[i])


    #get the best path of all
    temp_max = 0
    temp_path = {'name': '', 'cost': 0, 'prio': 0}
    for path in paths:
        if path['prio'] > temp_max:
            temp_path = path
            temp_max = temp_path['prio']
        elif path['prio'] == temp_max and path['cost'] < temp_path['cost']:
            temp_path = path
            temp_max = temp_path['prio']
    
    #set the winning valve to 0
    name = temp_path['name']
    for dic in destinations:
        if dic['name'] == name:
            dic['flow-rate'] = 0

    #returning the time cost and presure released    
    return temp_path['cost'], temp_path['prio']

minutes = 30
print(logic(minutes, Valves))