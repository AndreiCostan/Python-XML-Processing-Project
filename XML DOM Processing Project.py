'''XML Processing using xml.dom'''

import xml.dom.minidom
import re

# Creating a domtree from the XML file
domtree = xml.dom.minidom.parse('people.xml')

# Getting the root element
group = domtree.documentElement

# Getting all the elements that have tag name: person
people = group.getElementsByTagName('person')

# Iterating and processing the people collection of person elements
for person in people:
    print(f'-- Person {person.getAttribute("id")} --')

    # Getting element values in the person node
    name = person.getElementsByTagName('name')[0].childNodes[0].nodeValue
    age = person.getElementsByTagName('age')[0].childNodes[0].nodeValue
    weight = person.getElementsByTagName('weight')[0].childNodes[0].nodeValue
    height = person.getElementsByTagName('height')[0].childNodes[0].nodeValue
    
    # Printing elements in the person node
    print(f'Name: {name}')
    print(f'Age: {age}')
    print(f'Weight: {weight}')
    print(f'Height: {height}')


# Manipulating values in the XML file
people[0].getElementsByTagName('name')[0].childNodes[0].nodeValue = 'Peter Warm'
people[0].setAttribute('id', '200')
people[0].setAttribute('newattr', 'Male')


# Adding new node with elements
# Creating new person
new_person = domtree.createElement('person')
new_person.setAttribute('id', '89')

# Creating elements for the new node
name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('Jon Doe'))

age = domtree.createElement('age')
age.appendChild(domtree.createTextNode('26'))

weight = domtree.createElement('weight')
weight.appendChild(domtree.createTextNode('79'))

height = domtree.createElement('height')
height.appendChild(domtree.createTextNode('191'))

# Appending elements to the new_person node
new_person.appendChild(name)
new_person.appendChild(age)
new_person.appendChild(weight)
new_person.appendChild(height)

# Appending new_person node to the root element
group.appendChild(new_person)


# Writing changes to xml (with identation for changes but with spaces for the rest of the file)
with open('people_modified.xml', 'w') as f:
    f.write(domtree.toprettyxml())
# Quick workaround is to replace text in file with regex: ^(\s+|)$\n and replace with blank: ''


# Writing changes to xml (No identation)

# domtree.writexml(open('people_modified.xml', 'w'))
