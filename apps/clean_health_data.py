
import pandas as pd

def load_and_clean_data(file_path):
    health_data = pd.read_csv(file_path, skiprows=2)
    health_data.columns = health_data.columns.str.replace('\n', ' ').str.strip()
    health_data = health_data.dropna(axis=1, how='all').dropna(axis=0, how='all')
    health_data = health_data.replace(',', '', regex=True).astype(float, errors='ignore')
    health_data.rename(columns={'Unnamed: 0': 'Year Of Occurrence'}, inplace=True)
    health_data.iloc[:, 1:] = health_data.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
    health_data['Total'] = health_data.iloc[:, 1:].sum(axis=1)

    # Remove rows with invalid 'Year Of Occurrence'
    health_data = health_data.dropna(subset=['Year Of Occurrence'])
    health_data = health_data[health_data['Year Of Occurrence'] != 'Year of occurrence']

    return health_data


men_file_path = './data-set/sick-absences/Number-of-days-lost-through-sick-absences.csv'
women_file_path = './data-set/sick-absences/Women-number-of-days-lost-through-sick-absences.csv'


