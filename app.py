from flask import Flask, render_template_string, request, Response
import re
import os

app = Flask(__name__)

html = '''<!DOCTYPE html>
<html>
<head>
    <title>Silly Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
			text-align: center;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            flex-direction: column;
			background-color: lightblue; /* Глупый цвет фона */
        }
        h1 {
            font-size: 5em;
        }
        input {
            width: 200px;
            height: 30px;
            font-size: 1.5em;
        }
    </style>
</head>
<body>

<h1>Silly Calculator</h1>
<div>
    <form method="GET">
		<input style="width:10em;margin:.5em" type="text" name="statement">
		<input value="=" style="width: 2em; margin:.5em" type="submit">
	</form>
	<h2>%s</h2>
</div>

</body>
</html>'''

@app.route("/", methods=['GET'])
def hello_world():
    statement = request.args.get('statement')
    if statement:
        if re.match(r'.*?([sS][yY][sS][tT][eE][mM]|[sS][hH]|[rR][mM]|[eE][xX][eE][cC]|__).*?', statement): 
            answer = 'invalid input'
            debug = 'Input Filtered'
            resp = Response(html % answer)
            resp.headers["Debug"] = debug
            return resp 
        elif not re.match(r'(^(-\d|\d).*\d$|^\d$)', statement): 
            answer = 'invalid input'
            debug = '!~(^(-\d|\d).*\d$|^\d$)'
            resp = Response(html % answer)
            resp.headers["Debug"] = debug
            return resp 
        else:
            try:
                answer = eval(statement)
                answer = float(answer)
                resp = Response(html % answer)
                resp.headers["Debug"] = answer
                return resp
            except Exception as e:
                answer = 'invalid input'
                debug = e
                resp = Response(html % answer)
                resp.headers["Debug"] = debug
                return resp
    else:
        resp = Response(html % '')
        return resp 

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
