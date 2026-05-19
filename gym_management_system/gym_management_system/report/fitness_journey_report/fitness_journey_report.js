frappe.query_reports["Fitness Journey Report"] = {

    filters: [

        {
            fieldname: "member",
            label: "Gym Member",
            fieldtype: "Link",
            options: "Gym Member",
            reqd: 1
        }

    ]
};