def solution(l):
    result = []
    table = []
    final = []
    for item in l:
        if item.count('.') == 0:
            table.append({'version': int(item), 'minor': -1, 'revision': -1})
        elif item.count('.') == 1:
            list = item.split(".")
            table.append({'version': int(list[0]), 'minor': int(list[1]), 'revision': -1})
        elif item.count('.') == 2:
            list = item.split(".")
            table.append({'version': int(list[0]), 'minor': int(list[1]), 'revision': int(list[2])})
    for i in range(len(table)):
        min = table[0]
        for item in table:
            if item['version'] < min['version']:
                min = item
            elif item['version'] == min['version'] and item['minor'] < min['minor']:
                min = item
            elif item['version'] == min['version'] and item['minor'] == min['minor'] and item['revision'] < min['revision']:
                min = item
        result.append(min)
        table.remove(min)
    for item in result:
        minor = '.' + str(item['minor']) if item['minor'] != -1 else ''
        revision = '.' + str(item['revision']) if item['revision'] != -1 else ''
        final.append(str(item['version']) + minor + revision)
    return final


if __name__ == "__main__":
    n = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0", '2.1', '11.1']

    b = solution(n)
    print(b)
