from pathlib import Path

def main():
    # Set the data folder
    data_folder = 'data'

    p = Path(data_folder)

    # List all files in the data folder
    file_list = list(p.glob('*.fa'))

    for file in file_list:
        histogram = {}
    
        with open(file, 'r') as input_file:
            for line in input_file.readlines():
                if not line.startswith('>'):
                    stripped_line = line.strip()
                    for char in stripped_line:
                        if not char in histogram:
                            histogram[char] = 0
                        histogram[char] += 1

        print(file)
        print(histogram)

main()