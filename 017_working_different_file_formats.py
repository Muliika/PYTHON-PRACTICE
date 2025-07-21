# Working with different file formats like CSV(Comma-Separated Values), JSON (JavaScript Object Notation), and XML (eXtensible Markup Language) is essential in data processing and web development. Python provides built-in libraries and third-party packages to handle these formats efficiently.

# Reading csv files:
import csv

# Open a CSV file and read its contents
with open("data.csv", mode="r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)  # Each row is a list of values
# Writing to a CSV file
with open("output.csv", mode="w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Name", "Age", "City"])  # Writing header
    csv_writer.writerow(["Alice", 30, "New York"])
    csv_writer.writerow(["Bob", 25, "Los Angeles"])
# Reading JSON files:
import json

# Open a JSON file and read its contents
with open("data.json", mode="r") as file:
    json_data = json.load(file)
    print(json_data)  # Each key-value pair is a dictionary
# Writing to a JSON file
with open("output.json", mode="w") as file:
    json.dump({"Name": "Alice", "Age": 30, "City": "New York"}, file, indent=4)
# Reading XML files:
import xml.etree.ElementTree as ET

# Open an XML file and read its contents
tree = ET.parse("data.xml")
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)  # Each child is an element with a tag and attributes
# Writing to an XML file
root = ET.Element("data")
child1 = ET.SubElement(root, "person")
child1.set("name", "Alice")
child1.set("age", "30")
child2 = ET.SubElement(root, "person")
child2.set("name", "Bob")
child2.set("age", "25")
tree = ET.ElementTree(root)
tree.write("output.xml", encoding="utf-8", xml_declaration=True)
# This code demonstrates how to read and write different file formats in Python, which is crucial for data manipulation and storage in various applications.
