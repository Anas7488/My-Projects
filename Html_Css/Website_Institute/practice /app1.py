from flask import Flask, request, jsonify, render_template, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session and flash to work

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if username:
            session['username'] = username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Please enter a username.', 'error')
    return render_template('login.html')

# Profile route (only accessible if logged in)
@app.route('/profile')
def profile():
    if 'username' not in session:
        flash('You must be logged in first.', 'warning')
        return redirect(url_for('login'))
    return render_template('profile.html', username=session['username'])

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('index'))

# JSON API endpoint
@app.route('/api/data')
def api_data():
    return jsonify({'message': 'Hello from Flask!', 'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
