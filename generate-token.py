from flask import Flask, redirect, request
import uuid
import time

app = Flask(__name__)
tokens = {}

@app.route('/generate-token')
def generate_token():
    token = str(uuid.uuid4())
    tokens[token] = time.time()  # Save the generation time
    return redirect(f'https://yourform.com/?token={token}')

@app.route('/yourform')
def your_form():
    token = request.args.get('token')
    if token in tokens and time.time() - tokens[token] < 300:  # Token is valid for 5 minutes
        # Render your form here
        return "Form Contents"
    else:
        return "Invalid or expired token", 403

if __name__ == '__main__':
    app.run()
