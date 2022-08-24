import string

from telebot.types import (
	InlineKeyboardMarkup, InlineKeyboardButton,
	ReplyKeyboardMarkup, KeyboardButton,

	WebAppInfo,
)


class Keyboard:
	def __init__(self, keyboard_type='reply_keyboard', buttons=[]):
		self.buttons = buttons

		if keyboard_type == 'reply_keyboard':
			self.keyboard_class = ReplyKeyboardMarkup
			self.button_class = KeyboardButton
		elif keyboard_type == 'inline_keyboard':
			self.keyboard_class = InlineKeyboardMarkup
			self.button_class = InlineKeyboardButton

	def create(self, sub_values={}, options={}):
		"""
		Creates a keyboard from a given format. 
		Applies given values to placeholders.
		"""
		keyboard = self.keyboard_class(**options)
		for row in self.buttons:
			keyboard_row = [
				button.create(self.button_class, sub_values) for button in row
			]
			keyboard.row(*keyboard_row)
		return keyboard


class Button:
	def __init__(self, button_type='callback_data', text='', extra=''):
		self.button_type = button_type
		self.text = text

		if button_type in ('callback_data', 'url'):
			self.extra_type = str
			self.extra = extra
		elif button_type == 'web_app':
			self.extra_type = WebAppInfo
			self.extra = extra

	def create(self, button_class, sub_values={}):
		"""
		Creates a button from a given format. 
		Applies given values to placeholders.
		"""
		button_params = {
			'text': format_text(self.text, self.button_type),
			self.button_type: self.extra_type(
				format_text(self.extra, sub_values)
			)
		}
		return button_class(**button_params)


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


def format_text(text, placeholder_values):
	"""
	Formats a text string with given placeholder values.
	Example:
	```python
	text='Hello {name}, how are you?. My name is {bot_name}.'
	placeholder_values = {'name': 'John', 'bot_name': 'Jasa', 'age': '25'}
	res = 'Hello John, how are you?. My name is Jasa.'
	```
	"""
	keys = get_format_keys(text)
	ddict = dict(zip(keys, [placeholder_values[key] for key in keys]))
	return text.format(**ddict)
