from pathlib import Path
import time

directory = 'F:\RUBoosted\\new_matches'
pathlist = Path(directory).glob('**/*.txt')

for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    print(path_in_str)

    with open(path_in_str, mode="r") as f:
        print(f.read())
        time.sleep(10)
