import re

fragment_list_true = []
fragment_list_false = []
val_list = []
lower = 100
upper = 500
concentration = 50.0
tolerance = 0.0
f_name = 'C:\\Users\\henri\\OneDrive\\Desktop\\School\\Concordia\\Genome Foundry\\FragmentAnalyzerOutput.csv'

with open(f_name) as f:
    for line in f:
        # check for a cell id
        if re.search("^[A-Z][0-9]+", line) is not None:
            split_line = line.split(',')
            cell = split_line[0]
            plasmid = split_line[1]
            split_line.clear()
        # check for a peak id
        elif re.search("^[0-9]+", line) is not None:
            val_list = [x.split(' ')[0] for x in line.split(',')]
            # [cell name, plasmid, peakId, size (bp), % conc]
            if lower <= int(val_list[1]) <= upper and float(val_list[2]) > concentration:
                fragment_list_true.append([cell, plasmid, val_list[0], val_list[1], val_list[2]])
            else:
                fragment_list_false.append([cell, plasmid, val_list[0], val_list[1], val_list[2]])
            val_list.clear()

print('TRUE')
for lt in fragment_list_true:
    print(lt)
print('\nFALSE')
for lf in fragment_list_false:
    print(lf)
