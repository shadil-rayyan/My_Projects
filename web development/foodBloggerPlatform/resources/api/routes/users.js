import express from "express";
import userController from "../controllers/user.js"; // Import the user controller

const app = express();
const router = express.Router();

// Set up middleware, other routes, etc.

// Use the user controller with the "/users" prefix
app.use("/users", userController);

// Start the Express app
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
export default router;
