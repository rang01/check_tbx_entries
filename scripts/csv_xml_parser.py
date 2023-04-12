import csv
import xml.etree.ElementTree as ET

# Define the paths to your CSV file and XML file
csv_path = 'path/to/your/csv/file.csv'
xml_path = 'path/to/your/xml/file.xml'

# Define a function that takes a word and an Element object representing an XML <term> tag,
# and returns True if the word is found in the tag's text, and False otherwise
def word_in_term(word, term_elem):
    return word in term_elem.text

# Read the CSV file and create a list of its words
csv_words = []
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        csv_words.append(row[0])

# Parse the XML file and create a list of its <term> tags
xml_terms = []
tree = ET.parse(xml_path)
root = tree.getroot()
for term_elem in root.findall('.//term'):
    xml_terms.append(term_elem)

# Check if each word in the CSV file is found in any of the <term> tags in the XML file
for word in csv_words:
    found = False
    for term_elem in xml_terms:
        if word_in_term(word, term_elem):
            found = True
            break
    if found:
        print(f'The word "{word}" was found in the XML file.')
    else:
        print(f'The word "{word}" was not found in the XML file.')
