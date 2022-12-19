from pathlib import Path

''' *** PATHS *** '''
# Names
data_dir_name = 'data/'
recordings_dir_name = data_dir_name + 'recordings/wav/'
csv_dir_name = data_dir_name + 'csv/'

# Directories
PROJECT_DIR = Path(__file__).parent.parent

DATA_DIR = PROJECT_DIR / data_dir_name

RECORDINGS_DIR = PROJECT_DIR / recordings_dir_name

CSV_DIR = PROJECT_DIR / csv_dir_name
