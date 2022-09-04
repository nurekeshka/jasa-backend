from jasa.settings import DOMAIN
from .utils import Keyboard, Button

context = {
    'intro': {
        'text': (
            'Добро пожаловать в Jasa bot!\n'
            'Я помогу вам найти текущее событие и мероприятие в вашем регионе.\n'
            'Для того, чтобы использовать этого бота, вам необходимо' 'зарегистрироваться с помощью команды /signup'
            'Если вы хотите узнать больше о bot-е, введите /help.\n'
            'Чтобы начать, введите /start'
        ),
        'keyboard': Keyboard(
            keyboard_type='inline_keyboard',
            buttons=[
                [
                    Button(
                        button_type='web_app',
                        text='Войти',
                        extra=DOMAIN + '/login/'
                    ),
                ],
                [
                    Button(
                        button_type='web_app',
                        text='Зарегистрироваться',
                        extra=DOMAIN + '/signup/'
                    ),
                ]
            ]
        )
    },
    'start': {
        'text': (
            'Добро пожаловать {user}!\n'
            'если у вас есть вопросы, напишите /help.'
        ),
        'keyboard': Keyboard(
            keyboard_type='reply_keyboard',
            buttons=[
                [
                    Button(
                        button_type='web_app',
                        text='🌐 Текущие события',
                        extra=DOMAIN + '/events/'
                    ),
                    Button(
                        button_type='web_app',
                        text='🔎 Поиск',
                        extra=DOMAIN + '/search/'
                    ),
                    Button(
                        button_type='web_app',
                        text='📅 Настройки',
                        extra=DOMAIN + '/settings/'
                    )
                ],
                [
                    Button(
                        button_type='web_app',
                        text='👤 Профиль',
                        extra=DOMAIN + '/profile/{username}/'
                    ),
                ]
            ]
        ),
    },
    'help': {
        'text': (
            'Вот несколько команд, которые вы можете использовать:\n\n'

            '*Команды справки*\n'
            '/intro - Отправить вводное сообщение '
            'это руководство для пользователей о том, как использовать приложение.\n'
            '/help - Отправить сообщение со списком всех доступных команд.\n\n'

            '*Команды аутентификации*\n'
            '/login - войдите в свою учетную запись.\n'
            '/logout из системы - выйдите из своей учетной записи.\n'
            '/signup - Подпишитесь на новую учетную запись.\n\n'

            '*Команды бота\n*'
            '/start - Запустить приложение.\n'
            '/explore - Исследовать события.\n'
            #'/search <теги> - Поиск событий по тегам.\n'
            '/profile - Просмотр вашего профиля.\n'
        )
    },
    'signup': {
        'text': (
            'Чтобы зарегистрировать аккаунт, пожалуйста, нажмите на кнопку ниже.\n'
        ),
        'keyboard': Keyboard(
            keyboard_type='inline_keyboard',
            buttons=[
                [
                    Button(
                        button_type='web_app',
                        text='👤 Зарегистрироваться',
                        extra=DOMAIN + '/auth/signup/'
                    )
                ],
                [
                    Button(
                        button_type='web_app',
                        text='У вас уже есть аккаунт? Войдите в систему здесь',
                        extra=DOMAIN + '/auth/login/'
                    )
                ]
            ]
        )
    },
    'login': {
        'text': (
            'Чтобы войти в свою аккаунт, пожалуйста, нажмите на кнопку ниже.\n'
        ),
        'keyboard': Keyboard(
            keyboard_type='inline_keyboard',
            buttons=[
                [
                    Button(
                        button_type='web_app',
                        text='↪️ Войти',
                        extra=DOMAIN + '/auth/login/'
                    )
                ],
                [
                    Button(
                        button_type='web_app',
                        text='У вас нет учетной записи? Зарегистрируйтесь здесь',
                        extra=DOMAIN + '/auth/signup/'
                    )
                ]
            ]
        )
    },
    'logout': {
        'text': (
            'Вы уверены, что хотите выйти из системы?'
            'Для подтверждения, пожалуйста, нажмите на кнопку ниже\n'
        ),
        'keyboard': Keyboard(
            keyboard_type='inline_keyboard',
            buttons=[
                [
                    Button(
                        button_type='web_app',
                        text='↩️ Выйти',
                        extra=DOMAIN + '/auth/logout/'
                    )
                ]
            ]
        )
    },
    'about': {
        'text': (
            'Этот бот был создан @H_reugo\n'
            'Github - https://github.com/Hereugo\n'
            'Linkedin - https://www.linkedin.com/in/amir-nurmukhambetov-190a6b214/\n'
        )
    },
    'explore': {
        'text': (
            'Чтобы просмотреть все последние события, пожалуйста, нажмите кнопку ниже.'
        ),
        'keyboard': Keyboard(
            keyboard_type='inline_keyboard',
            buttons=[
                [
                    Button(
                        button_type='web_app',
                        text='🌐 Текущие события',
                        extra=DOMAIN + '/events'
                    )
                ]
            ]
        )
    },
    'profile': {
        'text': (
            'To open your profile press the button below.'
        ),
        'warning_text': (
            'В настоящее время вы не вошли в аккаунт, войдите в систему до прежде чем получить доступ к вашему профилю'
        ),
        'keyboard': Keyboard(
            keyboard_type='inline_keyboard',
            buttons=[
                [
                    Button(
                        button_type='web_app',
                        text='👤 Профиль',
                        extra=DOMAIN + '/profile/{username}/'
                    )
                ]
            ]
        )
    }
}