// authRouter.js

import { register, login, logout } from "../controllers/auth.js";
import express from "express";

const authRouter = express.Router();

// User registration
authRouter.post("/register", register);

// User login
authRouter.post("/login", login);

// User logout
authRouter.post("/logout", logout);

export default authRouter;
