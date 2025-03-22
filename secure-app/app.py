from flask import Flask, request, redirect, url_for, make_response
import secrets
import bcrypt

app = Flask(__name__)

sessions = {}

# Hardcoded users with bcrypt-hashed passwords
users = {
    "alice": bcrypt.hashpw("alicepassword".encode('utf-8'), bcrypt.gensalt()),
    "admin": bcrypt.hashpw("adminpassword".encode('utf-8'), bcrypt.gensalt()),
}

# Verify a password
def verify_password(username, password):
    if username in users:
        # Compare the provided password with the stored hash
        return bcrypt.checkpw(password.encode('utf-8'), users[username])
    return False

def generate_session_id():
    """Generate a random URL-safe hash (16 bytes = 24 chars)"""
    return secrets.token_urlsafe(16)

@app.route('/')
def index():
    session_id = request.args.get('session_id')
    print(session_id)
    if session_id:
        print(session_id)
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('session_id', session_id)
        return resp
    
    if not session_id:
        session_id = request.cookies.get('session_id')
    
    # Check if session is valid
    if session_id not in sessions:
        # Generate new session hash for unauthenticated users
        session_id = generate_session_id()
        sessions[session_id] = None
        resp = redirect(url_for('login'))
        resp.set_cookie('session_id', session_id)
        return resp
    
    # Check login status
    username = sessions.get(session_id)
    if username:
        # User is logged in - redirect to view
        return redirect(url_for('view'))
    else:
        # Not logged in - redirect to login
        return redirect(url_for('login'))
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Validate username and password
        if verify_password(username, password):
            # Authentication successful
            
            # 1. Delete the old session (if it exists)
            old_session_id = request.cookies.get('session_id')
            if old_session_id in sessions:
                del sessions[old_session_id]
            
            # 2. Generate a new session ID
            new_session_id = generate_session_id()
            
            # 3. Store the new session
            sessions[new_session_id] = username
            
            # 4. Create a response and set the new cookie
            resp = redirect(url_for('view'))
            resp.set_cookie('session_id', new_session_id)
            print(sessions)
            return resp
        else:
            # Authentication failed
            error_message = "Invalid username or password"
            return f'''
                <form method="post">
                    <input type="text" name="username" placeholder="Username" required>
                    <input type="password" name="password" placeholder="Password" required>
                    <input type="submit" value="Login">
                    <p style="color: red;">{error_message}</p>
                </form>
            '''
    
    # Show login form for GET requests
    return '''
        <form method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <input type="submit" value="Login">
        </form>
    '''  
    
@app.route('/view')
def view():
    session_id = request.cookies.get('session_id')
    username = sessions.get(session_id)
    if not username:
        return redirect(url_for('login'))
    return f"Logged in as: {username}"

@app.route('/logout')
def logout():
    session_id = request.cookies.get('session_id')
    if session_id in sessions:
        # Remove the session entirely from the dictionary
        del sessions[session_id]
    # Clear the session_id cookie
    resp = redirect(url_for('index'))
    resp.delete_cookie('session_id')
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)