import re


def convert_to_codeigniter(html):
    pattern = r'<input([^>]+)/?>'
    matches = re.findall(pattern, html)
    for match in matches:
        attrs = {}
        for attr in re.findall(r'(\w+)="([^"]+)"', match):
            attrs[attr[0]] = attr[1]
        data = {}
        for key, value in attrs.items():
            data[key] = value
        print("<?php")
        print("$data = array(")
        for key, value in data.items():
            print(f"    '{key}' => '{value}',")
        print(");")
        print("echo form_input($data);")
        print("?>")

contents = ""
#  # Check if the input file contains any input tags
#  with open('index.html', 'r') as f:
#      contents = f.read()
#  if '<input ' in contents:
#      convert_to_codeigniter(contents)
#  else:
#      print(contents)
#

# Read the input file line by line
with open('index.html', 'r') as f:
    for line in f:
        # Check if the line contains any input tags
        if '<input ' in line:
            # Convert the input tag to the CodeIgniter standard
            output_line = convert_to_codeigniter(line)
            print(output_line)
        else:
            # Print the current line
            print(line, end='')
