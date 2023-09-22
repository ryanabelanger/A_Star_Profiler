import pprint
import heapq
import random
import math
import time

pp = pprint.PrettyPrinter()
n_steps = [(0, 1), (0, -1), (-1, 0), (1, 0)]
w_range = [100, 150, 250, 400, 500, 1000, 2000, 2500]
h_range = [100, 150, 250, 400, 500, 1000, 2000, 2500]
subsection_size = 10
sample_size = 5


def get_pythag_dist(start, end):
    return int(math.sqrt(pow((start[0] - end[0]), 2) + pow((start[1] - end[1]), 2)))


def get_manhat_dist(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def a_star(map_list, start, hatch):
    to_search = [(0, start)]
    searched = set()
    parents = {start: None}
    g_values = {coord: float('inf') for coord in map_list}
    g_values[start] = 0
    f_values = {coord: float('inf') for coord in map_list}
    f_values[start] = get_manhat_dist(start, hatch)

    while to_search:
        current_f, current_node = heapq.heappop(to_search)
        if current_node == hatch:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parents[current_node]
            return list(reversed(path))
        searched.add(current_node)
        removes = list(n_steps)
        random.shuffle(removes)
        for direction in removes:
            dx, dy = direction
            neighbor = current_node[0] + dx, current_node[1] + dy
            if neighbor not in map_list or neighbor in searched:
                continue
            potential_g = g_values[current_node] + 1
            if potential_g < g_values[neighbor]:
                parents[neighbor] = current_node
                g_values[neighbor] = potential_g
                f_values[neighbor] = potential_g + get_manhat_dist(neighbor, hatch)
                if neighbor not in [node[1] for node in to_search]:
                    heapq.heappush(to_search,(f_values[neighbor], neighbor))
    return None


def divide_map(bmap):
    section_size = subsection_size
    sections = {}
    for x, y in bmap:
        section_x = x // section_size
        section_y = y // section_size
        section = (section_x, section_y)
        if section not in sections:
            sections[section] = []
        sections[section].append((x, y))
    return sections


def build_map(wide, tall):
    res_map = []
    for i in range(wide):
        for j in range(tall):
            res_map.append((i, j))
    print(f'Map created for {wide}x{tall}, {len(res_map)} squares')
    return res_map


class MapV1:
    def __init__(self, map_width, map_height):
        self.map = build_map(map_width, map_height)
        self.name = f'{len(self.map)}'
        self.metamap_1 = divide_map(self.map)
        self.metamap_2 = divide_map(self.metamap_1)
        self.hatch = self.ret_random_loc()

    def ret_random_loc(self):
        return random.choice(self.map)

    def get_path_1(self, start):
        time1 = time.time()
        path = a_star(self.map, start, self.hatch)
        calc_time = round(time.time() - time1, 5)
        ret_dict = {'p': len(path), 't': calc_time, 'l': 1}
        return ret_dict

    def get_path_2(self, start):
        time1 = time.time()
        end = self.hatch
        meta_path = a_star(self.metamap_1,
                           (start[0]//subsection_size, start[1]//subsection_size),
                           (end[0]//subsection_size, end[1]//subsection_size))
        searchable_map = []
        for section in meta_path:
            searchable_map.extend(self.metamap_1[section])
        path = a_star(searchable_map, start, self.hatch)
        calc_time = round(time.time() - time1, 5)
        ret_dict = {'p': len(path), 't': calc_time, 'm': 2}
        return ret_dict


def main():
    maplist = []
    i = 0
    while i < len(w_range):
        maplist.append(MapV1(w_range[i], h_range[i]))
        i += 1
    print(f'Created {len(maplist)} maps')
    mapdict = {}
    for m in maplist:
        map_name = f'Map_{str(m.name)}'
        mapdict[map_name] = {}
        starting_locs = []
        for l in range(sample_size):
            starting_locs.append(m.ret_random_loc())
        for c in starting_locs:
            mapdict[map_name][str(c)] = m.get_path_2(c)
    pp.pprint(mapdict)


if __name__ == '__main__':
    main()
