from frappe.model.document import Document
import frappe


class Locker(Document):

	def validate(self):
		

		if self.locker_type == "small":
			self.locker_price = 20

		elif self.locker_type == "big":
			self.locker_price = 50

		else:
			self.locker_price = 100