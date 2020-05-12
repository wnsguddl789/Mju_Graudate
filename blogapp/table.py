from jinja2 import Template
template = Template(open("./templates/calculator.html").read())
open('ouptut.html','w').write(template.render(
    header = ['a','b','c'],
    rows = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
))
