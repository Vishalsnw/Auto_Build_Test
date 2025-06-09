import os
import sys

idea = sys.argv[1]
slug = idea.lower().replace(" ", "-")

print(f"📁 Creating project for: {idea} → {slug}")

folders = [
    f"{slug}/public",
    f"{slug}/src",
]

files = {
    f"{slug}/package.json": f"""{{
  "name": "{slug}",
  "version": "0.0.1",
  "scripts": {{
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }},
  "dependencies": {{
    "react": "^18.0.0",
    "react-dom": "^18.0.0"
  }},
  "devDependencies": {{
    "vite": "^4.0.0",
    "tailwindcss": "^3.0.0",
    "postcss": "^8.0.0",
    "autoprefixer": "^10.0.0"
  }}
}}""",

    f"{slug}/vite.config.js": f"""import {{ defineConfig }} from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({{
  plugins: [react()],
}});
""",

    f"{slug}/tailwind.config.js": """module.exports = {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: { extend: {} },
  plugins: [],
};
""",

    f"{slug}/postcss.config.js": """module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
""",

    f"{slug}/index.html": f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>{idea}</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>""",

    f"{slug}/src/main.jsx": """import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);""",

    f"{slug}/src/index.css": """@tailwind base;
@tailwind components;
@tailwind utilities;
""",

    f"{slug}/src/App.jsx": f"""function App() {{
  return (
    <div className="min-h-screen flex items-center justify-center text-2xl text-center p-6">
      🚀 {idea}
    </div>
  );
}}
export default App;
""",

    f"{slug}/README.md": f"# {idea}\n\nAuto-generated React + Tailwind project. Ready to deploy on Vercel.",
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ Done! App generated in folder: {slug}")
