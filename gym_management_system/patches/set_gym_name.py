import frappe
def execute():

	members = frappe.get_all(
		"Gym Membership",
		fields=["name"]
	)

	for member in members:

		frappe.db.set_value(
			"Gym Membership",
			member.name,
			"Gym_new_name",
			"Fitness Funda"
		)

	