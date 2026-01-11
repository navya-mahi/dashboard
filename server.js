import express from "express";
import path from "path";

const app = express();
const __dirname = path.resolve();

app.use("/dashboard", express.static(path.join(__dirname, "dist")));

app.get("/dashboard/*", (_, res) => {
  res.sendFile(path.join(__dirname, "dist", "index.html"));
});

const port = process.env.PORT || 8080;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
