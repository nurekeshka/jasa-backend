from jasa.settings import DOMAIN

context = {
    'introduction': {
        'text': (
            'Welcome to the Jasa bot!\n'
            'This bot helps you find ongoing events in your area.\n'
            'To save events to your calendar, simply type /signup and follow the instructions.\n'
            'If you want to know more about the bot, type /help.\n'
            'To get started, type /start.'
        ),
    },
    'start': {
        'text': (
            'Welcome back {user}!\n'
            'If you are stuck, type /help.'
        ),
        'buttons': [
            [
                {
                    'text': '🌐 Explore',
                    'web_app': DOMAIN + '{user_id}/events/',
                },
                # {
                #     'text': '/search',
                #     'web_app': DOMAIN + 'search/',
                # },
                # {
                #     'text': '/profile',
                #     'web_app': DOMAIN + 'profile/',
                # },
            ]
        ]
    },
    'help': {
        'text': (
            'Here are some commands you can use:\n\n'

            '*Help commands*\n'
            '/intro - Send an introduction message that guides users on how to use the app.\n'
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
    }
}