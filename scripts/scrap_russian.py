import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://masterrussian.com/fr/most_common_words_2_fr.htm"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

#Find the table containing the data
table = soup.find('table', class_='topwords')

#Extract the data rows
rows = table.find_all('tr')[1:]  # Skip the header row

data = []
for row in rows:
    columns = row.find_all('td')
    
    # Extract Russian word, French translation and word type, handling potential errors
    try:
        russian_word = columns[1].text.strip()
        french_translation = columns[2].text.strip()
        word_type = columns[3].text.strip()
        data.append([russian_word, french_translation, word_type])
    except IndexError:
        print(f"Skipping row: {row}")

# Create a Pandas DataFrame
df = pd.DataFrame(data, columns=['Russian Word', 'French Translation', 'Word Type'])

print(df)