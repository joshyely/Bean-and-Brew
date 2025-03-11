"""
Script for running pytest and saving the results to a csv, generating the file name based on the current date and time.
"""

import subprocess
from datetime import datetime

if __name__ == '__main__':
    name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    subprocess.run(f'pytest -q --csv ./test_results/{name}.csv --csv-columns description,test_data,expected,actual,comments', shell=True)