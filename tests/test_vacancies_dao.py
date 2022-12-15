import os
import pytest

from app.vacancies.dao.vacancies_dao import VacanciesDAO

path = os.path.join('.', 'data', 'vacancies.json')

keys_should_be = {"pk", "company", "position", "salary"}


@pytest.fixture()
def vacancies_dao():
    vacancies_dao_instance = VacanciesDAO(path)
    return vacancies_dao_instance


class TestVacanciesDAO:

    def test_get_all(self, vacancies_dao):
        """ Проверяем получение всех вакансий"""
        vacancies = vacancies_dao.get_all()
        assert type(vacancies) == list
        assert len(vacancies) > 0
        assert set(vacancies[0].keys()) == keys_should_be

    @pytest.mark.parametrize("pk", [*range(1, 4)])
    def test_get_by_pk(self, vacancies_dao, pk):
        """ Проверяем получение одной вакансии"""
        vacancy = vacancies_dao.get_by_pk(pk)
        assert type(vacancy) == dict
        assert vacancy["pk"] == pk
        assert set(vacancy.keys()) == keys_should_be
