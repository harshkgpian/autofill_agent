from Extract_info_from_web import extract_ids_and_labels
from auto_fill import fill
from PyPDF2 import PdfReader


form_link = "https://form.jotform.com/241617189501153"

print("\n\nExtracting Input Ids from the form link using Beautiful Soup.......\n\n")


# Call the function with the provided form link
ids_and_labels = extract_ids_and_labels(form_link)

# Reading the CV.pdf
file_path = r"C:\Users\harsh\Desktop\GEN AI\Intern/CV.pdf"

print("Reading CV.PDF.......\n\n")

with open(file_path, "rb") as file:
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

print("Calling Ai Agent to extract the values for input fields.......\n\n")

# Call the ai agent to extract required values for the labels extracted from the extract_id_and_labels
from extract_from_pdf import extract_function_values

data1 = extract_function_values(text)

print("Data Extracted Successfully: \n\n")

print("\n\nAuto Filling.......\n\n")

# Call auto_fill which uses selenium to auto fill the extracted data into the form
fill(data1, form_link)
