from flask import Flask, request, jsonify, render_template
import pyotp

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# OTP generation (for example, sending via email or SMS)
@app.route('/generate-otp', methods=['GET'])
def generate_otp():
    totp = pyotp.TOTP('base32secret3232')
    otp = totp.now()
    # Send OTP to user (e.g., via email or SMS)
    # For now, we'll just print it
    print(f"Generated OTP: {otp}")
    return jsonify(success=True)

# OTP verification
@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    data = request.get_json()
    user_input_otp = data['otp']
    totp = pyotp.TOTP('base32secret3232')

    if totp.verify(user_input_otp):
        return jsonify(success=True)
    else:
        return jsonify(success=False)

if __name__ == '__main__':
    app.run(debug=True)
