sudo apt install node
cd front
npm install
npm run build
cd ..
gunicorn -b 0.0.0.0:$PORT back.src.main:app