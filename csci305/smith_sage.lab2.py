import re

def mkgraph(file_name):
    graph = {}

    f = open(file_name,'r')
    read = False
    for line in f.readlines():
        words = re.split('\s\s+', line.strip())
        if '-' not in words[0] and 'From' not in words[0]:
            if words[0] not in graph:
                graph[words[0]] = {}

            for i in range(1, len(words)-1):
                if words[i] not in graph:
                    graph[words[i]] = {}

                if words[0] is not words[i]:
                    graph[words[0]][words[i]] = words[len(words)-1]
                    graph[words[i]][words[0]] = words[len(words)-1]
    f.close()

    return graph

def num_con(graph, city):
    return str(len(graph[city]))

def is_dir_con(graph, city0, city1):
    return 'Yes' if city1 in graph[city0] else 'No'

def is_khop_con(graph, city0, city1, k):
    return 'Not yet coded'

def is_con(graph, city0, city1):
    return bfs(graph, city0, city1)

def bfs(graph, city0, city1):
    visited = []
    cities_to_visit = []
    city_paths = {}
    last_city = ''
    current_city = city0
    first = True

    while(len(cities_to_visit)>0 or first):
        if first:
            first = False
            printstr = current_city
        else:
            last_city = current_city
            current_city = cities_to_visit.pop()
            city_paths[last_city] = current_city

        if current_city not in visited:
            potential_cities = graph[current_city]
            visited.append(current_city)

            if city0 in visited and city1 in potential_cities:
                city_paths[current_city] = city1
                cur = city0
                dist = 0
                ans = 'Yes\n'
                path = city1 + ' -> '

                while cur is not city1:
                    dist+=int(graph[cur][city_paths[cur]])
                    cur = city_paths[cur]


                    if cur is not city1:
                        path += cur + ' -> '
                    else:
                        path+=cur
                return 'Path: '+path+'\nTotal Distance: '+str(dist)


            for city in potential_cities:
                if city not in visited:
                    cities_to_visit.insert(0, city)
    return 'No'

def main():
    graph = mkgraph('city.txt')
    command = ''

    while command is not 'q':
        command = raw_input('n: number of directly connected cities\nd: query if two cities are directly connected\nk: query if there is a khop connection\nc: query if two cities are connected\nq: quit\n\nEnter Command: ')

        if command is 'n':
            city = raw_input('Enter City: ')
            print num_con(graph, city) + '\n'

        elif command is 'd':
            city0 = raw_input('Enter City 0: ')
            city1 = raw_input('Enter City 1: ')
            print is_dir_con(graph, city0, city1) + '\n'

        elif command is 'k':
            city0 = raw_input('Enter City 0: ')
            city1 = raw_input('Enter City 1: ')
            k = raw_input('Number of Hops: ')
            print is_khop_con(graph, city0, city1, k) + '\n'

        elif command is 'c':
            city0 = raw_input('Enter City 0: ')
            city1 = raw_input('Enter City 1: ')
            print is_con(graph, city0, city1) + '\n'

        elif command is 'q':
            print "See you later\n"

        elif command is 'l':
            print graph.keys()

        else:
            print 'invalid input\n'





if __name__ == "__main__":
    main()
