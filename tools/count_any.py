import re, os, sys

func_stats = {"any": 0, "bool": 0, "str": 0, "int": 0}
assign_stats = {"any": 0, "bool": 0, "str": 0, "int": 0}
func_total = 0
assign_total = 0
reg_func = "-> .+:"
reg_assign = ": .+"

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
        func_total += 1


def analyze_files(f):
    fd = open(f, "r")
    lines = fd.readlines()
    for line in lines:
        # Check for func
        res = re.findall(reg_func, line)
        if len(res) == 1:
            count(res[0], func=True)
        # Check for assign
        res = re.findall(reg_assign, line)
        if len(res) > 0:
            for x in res:
                count(x, assign=True)

def main():
    d = "../big/allrepo/stripped/" 
    for root, dirs, files in os.walk(d):
        for file in files:
            if file.endswith(".pyi"):
                analyze_files(os.path.join(root, file))
    print(f"Total functions: {func_total}")
    for x in func_stats.keys():
        print(f"Total functions with {x} return type: {func_stats[x]}") 
        print(f"Percent of functions with this return type: {(func_stats[x]/func_total) * 100}")
    print()
    print(f"Total assignments: {assign_total}")
    for x in assign_stats.keys():
        print(f"Total assignments with {x} type: {assign_stats[x]}") 
        print(f"Percent of assignments with this type: {(assign_stats[x]/assign_total) * 100}")

if __name__ == "__main__":
    main()
