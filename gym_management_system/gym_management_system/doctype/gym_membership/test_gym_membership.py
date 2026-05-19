import frappe
from frappe.tests.utils import FrappeTestCase
from frappe.utils import add_days


class TestGymMembership(FrappeTestCase):

	def setUp(self):

		if not frappe.db.exists(
			"Membership Plan",
			"Monthly"
		):

			self.plan=frappe.get_doc({

				"doctype": "Membership Plan",
				
				"plan": "Monthly",
				"duration": 30,
				"price": 1000

			}).insert()

	def test_set_end_date(self):

		membership = frappe.get_doc({

			"doctype": "Gym Membership",
			"membership_plan": self.plan.name,
			"start_date": "2026-05-01",
			"price": 1000

		})

		membership.set_end_date()

		expected_date = add_days(
			"2026-05-01",
			30
		)

		self.assertEqual(
			membership.end_date,
			expected_date
		)

	def test_validate_price(self):

		membership = frappe.get_doc({

			"doctype": "Gym Membership",
			"membership_plan": "Monthly",
			"start_date": "2026-05-01",
			"price": 0

		})

		self.assertRaises(
			frappe.ValidationError,
			membership.validate_price
		)

	