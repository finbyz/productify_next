app_name = "productify_next"
app_title = "Productify Next"
app_publisher = "Finbyz"
app_description = "Productify Next"
app_email = "info@finbyz.com"
app_license = "mit"

on_session_creation = "productify_next.session.on_session_creation"

# Includes in <head>
# ------------------
app_include_js = [
    "https://cdn.plot.ly/plotly-latest.min.js",
    "https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js",
    "assets/productify_next/productify_next/setup.js",
]
# setup_wizard_requires = "assets/productify_next/setup.js"
# include js, css files in header of desk.html
# app_include_css = "/assets/productify_next/css/productify_next.css"
# app_include_js = "/assets/productify_next/js/productify_next.js"

# include js, css files in header of web template
# web_include_css = "/assets/productify_next/css/productify_next.css"
# web_include_js = "/assets/productify_next/js/productify_next.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "productify_next/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Lead": "public/js/doctype_js/lead.js",
    "Customer": "public/js/doctype_js/customer.js",
    "Opportunity": "public/js/doctype_js/opportunity.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "productify_next.utils.jinja_methods",
# 	"filters": "productify_next.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "productify_next.install.before_install"
# after_install = "productify_next.setup.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "productify_next.uninstall.before_uninstall"
# after_uninstall = "productify_next.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "productify_next.utils.before_app_install"
# after_app_install = "productify_next.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "productify_next.utils.before_app_uninstall"
# after_app_uninstall = "productify_next.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "productify_next.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Contact": {
        "validate": "productify_next.productify_next.doc_events.contact.validate",
    },
}

# Scheduled Tasks
# ---------------

scheduler_events = {
    "all": [
        "productify_next.schedule.bg_employee_log_generation",
        "productify_next.schedule.schedule_comments",
        "productify_next.schedule.create_productify_work_summary_today",
    ],
    "cron": {
        "0 1 * * *": [
            "productify_next.schedule.create_productify_work_summary",
            "productify_next.schedule.delete_productify_error_logs",
            "productify_next.schedule.delete_screenshots",
            "productify_next.schedule.delete_application_logs",
        ],
        "0 0 * * *": [
            "productify_next.schedule.submit_timesheet_created_by_productify",
        ],
        # "5 4 * * sun" :[
        #     "productify_next.schedule.send_weekly_report",
        # ]
    },
}
# 	"all": [
# 		"productify_next.tasks.all"
# 	],
# 	"daily": [
# 		"productify_next.tasks.daily"
# 	],
# 	"hourly": [
# 		"productify_next.tasks.hourly"
# 	],
# 	"weekly": [
# 		"productify_next.tasks.weekly"
# 	],
# 	"monthly": [
# 		"productify_next.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "productify_next.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "productify_next.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "productify_next.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["productify_next.utils.before_request"]
# after_request = ["productify_next.utils.after_request"]

# Job Events
# ----------
# before_job = ["productify_next.utils.before_job"]
# after_job = ["productify_next.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"productify_next.auth.validate"
# ]{task} - {issue}

fixtures = [
    {"dt": "Custom Field", "filters": [["fieldname", "=", "is_created_by_productify"]]},
    {
        "dt": "Activity Type",
        "filters": [
            ["name", "in", ["Project", "Task", "Issue"]]
        ]
    }
]
