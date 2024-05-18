from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Button Example</title>
        <script>
            function showMessage() {
                alert("Button clicked!");
            }
        </script>
    </head>
    <body>
        <h1>Welcome to Flask</h1>
        <button onclick="showMessage()">Click Me!</button>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
