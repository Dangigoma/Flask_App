from flask import Flask
from datetime import datetime

app = Flask (__name__)
@app.route('/')
def home():
    current_time = datetime.now().strftime("%H:%M:%S")
    return f'<h1>Hello, Developer all! </h1><p>The current time is {current_time}.</p>'

if __name__ =='__main__':
    app.run(debug=True)









