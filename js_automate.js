const fs = require('fs');

const ciStandard = {

	"text": "input",
	"email": "input",
	"password": "password",
	"button": "button",
	"radio": "radio",
	"submit": "submit"

}

function convertToCodeIgniter(html) {

	const pattern = /<input([^>]+)\/?>/g;
	const matches = html.match(pattern) || [];

	let result = "";

	for (const match of matches) {

		const attrs = {};
		for (const attr of match.match(/(\w+)="([^"]+)"/g) || []) {
			const [key, value] = attr.split('=');
			attrs[key] = value.slice(1, -1); // Remove quotes
		}

		const data = {...attrs};

		result += "<?php\n";
		result += "$data = array(\n";
		for (const [key, value] of Object.entries(data)) {
			result += `    '${key}' => '${value}',\n`;
		}
		result += ");\n";
		result += `echo form_${ciStandard[attrs["type"]]}($data);\n`;
		result += "?>\n";
	}

	return result;
}

// Read the input file line by line
const inputFile = 'index.html';
const inputLines = fs.readFileSync(inputFile, 'utf-8').split('\n');

for (const line of inputLines) {
	// Check if the line contains any input tags
	if (line.includes('<input ')) {
		// Convert the input tag to the CodeIgniter standard
		const outputCode = convertToCodeIgniter(line);

		// Print both the original line and the generated PHP code
		// console.log(line);
		console.log(outputCode);
	} else {
		// Print the current line
		console.log(line);
	}
}

