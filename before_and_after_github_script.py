import argparse
import os
import glob

# this script will convert the notebooks to .py before pushing to github and the .py files back to
# notebooks after pulling from github

parser = argparse.ArgumentParser(description='Before Push or After Pull from GitHub')
parser.add_argument('-b', '--before_push', action="store_true", help='Convert all .ipynb to .py in converted_notebooks folder')
parser.add_argument('-a', '--after_pull', action="store_true", help='Convert all .py from converted_notebooks folder to .ipynb')

def run():

    args = parser.parse_args()
    if args.before_push:
        _top_path = os.path.dirname(__file__)
        list_notebooks = glob.glob('*.ipynb')
        list_notebooks.sort()

        print("Cleaning ...")
        for _notebook in list_notebooks:
            os.system('nbstripout {}'.format(_notebook))
            print(" > {}".format(_notebook))

        list_notebooks_after = glob.glob('*.ipynb')
        list_notebooks_after.sort()

        if len(list_notebooks) == len(list_notebooks_after):
            print(" Cleaning Result:  OK!")
        else:
            print(" Cleaning Result: WARNING!")
            for _file in list_notebooks:
                if not (_file in list_notebooks_after):
                    print(" Missing File: {}".format(_file))

        os.system('jupytext --to converted_notebooks//py *.ipynb')

    elif args.after_pull:
        os.system('jupytext --to ipynb converted_notebooks/*.py')


if __name__ == '__main__':
    run()
