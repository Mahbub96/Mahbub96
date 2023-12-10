import re


def convert_to_codeigniter(html):
    pattern = r'<input([^>]+)/?>'
    matches = re.findall(pattern, html)
    
    result = ""
    
    for match in matches:
        attrs = {}
        for attr in re.findall(r'(\w+)="([^"]+)"', match):
            attrs[attr[0]] = attr[1]
        data = {}
        for key, value in attrs.items():
            data[key] = value
        
        result += "<?php\n"
        result += "$data = array(\n"
        for key, value in data.items():
            result += f"    '{key}' => '{value}',\n"
        result += ");\n"
        result += "echo form_input($data);\n"
        result += "?>\n"
    
    return result

# Read the input file line by line
with open('index.html', 'r') as f:
    for line in f:
        # Check if the line contains any input tags
        if '<input ' in line:
            # Convert the input tag to the CodeIgniter standard
            output_code = convert_to_codeigniter(line)
            
            # Print both the original line and the generated PHP code
            # print(line, end='')
            print(output_code)
        else:
            # Print the current line
            print(line, end='')

