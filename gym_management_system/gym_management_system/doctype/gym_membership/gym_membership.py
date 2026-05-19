import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import add_days


class GymMembership(Document):
	def validate(self):
		self.set_end_date()
		self.validate_price()

	def set_end_date(self):
		if self.membership_plan and self.start_date:
			plan = frappe.get_doc("Membership Plan", self.membership_plan)

			self.end_date = add_days(self.start_date, int(plan.duration))

	def validate_price(self):
		if self.price <= 0:
			frappe.throw(_("Amount must be greater than 0"))

	def on_submit(self):
		self.db_set("status", "Active")
