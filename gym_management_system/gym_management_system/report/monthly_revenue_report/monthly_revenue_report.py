import frappe

def execute(filters=None):

    columns = get_columns()

    data = get_data()

    chart = get_chart(data)

    return columns, data, None, chart


def get_columns():

    return [

        {
            "label": "Month",
            "fieldname": "month",
            "fieldtype": "Data",
            "width": 150
        },

        {
            "label": "Revenue",
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "width": 150
        }

    ]


def get_data():

    data = frappe.db.sql("""

        SELECT

            MONTHNAME(start_date) as month,

            SUM(price) as revenue

        FROM

            `tabGym Membership`

        GROUP BY

            MONTH(start_date)

    """, as_dict=True)

    return data


def get_chart(data):

    labels = []
    values = []

    for d in data:

        labels.append(d.month)
        values.append(d.revenue)

    return {

        "data": {

            "labels": labels,

            "datasets": [
                {
                    "name": "Revenue",
                    "values": values
                }
            ]
        },

        "type": "bar",

        "height": 300
    }