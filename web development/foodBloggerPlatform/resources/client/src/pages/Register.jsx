// Importing necessary dependencies
import React from "react";
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";

// Functional component definition for the Register page
const Register = () => {
  // State to manage form inputs (username, email, and password)
  const [inputs, setInputs] = useState({
    username: "",
    email: "",
    password: "",
  });

  // State to manage error messages
  const [err, setError] = useState(null);

  // Accessing the navigation functionality from React Router
  const navigate = useNavigate();

  // Event handler for input changes
  const handleChange = (e) => {
    // Updating the inputs state with the new values
    setInputs((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  // Event handler for form submission
  const handleSubmit = async (e) => {
    // Preventing the default form submission behavior
    e.preventDefault();
    try {
      // Making a POST request to the server to register a new user
      await axios.post("/auth/register", inputs);
      // Navigating to the login page upon successful registration
      navigate("/login");
    } catch (err) {
      // Handling and setting an error message if registration fails
      setError(err.response.data);
    }
  };

  // Rendering the JSX structure for the Register component
  return (
    <div className="auth">
      <h1>Register</h1>
      <form>
        {/* Input field for the username */}
        <input
          required
          type="text"
          placeholder="username"
          name="username"
          onChange={handleChange}
        />
        {/* Input field for the email */}
        <input
          required
          type="email"
          placeholder="email"
          name="email"
          onChange={handleChange}
        />
        {/* Input field for the password */}
        <input
          required
          type="password"
          placeholder="password"
          name="password"
          onChange={handleChange}
        />
        {/* Button for submitting the form */}
        <button onClick={handleSubmit}>Register</button>
        {/* Displaying an error message if there's an error */}
        {err && <p>{err}</p>}
        {/* Link to the login page */}
        <span>
          Do you have an account? <Link to="/login">Login</Link>
        </span>
      </form>
    </div>
  );
};

// Exporting the Register component as the default export
export default Register;
