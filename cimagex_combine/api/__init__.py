from cimagex import ParseCombined
from cimagex import PeptideDataset as Dataset
from cimagex import make_isotop_dataset as make_dataset
import pathlib
import requests
import re
from bs4 import BeautifulSoup


DATA_INPUT_PATH = pathlib.Path('data/input')
DATA_OUTPUT_PATH = pathlib.Path('data/output')


def combine():
    url = 'http://bfclabcomp4.scripps.edu/~radus/050714_insitu/rs004/combined_dta.txt'
    get_dataset_path(url)

    return 'hello'


def get_dataset_path(info):
    dataset_url = info

    combined_dta_path = DATA_INPUT_PATH.joinpath(info)
    annotated_path = combined_dta_path.with_suffix('.annotated')
    dta_select_path = combined_dta_path.with_suffix('.dtaselect')

    if not combined_dta_path.exists():
        combined_dta_url = dataset_url + '/combined_dta_HL.txt'
        annotated_url = combined_dta_url + '.annotated'
        dta_select_url = get_dta_select_url(dataset_url)

        with combined_dta_path.open('w') as f:
            data = requests.get(combined_dta_url).text
            f.write(data)

        with annotated_path.open('w') as f:
            data = requests.get(annotated_url).text
            f.write(data)

        with dta_select_path.open('w') as f:
            data = requests.get(dta_select_url).text
            f.write(data)

    return (combined_dta_path, annotated_path, dta_select_path)


def get_dta_select_url(dataset_url):
    dta_folder_url = dataset_url + '/dta_HL/'

    res = requests.get(dta_folder_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    dta_select_link = soup.find_all('a', string=re.compile('DTASelect'))[0].attrs['href']

    return dta_folder_url + dta_select_link