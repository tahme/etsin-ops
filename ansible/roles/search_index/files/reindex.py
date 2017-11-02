import sys

from search_index.reindexer import reindex_all_without_emptying_index
from search_index.reindexer import reindex_all_by_emptying_index
from reindexing_log import get_logger

log = get_logger(__name__)

def main():
    NO = 'no'
    YES = 'yes'
    RECREATE_INDEX = "recreate_index"

    instructions = """\nRun the program as etsin-user with pyenv activated using 'python reindex.py recreate_index=X where X = yes or X = no"""

    run_args = dict([arg.split('=', maxsplit=1) for arg in sys.argv[1:]])

    if not RECREATE_INDEX in run_args:
        print(instructions)
        log.error(instructions)
        sys.exit(1)

    if run_args[RECREATE_INDEX] not in [NO, YES]:
        print(instructions)
        log.error(instructions)
        sys.exit(1)

    if run_args[RECREATE_INDEX] == NO:
        reindex_all_without_emptying_index()

    if run_args[RECREATE_INDEX] == YES:
        reindex_all_by_emptying_index()


if __name__ == '__main__':
    # calling main function
    main()
