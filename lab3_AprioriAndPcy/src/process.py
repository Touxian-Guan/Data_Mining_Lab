def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    data = []
    for line in lines:
        parts = line.strip().split(', ')
        word = parts[0]
        if len(parts) == 3:
            titles = [parts[1].replace('(', '').replace(')', '')]
        elif len(parts) == 4:
            titles = []
            titles.insert(0, parts[1].replace('(', ''))
            titles.insert(1, parts[2].replace(')', ''))
        else:
            titles = []
            titles = parts[2:-2]
            titles.insert(0, parts[1].replace('(', ''))
            titles.append(parts[-2].replace(')', ''))

        titles.insert(0, parts[0])
        data.append(titles)
    
    return data