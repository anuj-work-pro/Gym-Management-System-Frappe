# Copyright (c) 2026, anuj and contributors
# For license information, please see license.txt

import frappe
import random

from frappe.model.document import Document
from frappe.utils import date_diff


class GymLockerBooking(Document):

    def validate(self):

        if self.locker and self.start_date and self.end_date:

            locker = frappe.get_doc(
                "Locker",
                self.locker
            )

            total_days = date_diff(
                self.end_date,
                self.start_date
            )

            if total_days <= 0:

                frappe.throw(
                    "End Date must be after Start Date"
                )

            self.payable_amount = (
                total_days * locker.locker_price
            )

    def before_save(self):

        self.locker_code = (
            f"L-{random.randint(1, 50)}"
        )