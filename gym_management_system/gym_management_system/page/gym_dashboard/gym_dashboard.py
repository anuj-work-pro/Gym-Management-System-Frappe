import frappe

@frappe.whitelist()
def get_dashboard_data():

    
    total_members = frappe.db.count(
        "Gym Member"
    )

    
    active_members = frappe.db.count(
        "Gym Membership",
        {
            "status": "Active"
        }
    )

    
    trainers_available = frappe.db.count(
        "Gym Trainer",
        {
            "available": 1
        }
    )

    
    revenue = frappe.db.sql("""

        SELECT SUM(price)

        FROM `tabGym Membership`

    """)[0][0] or 0

    
    booked_classes = frappe.db.count(
        "Gym Class Booking"
    )

    return {

        "total_members": total_members,

        "active_members": active_members,

        "trainers_available": trainers_available,

        "revenue": revenue,

        "booked_classes": booked_classes
    }