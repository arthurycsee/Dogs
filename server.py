from flask_app import app
from flask_app.controllers import dogs_controller
# full crud routing
# /table_name/id/action


if __name__ == "__main__":
    app.run(debug=True)