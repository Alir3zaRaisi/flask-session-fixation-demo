# Flask Session Fixation Demo

This project demonstrates **session fixation vulnerability** in Flask and its secure counterpart. It illustrates how attackers can exploit session fixation and how to prevent it.

## Features

- **Vulnerable App**:
  - Demonstrates session fixation vulnerability.
  - Allows session IDs to be set by the client.

- **Secure App**:
  - Prevents session fixation by regenerating session IDs after login.
  - Uses bcrypt for secure password hashing.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask-session-fixation-demo.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd flask-session-fixation-demo
   ```
   
3. Build and run the containers:
   ```bash
   docker-compose up --build
   ```
   
4. Access the apps:
   - **Secure App**: [http://localhost:5001](http://localhost:5001)
   - **Vulnerable App**: [http://localhost:5002](http://localhost:5002)

## Usage

### Vulnerable App

#### Login Credentials:
- Username: `alice`, Password: `alicepassword`
- Username: `admin`, Password: `adminpassword`

#### Session Fixation Attack:

1. **Attacker Sets a Session ID:**
   - The attacker sends a link to the victim with a predefined session ID:
     ```
     http://localhost:5002/?session_id=attacker_session_id
     ```
   - When the victim clicks the link, the browser sets the session ID cookie to `attacker_session_id`.

2. **Victim Logs In:**
   - The victim logs in using their credentials.
   - The app associates the victim's account with the attacker's session ID (`attacker_session_id`).

3. **Attacker Hijacks the Session:**
   - The attacker uses the same session ID (`attacker_session_id`) to access the victim's account.

### Secure App

#### Login:
- Uses the same credentials as the vulnerable app.

#### Prevention Measures:
- Regenerates session IDs after login to prevent session fixation.

## Project Structure
```
flask-session-fixation-demo/
├── secure-app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
├── vulnerable-app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
├── docker-compose.yml
├── README.md
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.
