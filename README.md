# 📝 TODO
- [ ] Profile page
- [ ] Design Logout page with bootstrap
- [ ] Figure out how to verify registration on event
# 👾 FIXME
- Nothing
# 🚀 Features
- **Event post**
  - [ ] Organizer profile image on event post
  - [ ] Image double press to like
  - [ ] Multiple images per event
  - [ ] Search input
  - [ ] Show events by tags
- **Auth**
  - [x] Implement 'Password Forget'
  - [x] Remember password on login
  - [ ] Link Telegram account to Jasa account
- **General**
  - [ ] Multiple languages
  - [ ] Link google maps to location given in an event
# 🐛 Bugs
- [ ] Background issues with telegram old version
- [ ] Input fields are not same color when in dark mode
- [x] Like and bookmark doesn't work properly
- [x] Fix test errors

# 🔗 Useful links
- https://pythonsansar.com/implement-infinite-scrolling-django/
- https://habr.com/ru/post/666278/
- https://core.telegram.org/bots/webapps
- https://metatags.io/



# 🛠 Setup Commands
Clone this repository
1. For Http
```
git clone 
```
2. For SSH
```
git clone git@github.com:nurekeshka/jasa-backend.git
```


## Host on a server
Change `DOMAIN` key in `.env` file to your domain from ngrok. Don't forget to 
remove `/` at the end.
```
...
DOMAIN = https://website.com
...
```

Follow hosting instruction of your domain provider

### Host on your local server
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

## Using Ngrok

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
