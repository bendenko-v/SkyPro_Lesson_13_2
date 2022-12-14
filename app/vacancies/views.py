import os

from flask import Blueprint, render_template
from .dao.vacancies_dao import VacanciesDAO

vacancies_bp = Blueprint('vacancies_bp', __name__, template_folder="templates")

path = os.path.join('..', 'data', 'vacancies.json')

vacancies_dao = VacanciesDAO(path)


@vacancies_bp.route('/vacancies/')
def page_vacancies():
    vacancies = vacancies_dao.get_all()
    return render_template("vacancies.html", vacancies=vacancies)


@vacancies_bp.route('/vacancies/<int:pk>')
def page_vacancy(pk):
    vacancy = vacancies_dao.get_by_pk(pk)
    return render_template("vacancy.html", vacancy=vacancy)
