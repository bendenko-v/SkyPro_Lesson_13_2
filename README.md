# Flask-приложение и тесты

* Приложение работает, тесты dao тоже, а тесты candidates и vacancies не работают из-за путей, хотя запускаются через test_client() приложения.
* Второй вариант: можно сделать пути такими что все тесты работают, для этого ставлю ".." в пути перед data во вьюшках candidates и vacancies, тогда все тесты работают, но в приложении будет работать только Главная страница, кандидаты и вакансии загружаться не будут..