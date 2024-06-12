import requests
from bs4 import BeautifulSoup

# Function to extract ids and labels of input fields
def extract_ids_and_labels(form_url):
    response = requests.get(form_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    input_fields = soup.find_all('input')
    select_fields = soup.find_all('select')
    textarea_fields = soup.find_all('textarea')
    ids_and_labels = []

    # Extracting ids and labels of input fields
    for field in input_fields + select_fields + textarea_fields:
        field_id = field.get('id')
        label = soup.find('label', {'for': field_id})
        label_text = label.text.strip() if label else ""
        ids_and_labels.append((field_id, label_text))

    return ids_and_labels


