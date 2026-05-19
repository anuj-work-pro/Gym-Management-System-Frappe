frappe.pages['gym-dashboard'].on_page_load = function(wrapper) {

    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Gym Dashboard',
        single_column: true
    });

    let html = `

        <div class="row">

            <div class="col-md-2">
                <div class="shadow p-4 rounded text-center">
                    <h4>Total Members</h4>
                    <h2 id="members">0</h2>
                </div>
            </div>

            <div class="col-md-2">
                <div class="shadow p-4 rounded text-center">
                    <h4>Active Members</h4>
                    <h2 id="active-members">0</h2>
                </div>
            </div>

            <div class="col-md-2">
                <div class="shadow p-4 rounded text-center">
                    <h4>Available Trainers</h4>
                    <h2 id="trainers">0</h2>
                </div>
            </div>

            <div class="col-md-3">
                <div class="shadow p-4 rounded text-center">
                    <h4>Revenue</h4>
                    <h2 id="revenue">₹0</h2>
                </div>
            </div>

            <div class="col-md-3">
                <div class="shadow p-4 rounded text-center">
                    <h4>Booked Classes</h4>
                    <h2 id="classes">0</h2>
                </div>
            </div>

        </div>

        <br>

        <div class="d-flex gap-2">

        <button 
        class="btn"
        id="refresh"
        style="background-color: black; color: white;"
        >   
        Refresh Dashboard
        </button> 
        

        <button 
        class="btn"
        id="add-member"
        style="background-color: green ;  color: white;"
        >
        Add Member
        </button>

        <button 
        class="btn"
        id="create-membership"
        style="background-color: black ; color: white;"
        >
        Create Membership
        </button>
        </div>

    `;

    $(page.body).html(html);

    load_data();

    
    $('#refresh').click(function() {
        load_data();
    });

    $('#add-member').click(function() {
        frappe.new_doc("Gym Member");
    });

    $('#create-membership').click(function() {
        frappe.new_doc("Gym Membership");
    });

};

function load_data() {

    frappe.call({

        method: "gym_management_system.gym_management_system.page.gym_dashboard.gym_dashboard.get_dashboard_data",

        callback: function(r) {

            if (r.message) {

                $('#members').text(
                    r.message.total_members
                );

                $('#active-members').text(
                    r.message.active_members
                );

                $('#trainers').text(
                    r.message.trainers_available
                );

                $('#revenue').text(
                    "₹" + r.message.revenue
                );

                $('#classes').text(
                    r.message.booked_classes
                );
            }
        }
    });
}