import re as regex


class FragmentAnalyzer:
    def __init__(self):
        self.fragment_list_false = []
        self.fragment_list_true = []
        self.input_list = []
        self.bands = [200, 500, 1000]
        self.concentration_threshold = 0.0
        self.tolerance = 5
        self.file_name = 'C:\\Users\\henri\\OneDrive\\Desktop\\School\\Concordia\\Genome Foundry\\FragmentAnalyzerOutput.csv'

    def print_results(self):
        print('TRUE')
        for lt in self.fragment_list_true:
            print(lt)
        print('\nFALSE')
        for lf in self.fragment_list_false:
            print(lf)

    # @staticmethod
    def get_cell_and_plasmid(self, f_line):
        split_line = f_line.split(',')
        return [split_line[0], split_line[1]]

    # @staticmethod
    def get_input_list(self, cell, plasmid, f_line):
        # split by comma delimiter then by whitespace to remove "(LM)/(UM)" from the band size
        value_list = [x.split(' ')[0] for x in f_line.split(',')]
        # return [cell, plasmid, peakId, size (bp), % conc]
        return [cell, plasmid, value_list[0], value_list[1], value_list[2]]

    def add_input_list(self, input_list):
        add_false = False
        band_size = int(input_list[3])
        concentration = float(input_list[4]) if input_list[4] else -1

        for band in self.bands:
            # see if the band size is within the correct range and above the desired concentration
            if ((band - self.tolerance) <= band_size <= (band + self.tolerance)
                    and concentration > self.concentration_threshold):
                self.fragment_list_true.append(input_list.copy())
                break
            elif not add_false:
                add_false = True

        if add_false:
            self.fragment_list_false.append(input_list.copy())

        input_list.clear()

    def process_file_data(self):
        current_cell = ''
        current_plasmid = ''
        with open(self.file_name) as f:
            for line in f:
                # check for a cell id
                # regex uses ^[A-Z]+[0-9]+ to find uppercase letters followed by digits at the beginning of the line
                if regex.search("^[A-Z]+[0-9]+", line) is not None:
                    cell_plasmid_list = self.get_cell_and_plasmid(line)
                    current_cell = cell_plasmid_list[0]
                    current_plasmid = cell_plasmid_list[1]
                # check for a peak id
                # regex uses ^[0-9]+ to find one or more digits at the beginning of the line
                elif regex.search("^[0-9]+", line) is not None:
                    self.add_input_list(self.get_input_list(current_cell, current_plasmid, line))

    def main(self):
        self.process_file_data()
        self.print_results()


if __name__ == "__main__":
    analyzer = FragmentAnalyzer()
    analyzer.main()
