from flask import Flask

from app.main.views import main_bp
from app.candidates.views import candidates_bp
from app.vacancies.views import vacancies_bp

app = Flask(__name__)

app.register_blueprint(main_bp)
app.register_blueprint(candidates_bp)
app.register_blueprint(vacancies_bp)

if __name__ == "__main__":
    app.run()
