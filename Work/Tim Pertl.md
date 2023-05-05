# Tim Pertl

# E-Lad-O-Mat

[https://github.com/AlphaSoundZ/webserver/](https://github.com/AlphaSoundZ/webserver/)

[E-Lad-O-Mat | Fragebogen](https://alphasoundz.github.io/webserver/)

## Stunden

20.01.23: 3 h

21.01.23: 1.5 h

22.01.23: 4.5 h

23.01.23: 6.5 h

25.01.23: 4 h

26.01.23: 1.5 h

27.01.23: 3 h

28.01.23: 2 h

29.01.23: 5 h

01.02.23: 3 h

03.02.23: 0.5 h

04.02.23: 4 h

Insgesamt: 38.5 h

Basispreis: 450 €

474 €

 

Limit: 350€

[E-Lad-O-Mat](Tim%20Pertl/E-Lad-O-Mat.md)

[Untitled](Tim%20Pertl/Untitled%20Database.md)

---

# Database Structure

## Recommendations

### Basics

```json
{
	"title": ""
}
```

### Paragraphs

```json
{
	"paragraphs": [
		{
			"type": "" // options: text, hint
			"text": [
				{
					"type": "", // options: var, string, array
					"id": "" // options: id (var), string (string), alias (array)
				}
			]
		}
	]
}
```

One paragraph is one row.

### Criteria

```json
{
	"criterias": [ // or operator
		[ // and operator
			{
				"id": "",
				"operator": "" // option: ==, !=
			},
			{
				"id": "",
				"operator": ""
			}
		]
	]
}
```

Criteria can be either placed at the top of the hierarchy or in a paragraph.

### Table

```json
{
	"table": [
		[ // rows
			[ // row
				{ // column
					"type": "", // options: var, string
					"id": "" // options: id (var), string (string)
				}
			],
			"horizontal_line" // creates a horizontal line
		]
	]
	
}
```

### Text Types

var:

```json
{
	"text": [
		"type": "var",
		"id": ""
]
```

string

```json
{
	"text": [
		"type": "string",
		"string": ""
]
```

array

```json
{
	"text": [
		"type": "var",
		"alias": [], // iterate through answers and give them custom values
		"separator": "", // ", " e.g. (only when multiAnswer is true)
		"question": "" // id
		"
]
```

Use array if you want to assign for each answer of one question a value. For expample if you choose answer n, the text is not the string of the answer but the value of the nth el in the array.

calc

```json
{
  "text": [
		"type": "calc",
	    "values": [
	        {
	            "id": ["", ""]
	        },
	        {
	            "value": ""
	        }
	    ],
	    "operator": "*"
		]
}
```

## Recommendations Checklist

- [x]  Daten der Parkbauten
- [x]  Empfehlung 1
- [ ]  Empfehlung 2
- [x]  Empfehlung 3
- [x]  Empfehlung 4 (es fehlt noch “Benötigter Netzanschluss”, “Finanzierung”)
- [x]  Empfehlung 5 (es fehlt noch “Benötigte Fläche” (einfache Rechnung))
- [x]  Empfehlung 6