frappe.ui.form.on('Lead', {
	refresh: function(frm) {
		if(!frm.doc.__islocal){
			frm.add_custom_button(__("Meeting Schedule"), function() {
				return frappe.call({
					method : "Productify Next.api.make_meetings",
					args: {
						"source_name": frm.doc.name,
						"doctype": 'Lead',
						"ref_doctype": 'Meeting Schedule'
					},
					callback: function(r) {
						if(!r.exc) {
							var doc = frappe.model.sync(r.message);
							frappe.set_route("Form", r.message.doctype, r.message.name);
						}
					}
				})
			}, __("Create"));
			
			frm.add_custom_button(__("Meeting"), function() {
				return frappe.call({
					method : "Productify Next.api.make_meetings",
					args: {
						"source_name": frm.doc.name,
						"doctype": 'Lead',
						"ref_doctype": 'Meeting'
					},
					callback: function(r) {
						if(!r.exc) {
							var doc = frappe.model.sync(r.message);
							frappe.set_route("Form", r.message.doctype, r.message.name);
						}
					}
				})
			}, __("Create"));
		}
	},
});