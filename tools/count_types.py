import re, os, sys

func_stats = {"any": 0, "bool": 0, "str": 0, "int": 0, "None": 0, "TypeVar": 0, "Dict": 0, "List": 0, "Union": 0}
assign_stats = {"any": 0, "bool": 0, "str": 0, "int": 0, "None": 0, "TypeVar": 0, "Dict": 0, "List": 0, "Union": 0}
func_total = 0
assign_total = 0
reg_func = "-> .+:"
reg_assign = ": .+"
type_reg = "_T[0-9]"

func_return_map = {}
assignment_map = {}

def map_types(s, assign=False, func=False):
    global func_return_map
    global assignment_map
    if func:
        s = s.split('->')[1].split(':')[0].strip()
        if s in func_return_map.keys():
            func_return_map[s] += 1
        else:
            func_return_map[s] = 1
    
    if assign:
        s = s.split(':')[1].strip()
        if s in assignment_map.keys():
            assignment_map[s] += 1
        else:
            assignment_map[s] = 1



def count(s, assign=False, func=False):
    global func_total
    global assign_total
    global func_stats
    global assign_stats

    if assign:
        if 'Any' in s:
            assign_stats['any'] += 1
        elif 'bool' in s:
            assign_stats['bool'] += 1
        elif 'str' in s:
            assign_stats['str'] += 1
        elif 'int' in s:
            assign_stats['int'] += 1
        elif 'None' in s:
            assign_stats['None'] += 1
        elif len(re.findall(type_reg, s)) > 0:
            assign_stats['TypeVar'] += 1
        elif "List" in s:
            assign_stats["List"] += 1
        elif "Union" in s:
            assign_stats["Union"] += 1
        elif "Dict" in s:
            assign_stats["Dict"] += 1
        assign_total += 1
    elif func:
        if 'Any' in s:
            func_stats['any'] += 1
        elif 'bool' in s:
            func_stats['bool'] += 1
        elif 'str' in s:
            func_stats['str'] += 1
        elif 'int' in s:
            func_stats['int'] += 1
        elif 'None' in s:
            func_stats['None'] += 1
        elif len(re.findall(type_reg, s)) > 0:
            func_stats["TypeVar"] += 1
        elif "List" in s:
            func_stats["List"] += 1
        elif "Union" in s:
            func_stats["Union"] += 1
        elif "Dict" in s:
            func_stats["Dict"] += 1
        func_total += 1


def analyze_files(f):
    global assign_total
    global func_total
    fd = open(f, "r")
    lines = fd.readlines()
    for line in lines:
        # Check for func
        res = re.findall(reg_func, line)
        if len(res) == 1:
            func_total += 1
            map_types(res[0], func=True)
        # Check for assign
        res = re.findall(reg_assign, line)
        if len(res) > 0:
            for x in res:
                assign_total += 1
                map_types(x, assign=True)

def main():
    d = "/home/daniel/Documents/College/Semester7/Research/mypy-output/allrepo/original/" 
    for root, dirs, files in os.walk(d):
        for file in files:
            if file.endswith(".pyi"):
                analyze_files(os.path.join(root, file))
    '''
    print(f"Total functions: {func_total}")
    for x in func_stats.keys():
        print(f"Total functions with {x} return type: {func_stats[x]}") 
        print(f"Percent of functions with this return type: {(func_stats[x]/func_total) * 100}")
    print()
    print(f"Total assignments: {assign_total}")
    for x in assign_stats.keys():
        print(f"Total assignments with {x} type: {assign_stats[x]}") 
        print(f"Percent of assignments with this type: {(assign_stats[x]/assign_total) * 100}")
    '''
    print("\n------ Function return types ------\n")
    print(f"Total functions: {func_total}\n")
    for k in func_return_map.keys():
        print(f"{k}: {func_return_map[k]}") 
    
    print("\n------ Assignments types ------\n")
    print(f"Total assignments: {assign_total}\n")
    for k in assignment_map.keys():
        print(f"{k}: {assignment_map[k]}")

if __name__ == "__main__":
    main()
