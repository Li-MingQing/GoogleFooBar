def solution(map):
# Your code here
    global table
    table = []
    global map1
    map1 = map.copy()
    for i in range(len(map)):
        for j in range(len(map[0])):
            table.append((i,j,map[i][j]))
    #print(table)
    possibleRoute = [[(0,0,map[0][0]),(0,1,map[0][1])],
                     [(0,0,map[0][0]),(1,0,map[1][0])],
                    ]
    a = findNextStep(possibleRoute)

    """
    for item in possibleRoute:
        result = item
        #print(item)
        newRoute = []
        x = item[len(item)-1]
        y = item[len(item)-1]['y']
        xprevious = item[len(item)-2]['x']
        yprevious = item[len(item)-2]['y']
        sum = 0
        for element in item:
            sum += element['value']

        if x != len(map)-1 and y != len(map[0])-1:
            if x == xprevious + 1:
                if {'x': x + 1, 'y': y, 'value': map[x + 1][y]} in table:
                    if sum +map[x + 1][y] <= 1:
                        newRoute.append({'x': x + 1, 'y': y, 'value': map[x + 1][y]})
                if {'x': x, 'y': y + 1,'value': map[x][y + 1]} in table:
                    if sum + map[x][y + 1] <= 1:
                        newRoute.append({'x': x, 'y': y + 1, 'value': map[x][y+1]})
                if {'x': x, 'y': y - 1,'value': map[x][y - 1]} in table:
                    if sum + map[x][y - 1] <= 1:
                        newRoute.append({'x': x, 'y': y-1, 'value': map[x][y-1]})
            elif x == xprevious - 1:
                if {'x': x - 1, 'y': y, 'value': map[x - 1][y]} in table:
                    if sum + map[x - 1][y] <= 1:
                        newRoute.append({'x': x - 1, 'y': y, 'value': map[x - 1][y]})
                if {'x': x, 'y': y + 1,'value': map[x][y + 1]} in table:
                    if sum + map[x][y + 1] <= 1:
                        newRoute.append({'x': x, 'y': y + 1, 'value': map[x][y+1]})
                if {'x': x, 'y': y - 1,'value': map[x][y - 1]} in table:
                    if sum + map[x][y - 1] <= 1:
                        newRoute.append({'x': x, 'y': y-1, 'value': map[x][y-1]})
            elif y == yprevious + 1:
                if {'x': x - 1, 'y': y, 'value': map[x - 1][y]} in table:
                    if sum + map[x - 1][y] <= 1:
                        newRoute.append({'x': x - 1, 'y': y, 'value': map[x - 1][y]})
                if {'x': x+1, 'y': y,'value': map[x+1][y]} in table:
                    if sum + map[x + 1][y] <= 1:
                        newRoute.append({'x': x+1, 'y': y, 'value': map[x+1][y]})
                if {'x': x, 'y': y + 1,'value': map[x][y + 1]} in table:
                    if sum + map[x][y + 1] <= 1:
                        newRoute.append({'x': x, 'y': y+1, 'value': map[x][y+1]})
            elif y == yprevious -1:
                if {'x': x - 1, 'y': y, 'value': map[x - 1][y]} in table:
                    if sum + map[x - 1][y] <= 1:
                        newRoute.append({'x': x - 1, 'y': y, 'value': map[x - 1][y]})
                if {'x': x+1, 'y': y,'value': map[x+1][y]} in table:
                    if sum + map[x + 1][y] <= 1:
                        newRoute.append({'x': x+1, 'y': y, 'value': map[x+1][y]})
                if {'x': x, 'y': y - 1,'value': map[x][y - 1]} in table:
                    if sum + map[x][y-1] <= 1:
                        newRoute.append({'x': x, 'y': y-1, 'value': map[x][y-1]})
            print(newRoute)
            for route in newRoute:
                possibleRoute.append(item.append(route))
            print(possibleRoute)
        else:
            return len(item)
    """
    return a

def findNextStep(possibleRoute):
    #print(possibleRoute)
    solution = []
    result = []
    minLen = []
    for item in possibleRoute:
        sum = 0
        print("item:" + str(item))
        for value in item:
            #print(value)
            sum += value[2]
        #print(sum)
        if sum > 1:
            continue
        else:
            length = len(item)
            x = item[length - 1][0]
            y = item[length - 1][1]
            if x != table[len(table) - 1][0] and y != table[len(table) - 1][1]:
                xprevious = item[length - 2][0]
                yprevious = item[length - 2][1]
                vprevious = item[length - 2][2]
                if (x+1,y,map1[x+1][y]) in table and (x+1,y,map1[x+1][y]) not in item:
                    if sum + map1[x+1][y] <= 1:
                        solution.append((x+1,y,map1[x+1][y]))
                if (x-1,y,map1[x-1][y]) in table and (x-1,y,map1[x-1][y]) not in item:
                    if sum + map1[x-1][y] <= 1:
                        solution.append((x-1,y,map1[x-1][y]))
                if (x,y+1,map1[x][y+1]) in table and (x,y+1,map1[x][y+1]) not in item:
                    if sum + map1[x][y+1] <= 1:
                        solution.append((x,y+1,map1[x][y+1]))
                if (x,y-1,map1[x][y-1]) in table and (x,y-1,map1[x][y-1]) not in item:
                    if sum + map1[x][y-1] <= 1:
                        solution.append((x,y-1,map1[x][y-1]))
                print("solution:" + str(solution))
                #print(item)

                for s in solution:
                    #print(s)
                    i = item.copy()
                    #print(i)
                    i.append(s)
                    #print(i)
                    result.append(i)
                print("result:" + str(result))
                solution = []
            else:
                #minLen.append(len(item))
                return len(item)

    """
    if len(minLen) != 0:
        min = minLen[0]
        for i in minLen:
            if i < min:
                min = i
    if len(minLen) != 0:
        return min
    else:
        findNextStep(result)
    """
    findNextStep(result)


if __name__ == "__main__":
    m = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
    a = solution(m)
    print(a)
