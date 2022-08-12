# jasa-backend

## 📝 TODO
- [x] Design Signup/Login page with bootstrap
- [ ] Design Logout page with bootstrap
- [ ] Work on TODOs
- [ ] Profile page
- [ ] Create Tag model
- [ ] Display the *Relationships* design on github using mermaid js
- [x] Have well written instruction on how to setup `README.md`
- [x] TDD 

## 🐛 Bugs
- [ ] Background issues with telegram old version
- [x] Signup doesn't work
- [ ] Intro message is not sent
- [ ] Guest users can still like/bookmark events
- [ ] Password input values are shown

## 🔗 Useful links
- https://pythonsansar.com/implement-infinite-scrolling-django/
- https://habr.com/ru/post/666278/
- https://core.telegram.org/bots/webapps
- https://metatags.io/

## 🛠 Setup Commands
Clone this repository
1. For Http
```
git clone 
```
2. For SSH
```
git clone git@github.com:nurekeshka/jasa-backend.git
```

Goto the projects directory
```
cd YOUR_PROJECT_PATH
```

Setup virtual environment (optional)
```
python3 -m venv venv
```

Activate venv
1. For windows
```
source venv
```
2. For Mac and Linux
```
source venv/bin/activate
```

Install requirements
```
pip install -r requirements.txt
```

Goto projects app directory
```
cd jasa
```

Setup ngrok server. Make sure to connect to the same port as in `.env` file (default in `.env` file: 8000)
```
ngrok http 8000
```

Change `DOMAIN` key in `.env` file to given domain from ngrok. Don't forget to remove `/` at the end.
```
...
DOMAIN = https://abcd-123-12-123-123.eu.ngrok.io
...
```

Then, simply run the server using this command.
```
python3 manage.py runserver
```

