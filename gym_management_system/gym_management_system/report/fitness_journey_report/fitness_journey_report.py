import frappe

def execute(filters=None):

    columns = get_columns()

    data = get_data(filters)

    chart = get_chart(data)

    return columns, data, None, chart


def get_columns():

    return [
        

        {
            "label": "Date",
            "fieldname": "date",
            "fieldtype": "Date",
            "width": 120
        },

        {
            "label": "Weight",
            "fieldname": "weight",
            "fieldtype": "Float",
            "width": 120
        },

        {
            "label": "Calories Intake",
            "fieldname": "calories_intake",
            "fieldtype": "Float",
            "width": 150
        },

        {
            "label": "Calories Burned",
            "fieldname": "calories_burnt",
            "fieldtype": "Float",
            "width": 150
        },

        {
            "label": "BMI",
            "fieldname": "bmi",
            "fieldtype": "Float",
            "width": 100
        }

    ]


def get_data(filters):

    return frappe.get_all(

        "Fitness Progress",

        filters={
            "member": filters.get("member")
        },

        fields=[
            
            "date",
            "weight",
            "calories_intake",
            "calories_burnt",
            "bmi"
        ],

        order_by="date asc"
    )


def get_chart(data):

    labels = []
    weights = []

    for d in data:
        labels.append(str(d.date))
        weights.append(d.weight)

    chart = {

        "data": {
            "labels": labels,

            "datasets": [
                {
                    "name": "Weight",
                    "values": weights
                }
            ]
        },

        "type": "line",

        "height": 300
    }

    return chart