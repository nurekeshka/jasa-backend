import string

from telebot.types import (
	ReplyKeyboardMarkup, KeyboardButton,
	WebAppInfo
)


def create_reply_keyboard(buttons, placeholder_values = {}, options = {}):
	"""
	Creates a reply keyboard from a given format. 
	Applies given values to placeholders.
	"""
	keyboard = ReplyKeyboardMarkup(**options)
	for row in buttons:
		keyboard_row = []
		for button in row:
			text_keys = get_format_keys(button['text'])
			text_dict = dict(zip(text_keys, [
								 placeholder_values[key]['text'] 
								 for key in text_keys
						]))
			web_app_keys = get_format_keys(button['web_app'])
			web_app_dict = dict(zip(web_app_keys, [
								 placeholder_values[key]['web_app']
								 for key in web_app_keys
						]))
			
			print(button['web_app'].format(**web_app_dict))

			reply_button = KeyboardButton(
				button['text'].format(**text_dict),
				web_app=WebAppInfo(button['web_app'].format(**web_app_dict))
			)

			keyboard_row.append(reply_button)
		keyboard.row(*keyboard_row)

	return keyboard


def get_format_keys(s: str):
	"""
	Finds all format keys in a string.
	Example:
	```python
	s = 'Hello {name}, how are you?. My name is {bot_name}.'
	res = ['name', 'bot_name']
	```
	"""
	keys = [t[1] for t in string.Formatter().parse(s) if t[1] is not None]
	return keys
