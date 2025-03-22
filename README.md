# flask-session-fixation-demo
A Flask app demonstrating session fixation vulnerability and its secure counterpart. This project highlights the risks of session fixation and how to prevent it.
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
git clone https://github.com/Alir3zaRaisi/flask-session-fixation-demo/
```
2.Navigate to the project directory:
```bash
cd flask-session-fixation-demo
```
3.Build and run the containers:
```bash
docker-compose up --build
```
