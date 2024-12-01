import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV file
file_path = './data-set/sick-absences/sick-absences-rate-by-sex.csv'  
data = pd.read_csv(file_path, skiprows=3)  


data.columns = data.columns.str.replace('\n', ' ').str.strip()

data = data.dropna(axis=1, how='all')  
data = data.dropna(axis=0, how='all')  
data = data.replace(',,', None)  
data.dropna(inplace=True)  


data['Year'] = data['Year'].astype(str).str.extract('(\d+)').astype(int)

print(repr(data.columns))


men_col = [col for col in data.columns if 'men' in col.lower()][0]
women_col = [col for col in data.columns if 'women' in col.lower()][0]




plt.figure(figsize=(10, 5))
plt.plot(data['Year'], data[men_col], marker='o', label='Men')
plt.title('Sickness Absence Rate (Men)')
plt.xlabel('Year')
plt.ylabel('Sickness Absence Rate (%)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(data['Year'], data[women_col], marker='o', color='orange', label='Women')
plt.title('Sickness Absence Rate (Women)')
plt.xlabel('Year')
plt.ylabel('Sickness Absence Rate (%)')
plt.grid(True)
plt.show()
