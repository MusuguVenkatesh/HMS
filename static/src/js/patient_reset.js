///** @odoo-module **/
//
//import { registry } from "@web/core/registry";
//import { FormController } from "@web/views/form/form_controller";
//
//class CustomPatientFormController extends FormController {
//    async onClickButton(event) {
//        const buttonName = event.currentTarget?.attributes?.name?.value;
//        if (buttonName === "action_reset_form") {
//            // Clear fields manually without reloading
//            const fieldsToClear = [
//                "name",
//                "date_of_birth",
//                "gender",
//                "contact_number",
//                "blood_group",
//                "martial_status",
//                "state_id",
//                "address",
//                "case_description"
//            ];
//
//            for (const field of fieldsToClear) {
//                if (this.model.meta.fields[field]) {
//                    this.model.setValue(field, null);
//                }
//            }
//
//            this.env.services.notification.add("Form data cleared.", {
//                type: "warning",
//            });
//
//            // Prevent backend call
//            return;
//        }
//
//        // Otherwise, default behavior
//        super.onClickButton(event);
//    }
//}
//
//registry.category("views").add("hospital_patient_form", {
//    ...registry.category("views").get("form"),
//    Controller: CustomPatientFormController,
//});
