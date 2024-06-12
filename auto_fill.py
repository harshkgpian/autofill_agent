from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def fill(data,link):
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    # Open the webpage
    driver.get(link)

    # Function to fill input fields
    def fill_input_field(field_id, value):
        input_element = driver.find_element(By.ID, field_id)
        input_element.clear()
        input_element.send_keys(value)

    # Mapping between labels and IDs
    label_to_id = {
        'First Name': 'first_11',
        'Middle Name': 'middle_11',
        'Last Name': 'last_11',
        'Street Address': 'input_16_addr_line1',
        'Street Address Line 2': 'input_16_addr_line2',
        'City': 'input_16_city',
        'State / Province': 'input_16_state',
        'Email Address': 'input_12',
        'Phone Number': 'input_13_full',
        'LinkedIn': 'input_19',
        # 'Write something interesting about AI Agents/ LLMs': 'input_24',
        # 'Write something interesting about Web Automation': 'input_25',
        # 'Reverse a LinkedList': 'input_23',
        # 'Upload Your Resume': 'input_17',
        # 'Cover Letter': 'input_22'
    }

    # Fill each input field
    for label, value in data.items():
        time.sleep(0.5)  # Adjust the waiting time as needed

        field_id = label_to_id.get(label)
        if field_id:
            fill_input_field(field_id, value)
        else:
            print(f"No ID found for label: {label}")
    # time.sleep(10)  # Adjust the waiting time as needed


    