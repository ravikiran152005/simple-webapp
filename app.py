from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Welcome</title>
            <style>
                body {
                    margin: 0;
                    height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    background-color: #f8f9fa;
                    font-family: Arial, sans-serif;
                }
                .container {
                    text-align: center;
                    background: white;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
                }
                h1 {
                    color: #007bff;
                }
                p {
                    font-size: 18px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello from Ravi Kiran!</h1>
                <p>This is a simple Flask app running inside Docker.</p>
            </div>
        </body>
        </html>
    """

@app.route("/howareyou")
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
