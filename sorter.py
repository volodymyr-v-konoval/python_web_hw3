import argparse
import sys
from multiprocessing import Process
from pathlib import Path
from shutil import copyfile


parser = argparse.ArgumentParser(description="Starting the job!")
parser.add_argument("source", help='Source folder.')
parser.add_argument("--output", help='Output folder.', default="dist")


args = vars(parser.parse_args())
source = Path(args.get('source'))
output = Path(args.get('output'))


def folder_reader(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            inner_process = Process(target=folder_reader, args=(el,))
            inner_process.start()
        else:
            copy_file(el)


def copy_file(path: Path) -> None:
    ext = path.suffix[1:]
    ext_folder = output / ext
    try:
        ext_folder.mkdir(exist_ok=True, parents=True)
        copyfile(path, ext_folder / path.name)
    except OSError:
        sys.exit(1)

if __name__ == '__main__':
    pr = Process(target=folder_reader, args=(source,))
    pr.start()
    pr.join()
    print("Copy and sort processes are finished.")
