import pytest
import os

from app.candidates.dao.candidates_dao import CandidateDAO

path = os.path.join('..', 'data', 'candidates.json')


@pytest.fixture()
def candidates_dao():
    candidates_dao_instance = CandidateDAO(path)
    return candidates_dao_instance


keys_should_be = {"pk", "name", "position"}


class TestCandidateDao:

    def test_get_all(self, candidates_dao):
        """ Проверяем, верный ли список кандидатов возвращается """
        candidates = candidates_dao.get_all()
        assert type(candidates) == list, "возвращается не список"
        assert len(candidates) > 0, "возвращается пустой список"
        assert set(candidates[0].keys()) == keys_should_be, "неверный список ключей"

    @pytest.mark.parametrize("pk", [*range(1, 4)])
    def test_get_by_pk(self, candidates_dao, pk):
        """ Проверяем, верный ли кандидат возвращается при запросе одного """
        candidate = candidates_dao.get_by_pk(pk)
        assert candidate["pk"] == pk, f"возвращается неправильный кандидат #{pk}"
        assert set(candidate.keys()) == keys_should_be, "неверный список ключей"
