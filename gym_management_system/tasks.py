import frappe



def send_weekly_class_summary():

	
	members = frappe.get_all(
		"Gym Member",
		fields=["name", "email"]
	)

	for member in members:

		
		bookings = frappe.get_all(
			"Gym Class Booking",
			filters={
				"member": member.name
			},
			fields=[
				"gym_class",
				"booking_date"
			]
		)

		
		if not bookings:
			continue

		
		message = """
		<h3>Weekly Gym Class Summary</h3>

		<table border="1" cellpadding="5">
			<tr>
				<th>Class</th>
				<th>Date</th>
			</tr>
		"""

		for booking in bookings:

			message += f"""
			<tr>
				<td>{booking.gym_class}</td>
				<td>{booking.booking_date}</td>
			</tr>
			"""

		message += "</table>"

		
		frappe.sendmail(
			recipients=[member.email],
			subject="Weekly Gym Class Summary",
			message=message
		)




@frappe.whitelist()
def custom_get_count(*args, **kwargs):

	return "Override Working"


import frappe


