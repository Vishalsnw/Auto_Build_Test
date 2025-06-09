import os

IDEA = "AI-based diet tracker app"
SLUG = IDEA.lower().replace(" ", "-")

print(f"\n🚀 Generating project: {SLUG}\n")

folders = [
    f"{SLUG}/public",
    f"{SLUG}/src/components",
    f"{SLUG}/src/layout",
    f"{SLUG}/src/pages",
    f"{SLUG}/src/lib"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

files = {
    f"{SLUG}/package.json": f"""{{
  "name": "{SLUG}",
  "version": "1.0.0",
  "scripts": {{
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }},
  "dependencies": {{
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  }},
  "devDependencies": {{
    "vite": "^4.4.9",
    "tailwindcss": "^3.4.1",
    "postcss": "^8.4.21",
    "autoprefixer": "^10.4.14"
  }}
}}""",

    f"{SLUG}/vite.config.js": """import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
});""",

    f"{SLUG}/tailwind.config.js": """module.exports = {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
};""",

    f"{SLUG}/postcss.config.js": """module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};""",

    f"{SLUG}/index.html": f"""<!DOCTYPE html>
<html lang=\"en\">
  <head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>{IDEA}</title>
  </head>
  <body>
    <div id=\"root\"></div>
    <script type=\"module\" src=\"/src/main.jsx\"></script>
  </body>
</html>""",

    f"{SLUG}/src/index.css": """@tailwind base;
@tailwind components;
@tailwind utilities;""",

    f"{SLUG}/src/main.jsx": """import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);""",

    f"{SLUG}/src/App.jsx": """import AppLayout from './layout/AppLayout';
import Home from './pages/Home';

function App() {
  return (
    <AppLayout>
      <Home />
    </AppLayout>
  );
}
export default App;""",

    f"{SLUG}/src/layout/AppLayout.jsx": """import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const AppLayout = ({ children }) => {
  return (
    <div className='flex flex-col min-h-screen'>
      <Navbar />
      <main className='flex-1 p-4'>{children}</main>
      <Footer />
    </div>
  );
};

export default AppLayout;""",

    f"{SLUG}/src/components/Navbar.jsx": """const Navbar = () => (
  <nav className='bg-blue-600 text-white p-4'>
    <h1 className='text-xl font-bold'>AI Diet Tracker</h1>
  </nav>
);
export default Navbar;""",

    f"{SLUG}/src/components/Footer.jsx": """const Footer = () => (
  <footer className='bg-gray-800 text-white text-center p-2'>
    <p>© 2025 AI Diet Tracker</p>
  </footer>
);
export default Footer;""",

    f"{SLUG}/src/pages/Home.jsx": f"""const Home = () => (
  <div className='text-center'>
    <h2 className='text-2xl font-bold mb-4'>Welcome to {IDEA}</h2>
    <p className='text-gray-600'>Track your nutrition with AI insights.</p>
  </div>
);
export default Home;""",

    f"{SLUG}/src/lib/api.js": """// Example placeholder for API logic
export const fetchData = async () => {
  return {{ status: 'ok', data: [] }};
};""",

    f"{SLUG}/README.md": f"""# {IDEA}

🚀 Auto-generated polished web app using React + Tailwind.

## Features
- Layout with Navbar + Footer
- Component structure
- Page routing ready
- Tailwind integrated
- Ready for Vercel

## Run locally
```bash
npm install
npm run dev
```"""
}

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"\n✅ Project generated in: {SLUG}/")
