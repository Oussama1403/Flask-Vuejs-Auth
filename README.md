<h1 align="center">
Flask-Vue.js Authentication App
</h1>

<p align="center">
  <img src="Logos/vuejs-icon.svg" alt="Vue.js Logo" style="width: 20%;"/>
  <img src="Logos/flask-icon.svg" alt="Flask Logo" style="width: 20%;"/>
  <img src="Logos/mongodb-icon.svg" alt="MongoDB Logo" style="width: 20%;"/>
</p>

This project demonstrates a simple user authentication system using Flask as the backend and Vue.js as the frontend. It provides a basic template for setting up a Flask API with JWT-based authentication and a Vue.js Single Page Application (SPA) that interacts with the API.

## Project Structure

The project is organized into two main folders:

- **Backend**: Contains the Python code for the Flask backend.
- **Frontend**: Contains the JavaScript code for the Vue.js frontend.

## Libraries and Tools Used

### Backend (Python)
- **Flask**: A micro web framework used for creating the backend API.
- **Flask-Cors**: A Flask extension for handling Cross-Origin Resource Sharing (CORS), allowing the frontend to communicate with the backend.
- **Flask-PyMongo**: A Flask extension for interacting with MongoDB.
- **Flask-JWT-Extended**: A Flask extension for creating and verifying JSON Web Tokens (JWT) for secure API authentication.

### Frontend (JavaScript)
- **Vue.js**: A progressive JavaScript framework for building user interfaces.
- **vee-validate**: A validation library for Vue.js that allows you to validate inputs in a declarative way.
- **@vee-validate/rules**: Additional validation rules for `vee-validate`.
- **axios**: A promise-based HTTP client for making requests to the backend API.
- **bootstrap**: A CSS framework for creating responsive layouts and styling the application.
- **jwt-decode**: A library for decoding JWT tokens on the client-side.

### Development Tools
- **Prettier**: A code formatter to ensure consistent code style across the project.

## Getting Started

### Prerequisites
1.  **Install Python:** Ensure Python is installed on your machine.
2. **Install Node.js and npm:** Ensure Node.js and npm are installed.
3. **Install MongoDB:** Make sure MongoDB is installed and running on your local machine.

### Backend Setup

1. **Navigate to the backend directory:**

   ```bash
   cd Backend
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**

   ```bash
    python app.py
   ```

   The backend will be available at `http://localhost:5000`.

### Frontend Setup

1. **Navigate to the frontend directory:**

   ```bash
   cd Frontend
   ```

2. **Install the required packages:**

   ```bash
   npm install
   ```

3. **Start the development server:**

   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:5173/`.

### Database Setup
- **The MongoDB service** is started upon successful installation, By default, MongoDB will run on mongodb://localhost:27017.
- You can use **MongoDB Compass**, a user-friendly GUI for creating and managing databases.

### Formatting Code

To format the code across the project using Prettier, run:

```bash
npx prettier --write .
```
## Usage

- **Login**: Enter your credentials to log in and receive a JWT token.
- **Signup**: Create a new account to access protected routes.
- **Protected Routes**: Once logged in, the frontend will use the JWT token stored in `localStorage` to access protected routes.

## Important Notes

- This project is intended for educational purposes and should not be used in production without implementing additional security measures.
- Always ensure sensitive data, such as JWT tokens, is handled securely both on the client and server sides.

## Contributing

Feel free to fork this repository, open issues, or submit pull requests to contribute to the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

