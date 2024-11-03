'''XML Processing using xml.sax'''

import xml.sax

class PeopleHandler(xml.sax.ContentHandler):

    # Setting the current variable to the tag name
    def startElement(self, name, attrs):
        self.current = name
        if name == 'person':
            print(f'-- Person {attrs["id"]} --')
    
    # Setting the local variable to the content which is currently read in the XML file
    def characters(self, content):
        if self.current == 'name':
            self.name = content
        elif self.current == 'age':
            self.age = content
        elif self.current == 'weight':
            self.weight = content
        elif self.current == 'height':
            self.height = content
    
    # Printing the local variables
    def endElement(self, name):
        if self.current == 'name':
            print(f'Name: {self.name}')
        elif self.current == 'age':
            print(f'Age: {self.age}')
        elif self.current == 'weight':
            print(f'Weight: {self.weight}')
        elif self.current == 'height':
            print(f'Height: {self.height}')
        
        # Reseting current variable
        self.current = ''

# Parsing the XML file
handler = PeopleHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('people.xml')