import sys
sys.path.append('.')
sys.path.append('./app')

from app.init_app import app


app.run(debug=True)