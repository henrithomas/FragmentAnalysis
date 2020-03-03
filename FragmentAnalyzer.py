import re
fragment_list = []
val_list = []
lower = 100
upper = 500
f_name = 'C:\\Users\\mt200\\OneDrive\\Desktop\\School\\Concordia\\Genome Foundry\\FragmentAnalyzerOutput.csv'
with open(f_name) as f:
    for line in f:
        # check for a cell id
        if re.search("^[A-Z][0-9]+", line) is not None:
            if val_list:
                fragment_list.append(val_list.copy())
                # print(valList)
            val_list.clear()
            val_list = [line.split(',')[0]]
        # check for a peak id and grab size value
        elif re.search("^[0-9]+", line) is not None:
            val = int(line.split(',')[1].split(' ')[0])
            val_list.append(val)
    fragment_list.append(val_list.copy())

for lst in fragment_list:
    frags = ', '.join(['peak ' + str(i + 1) + ': ' + str(x)
                       for i, x in enumerate(lst[1:]) if lower <= x <= upper])
    if frags:
        cell_name = lst[0]
        print(cell_name)
        print('\t' + frags + '\n')
