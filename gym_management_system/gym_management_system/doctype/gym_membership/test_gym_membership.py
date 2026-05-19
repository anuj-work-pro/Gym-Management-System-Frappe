import frappe
from frappe.tests.utils import FrappeTestCase
from frappe.utils import today, add_days


class TestGymMembership(FrappeTestCase):

	def test_membership_creation(self):

		member = frappe.get_doc({
			"doctype": "Gym Member",
			"member_name": "Test Member"
		}).insert(ignore_if_duplicate=True)

		plan = frappe.get_doc({
			"doctype": "Membership Plan",
			"plan": "Monthly",
			"price": 1000
			
		}).insert(ignore_if_duplicate=True)

		membership = frappe.get_doc({
			"doctype": "Gym Membership",
			"gym_member": member.name,
			"membership_plan": plan.name,
			"start_date": today(),
			
		}).insert()

		


	