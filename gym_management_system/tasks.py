import frappe


def send_weekly_class_summary():
	members = frappe.get_all("Gym Member", fields=["name", "email"])

	for member in members:
		bookings = frappe.get_all(
			"Gym Class Booking", filters={"member": member.name}, fields=["gym_class", "booking_date"]
		)

		if not bookings:
			continue

		message = "<h3>Weekly Gym Class Reminder</h3>"

		for booking in bookings:
			message += f"""
			<p>
			Class: {booking.gym_class}
			<br>
			Date: {booking.booking_date}
			</p>
			"""

		frappe.sendmail(recipients=[member.email], subject="Weekly Gym Class Reminder", message=message)


@frappe.whitelist()
def send_summary_in_background():
	frappe.enqueue("gym_management_system.tasks.send_weekly_class_summary", queue="default", timeout=300)

	return "Background Job Started"


@frappe.whitelist()
def custom_logged_user():
	return {"user": frappe.session.user, "message": "Custom Override Working"}
