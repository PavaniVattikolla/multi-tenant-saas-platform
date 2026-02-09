const express = require("express");
const cors = require("cors");
const dotenv = require("dotenv");
const morgan = require("morgan");

dotenv.config();

const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use(morgan("dev"));

// Import Routes
const authRoutes = require("./src/routes/auth.routes");
const tenantRoutes = require("./src/routes/tenant.routes");
const userRoutes = require("./src/routes/user.routes");
const projectRoutes = require("./src/routes/project.routes");
const taskRoutes = require("./src/routes/task.routes");

// Health Check
app.get("/api/health", (req, res) => {
  res.status(200).json({ status: "UP", message: "Multi-tenant SaaS Backend is healthy" });
});

// API Routes
app.use("/api/auth", authRoutes);
app.use("/api/tenants", tenantRoutes);
app.use("/api/users", userRoutes);
app.use("/api/projects", projectRoutes);
app.use("/api/tasks", taskRoutes);

// Root Route
app.get("/", (req, res) => {
  res.send("Multi-Tenant SaaS Backend Running 🚀");
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
