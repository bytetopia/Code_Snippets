

DIR_NAME = './'

# 1) get all files in the directory
all_files = [name for name in os.listdir(DIR_NAME) if os.path.isfile(os.path.join(DIR_NAME, name))]

# 2) if you want to filter files with specific suffix
type_files = [name for name in all_files if name.endswith('.pdf')]
