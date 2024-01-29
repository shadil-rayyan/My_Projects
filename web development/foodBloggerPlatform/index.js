// Import necessary modules and dependencies
import express from "express";          // Import the Express framework
import authRoutes from "./routes/auth.js";   // Import authentication routes
import userRoutes from "./routes/users.js";  // Import user routes
import postRoutes from "./routes/posts.js";  // Import post routes
import cookieParser from "cookie-parser";   // Import cookie-parser for handling cookies
import multer from "multer";                // Import multer for handling file uploads

// Create an instance of the Express application
const app = express();

// Middleware to parse JSON data in requests
app.use(express.json());

// Middleware to parse cookies in requests
app.use(cookieParser());

// Configure multer for handling file uploads
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, "../client/public/upload");  // Set the destination folder for uploaded files
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + file.originalname);  // Set the filename for the uploaded file
  },
});

const upload = multer({ storage });

// Endpoint for handling file uploads
app.post("/api/upload", upload.single("file"), function (req, res) {
  const file = req.file;
  res.status(200).json(file.filename);  // Send a JSON response with the uploaded filename
});

// Define route handlers for authentication, user, and post routes
app.use("/api/auth", authRoutes);
app.use("/api/users", userRoutes);
app.use("/api/posts", postRoutes);

// Start the Express server on port 8800
app.listen(8800, () => {
  console.log("Connected!");  // Log a message when the server is successfully connected and running
});
