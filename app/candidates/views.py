import os

from flask import Blueprint, render_template
from .dao.candidates_dao import CandidateDAO

candidates_bp = Blueprint('candidates_bp', __name__, template_folder="templates")

path = os.path.join('..', 'data', 'candidates.json')

candidates_dao = CandidateDAO(path)


# Создаем вьюшку для кандидатов
@candidates_bp.route('/candidates/')
def page_candidates():
    candidates = candidates_dao.get_all()
    return render_template("candidates.html", candidates=candidates)


# Создаем вьюшку для одного кандидата
@candidates_bp.route('/candidates/<int:pk>/')
def page_candidate_all(pk):
    candidate = candidates_dao.get_by_pk(pk)
    return render_template("candidate.html", candidate=candidate)
