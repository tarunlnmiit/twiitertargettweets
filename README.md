Steps to get the project up and running:
1. Install virtualenv if not installed
2. Open Terminal and go to your desired directory
3. Run "virtualenv venv"
4. Run "cd venv"
5. install git if not installed
6. Clone this repo "https://github.com/tarunlnmiit/twiitertargettweets.git"
7. Activate the virtualenv "source bin/activate"
8. Install all requriements "pip install -r twittertargettweets/requirements.txt"
9. Run "cd twittertargettweets"
10. Open main/views.py
11. Replace twitter app secrets and tokens with your app secret and tokens in the function search
12. Import temp.json into your MongoDB instance in database "temp" and collection "data"
13. Run Django server "python manage.py runserver"
14. Open "127.0.0.1:8000" in browser
15. Put any search term in the search field and listener for tweets with that term will start.
16. To see stored latest result click on the "See Results" button