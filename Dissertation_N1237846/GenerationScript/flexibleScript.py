import os, os.path
# path joining version for other paths
DIR = 'c++_scripts_dataset'
print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))