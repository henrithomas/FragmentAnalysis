import re
FragmentList = []
valList = []
lower = 100
upper = 200
with open(r'C:\Users\mt200\OneDrive\Desktop\School\Concordia\Genome Foundry\FragmentAnalyzerOutput.csv') as f:
    for line in f:
        # check for a cell id
        if re.search("^[A-Z][0-9]+", line) is not None:
            if valList:
                FragmentList.append(valList.copy())
                # print(valList)
            valList.clear()
            valList = [line.split(',')[0]]
        # check for a peak id and grab size value
        elif re.search("^[0-9]+", line) is not None:
            val = int(line.split(',')[1].split(' ')[0])
            valList.append(val)
    FragmentList.append(valList.copy())

for lst in FragmentList:
    frags = ', '.join(['peak ' + str(i + 1) + ': ' + str(x)
                       for i, x in enumerate(lst[1:]) if lower <= x <= upper])
    if frags:
        cell_name = lst[0]
        print(cell_name)
        print('\t' + frags + '\n')
