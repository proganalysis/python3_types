import re, os, sys

func_total = 0
func_any_total = 0
reg_func = "-> .+:"

assign_total = 0
assign_any_total = 0
reg_assign = ": .+"

def count_any(f):
    global func_total
    global func_any_total
    global assign_total
    global assign_any_total
    fd = open(f, "r")
    lines = fd.readlines()
    for line in lines:
        # Check for func
        res = re.findall(reg_func, line)
        if len(res) == 1:
            if 'Any' in res[0]:
                func_any_total += 1
            func_total += 1
        # Check for assign
        res = re.findall(reg_assign, line)
        if len(res) > 0:
            for x in res:
                if 'Any' in x:
                    assign_any_total += 1
                assign_total += 1



def main():
    d = "../allrepo/stripped/" 
    for root, dirs, files in os.walk(d):
        for file in files:
            if file.endswith(".pyi"):
                count_any(os.path.join(root, file))
    print(f"Total functions: {func_total}")
    print(f"Any return types: {func_any_total}")
    print(f"Percent: {func_any_total/func_total}")
    print()
    print(f"Total assignments: {assign_total}")
    print(f"Any-typed assignments: {assign_any_total}")
    print(f"Percent: {assign_any_total/assign_total}")

if __name__ == "__main__":
    main()
