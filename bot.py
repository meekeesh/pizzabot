from telebot import TeleBot, types
from machine import pizza_manager_machine


token = ''

bot = TeleBot(token)


@bot.message_handler(content_types=["text"])
def survey(message):
	if pizza_manager_machine.state == 'size_question':
		if message.text.lower() in ('/start', 'ещё', 'еще', 'заново'):
			bot.send_message(message.chat.id, 'Какую пиццу Вы хотите? Большую или маленькую?')
			pizza_manager_machine.size_answer()
			bot.register_next_step_handler(send, survey)
	if pizza_manager_machine.state == 'save_size':
		pizza_manager_machine.size = message.text
		pizza_manager_machine.save()

	if pizza_manager_machine.state == 'payment_question':
		bot.send_message(message.chat.id, 'Как Вы будете проводить оплату? Наличными или картой?')
		pizza_manager_machine.payment_answer()
		bot.register_next_step_handler(send, survey)
	if pizza_manager_machine.state == 'save_payment':
		pizza_manager_machine.payment_method = message.text
		pizza_manager_machine.save()

	if pizza_manager_machine.state == 'confirmation_question':
		bot.send_message(message.chat.id, f'Вы будете {pizza_manager_machine.size.lower()} пиццу оплата {pizza_manager_machine.payment_method.lower()}?')
		pizza_manager_machine.confirmation_answer()
		bot.register_next_step_handler(send, survey)
	if pizza_manager_machine.state == 'confirmation':
		if message.text.lower() == 'да':
			bot.send_message(message.chat.id, 'Спасибо за заказ!\nЕсли Вы хотите ещё пиццу, то напишите "Ещё".')
			pizza_manager_machine.confirm()
		elif message.text.lower() == 'нет':
			bot.send_message(message.chat.id, 'Если Вы хотите сделать заказ заново, напишите "Заново".')
			pizza_manager_machine.confirm()




while True:
	try:
		bot.polling(none_stop = True)
		break
	except Exception:
		pass
