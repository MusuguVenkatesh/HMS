/** @odoo-module **/

import { registry } from '@web/core/registry';
import { FormController } from '@web/views/form/form_controller';
import { patch } from '@web/core/utils/patch';


console.log('reset_form.js file loaded!');

patch(FormController, 'hospital_patient_form_reset', {
    async _onCustomEvent(ev) {
        await this._super(ev);
        if (ev.detail.type === 'clear_hospital_patient_form') {
            // Get the form view record
            const record = this.model.get(this.model.root.id);
            if (record && record.fields) {
                // Iterate through the editable fields and reset their values
                for (const fieldName in record.fields) {
                    if (!record.fields[fieldName].readonly) {
                        let resetValue;
                        switch (record.fields[fieldName].type) {
                            case 'char':
                            case 'text':
                                resetValue = '';
                                break;
                            case 'integer':
                            case 'float':
                                resetValue = 0;
                                break;
                            case 'boolean':
                                resetValue = false;
                                break;
                            case 'many2one':
                                resetValue = false; // Or null
                                break;
                            case 'one2many':
                            case 'many2many':
                                resetValue = [];
                                break;
                            case 'date':
                            case 'datetime':
                                resetValue = false; // Or null
                                break;
                            default:
                                resetValue = false;
                        }
                        record.update({ [fieldName]: resetValue });
                    }
                }
            }
        }
    },
});

// Register the 'do_nothing' client action
const DoNothingAction = {
    name: 'do_nothing',
    trigger() {
        // This action doesn't need to do anything
    },
};
registry.clientActions.add('do_nothing', DoNothingAction);