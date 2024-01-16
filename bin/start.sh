npm install
npm run build
gunicorn -b 0.0.0.0:$PORT back.src.main:app