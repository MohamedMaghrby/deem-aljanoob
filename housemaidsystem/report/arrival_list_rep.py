from odoo import models, api


class ArrivalListRep(models.AbstractModel):
    _name = "report.housemaidsystem.arrival_list_rep"
    _description = "Arrival List Report"


    @api.model
    def _get_report_values(self, docids, data=None):

        invoice_domain = [('id', '!=', 0)]
        rep_head_line1 = ''
        rep_head_line2 = 'Invoice Status: All Status'
        rep_head_line3 = 'External Office: All'

        # 1) From Date
        if data['from_date']:
            invoice_domain.append(
                ('arrival_date', '>=', data['from_date']),
            )
            rep_head_line1 = 'From Date: ' + data['from_date']
        # 2) To Date
        if data['to_date']:
            invoice_domain.append(
                ('arrival_date', '<=', data['to_date']),
            )
            rep_head_line1 += ' - To Date: ' + data['to_date']
        # 3) External Offices
        if data['external_office']:
            invoice_domain.append(
                ('application_id.office_code.id', '=', data['external_office'])
            )
            external_office_obj = self.env['housemaidsystem.configuration.externaloffices'].search([('id', '=', data['external_office'])])
            if external_office_obj:
                rep_head_line3 = 'External Office: ' + external_office_obj.name
        # 4) Invoice Status
        if data['invoice_status']:
            invoice_domain.append(
                ('invoice_sales_id.state', '=', data['invoice_status'])
            )
            rep_head_line2 = 'Invoice Status: ' + data['invoice_status']



        docs = self.env['housemaidsystem.applicant.arrival'].search(invoice_domain)
        docargs = {
            'doc_ids': docids,
            'doc_model': 'housemaidsystem.applicant.arrival',
            'docs': docs,
            'rep_head_line1': rep_head_line1,
            'rep_head_line2': rep_head_line2,
            'rep_head_line3': rep_head_line3
        }
        return docargs