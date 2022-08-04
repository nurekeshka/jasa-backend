from jasa.settings import DOMAIN
from .utils import Keyboard, Button

context = {
    'introduction': {
        'text': (
            'Welcome to the Jasa bot!\n'
            'This bot helps you find ongoing events in your area.\n'
            'To save events to your calendar, simply type /signup '
            'and follow the instructions.\n'
            'If you want to know more about the bot, type /help.\n'
            'To get started, type /start.'
        ),
    },
    'start': {
        'text': (
            'Welcome back {user}!\n'
            'If you are stuck, type /help.'
        ),
        'keyboard': Keyboard(
            keyboard_type='reply_keyboard',
            buttons=[
                [
                    Button(
                        button_type='web_app',
                        text='Find events',
                        extra=DOMAIN+'/events/'
                    )
                ]
            ]
        )
    },
    'help': {
        'text': (
            'Here are some commands you can use:\n\n'

            '*Help commands*\n'
            '/intro - Send an introduction message '
            'that guides users on how to use the app.\n'
            '/help - Send a message listing all available commands.\n\n'

            '*Authentication commands*\n'
            '/login - Log in to your account.\n'
            '/logout - Log out of your account.\n'
            '/signup - Sign up for a new account.\n\n'

            '*App commands\n*'
            '/start - Start the app.\n'
            '/explore - Explore events.\n'
            '/search <tags> - Search for events by tags.\n'
            '/profile - View your profile.\n'
        )
    },
    'signup': {
        'text': (
            'To sign up for an account, please click on the button bellow.\n'
        ),
        'keyboard': Keyboard(
            keyboard_type='inline_keyboard',
            buttons=[
                [
                    Button(
                        button_type='web_app',
                        text='Sign up',
                        extra=DOMAIN+'/auth/signup/{id}/'
                    )
                ],
                [
                    Button(
                        button_type='web_app',
                        text='Already have an account? Log in here',
                        extra=DOMAIN+'/auth/login/'
                    )
                ]
            ]
        )
    },
    'login': {
        'text': (
            'To log in to your account, please click on the button bellow.\n'
        ),
        'keyboard': Keyboard(
            keyboard_type='inline_keyboard',
            buttons=[
                [
                    Button(
                        button_type='web_app',
                        text='Log in',
                        extra=DOMAIN+'/auth/login/'
                    )
                ],
                [
                    Button(
                        button_type='web_app',
                        text='Don\'t have an account? Sign up here',
                        extra=DOMAIN+'/auth/signup/{id}/'
                    )
                ]
            ]
        )
    },
    'logout': {
        'text': (
            'Are you sure you want to log out?\n'
            'To confirm, please click on the button bellow\n'
        ),
        'keyboard': Keyboard(
            keyboard_type='inline_keyboard',
            buttons=[
                [
                    Button(
                        button_type='web_app',
                        text='Log out',
                        extra=DOMAIN+'/auth/logout/'
                    )
                ]
            ]
        )
    }
}