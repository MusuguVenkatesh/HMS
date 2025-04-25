odoo.define('patient.icu_booking', function (require) {
    "use strict";

    var core = require('web.core');
    var Widget = require('web.Widget');

    var ICUBookingWidget = Widget.extend({
        events: {
            'click .o_kanban_record': '_onBedClick',
        },

        _onBedClick: function (event) {
            // Trigger opening of booking wizard when a bed is clicked
            var bed_id = $(event.currentTarget).data('bed-id');
            this.do_action({
                type: 'ir.actions.act_window',
                res_model: 'hospital.icu.booking.wizard',
                views: [[false, 'form']],
                target: 'new',
                context: { 'default_bed_id': bed_id },
            });
        },
    });

    core.action_registry.add('icu_booking_widget', ICUBookingWidget);

    return ICUBookingWidget;
});
