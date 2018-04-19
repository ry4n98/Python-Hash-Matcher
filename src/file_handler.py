from os import listdir
from os.path import isfile, join
from progress.bar import Bar

values_directory_path = "/Users/rsm30/home/bruteforce-database/"
# values_directory_path = "/Users/rsm30/home/_values/"
# values_directory_path = "/Users/rsm30/home/test/"

def load_files():
    files = [f for f in listdir(values_directory_path) if isfile(join(values_directory_path, f))]
    scannable_files = []
    for f in files:
        if ".txt" in f:
            scannable_files.append(f)
    return scannable_files

def get_file_contents():
    target_files = load_files()
    print("-- Loaded the following files --\n")
    for target_file in target_files:
        print(" - {}".format(target_file))

    print("")
    bar = Bar('Scanning files', max=len(target_files))
    values = []
    for target_file in target_files:
        f = open('{}{}'.format(values_directory_path,target_file),'r')
        for line in f:
            for value in line.split():
                values.append(value.strip())
        bar.next()
    bar.finish()
    return values
