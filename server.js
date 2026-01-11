import express from "express";
import path from "path";

const app = express();
const __dirname = path.resolve();

// Serve index.html for exact /dashboard (no trailing slash) - no auth required
app.get("/dashboard", (_, res) => {
  res.sendFile(path.join(__dirname, "dist", "index.html"));
});

// Serve static files from /dashboard/
app.use("/dashboard", express.static(path.join(__dirname, "dist")));

// Serve index.html for any sub-paths of /dashboard (SPA routing) - no auth required
app.get("/dashboard/*", (_, res) => {
  res.sendFile(path.join(__dirname, "dist", "index.html"));
});

const port = process.env.PORT || 8080;
app.listen(port, () => {
  console.log(`\n🚀 Server running!`);
  console.log(`\n📊 Dashboard: http://localhost:${port}/dashboard\n`);
});
