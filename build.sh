source .venv/bin/activate
pip install --upgrade pip
rm -rf public
reflex init
API_URL=https://reflex-web.onrender.com reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate