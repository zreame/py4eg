import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('lst', lst)
print('data type:', type(lst))
print('count:', len(lst))

# .find() returns text (only one per node), .get() returns child attribute value (can be many per node)
for item in lst:
    print('Name:', item.find('name').text,'ID:', item.find('id').text)
    print('x value is:', item.get('x'))