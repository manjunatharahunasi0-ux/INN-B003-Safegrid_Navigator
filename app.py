import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from api.routes import app

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Starting Safegrid Navigator")
    print("=" * 60)
    print("Backend API: http://localhost:5000")
    print("Frontend: Open frontend/index.html in your browser")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)
