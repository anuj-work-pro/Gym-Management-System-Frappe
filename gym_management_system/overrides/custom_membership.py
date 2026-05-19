from gym_management_system.gym_management_system.doctype.gym_membership.gym_membership import GymMembership
import frappe

class CustomGymMembership(GymMembership):

    def validate(self):

        super().validate()
        

        # if self.price <= 0:
        #     frappe.throw("Amount must be greater than 0")