from transitions import Machine


states      = ['size_question', 'save_size', 'payment_question', 'save_payment', 'confirmation_question', 'confirmation']
transitions = [
	{'trigger': 'size_answer',         'source': 'size_question',         'dest': 'save_size'},
	{'trigger': 'save',                'source': 'save_size',             'dest': 'payment_question'},
	{'trigger': 'payment_answer',      'source': 'payment_question',      'dest': 'save_payment'},
	{'trigger': 'save',                'source': 'save_payment',          'dest': 'confirmation_question'},
	{'trigger': 'confirmation_answer', 'source': 'confirmation_question', 'dest': 'confirmation'},
	{'trigger': 'confirm',             'source': 'confirmation',          'dest': 'size_question'},
]

class PizzaManagerBot(object):
	def __init__(self, size='', payment_method=''):
		self.size           = ''
		self.payment_method = ''

		self.machine = Machine(model=self, states=states, transitions=transitions, initial='size_question')


pizza_manager_machine = PizzaManagerBot()
