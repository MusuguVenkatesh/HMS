//odoo.define('hospital_management.icu_bed_ui', function (require) {
//    "use strict";
//
//    var FormController = require('web.FormController');
//    var Dialog = require('web.Dialog');
//
//    FormController.include({
//        _onClick: function (event) {
//            var $target = $(event.target);
//            if ($target.hasClass('img-fluid') && $target.data('bed-id')) {
//                var bedId = $target.data('bed-id');
//                var bed = this.model.get(bedId);
//                if (bed.status == 'available') {
//                    // Show form to fill patient details
//                    var dialog = new Dialog(this, {
//                        title: 'Assign Bed',
//                        buttons: [
//                            { text: 'Cancel', close: true },
//                            { text: 'Save', close: true, classes: 'btn-primary', click: this._onSaveBedBooking.bind(this, bedId) }
//                        ],
//                        $content: $(`
//                            <div>
//                                <label for="patient_id">Assign Patient</label>
//                                <input type="text" id="patient_id" class="form-control"/>
//                            </div>`)
//                    });
//                    dialog.open();
//                }
//            }
//        },
//
//        _onSaveBedBooking: function (bedId) {
//            var patientId = $('#patient_id').val();
//            if (patientId) {
//                var bed = this.model.get(bedId);
//                bed.assign_bed(patientId);
//            }
//        }
//    });
//});
