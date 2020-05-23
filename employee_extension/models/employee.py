from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    ppsn = fields.Char('PPSN')
    ppsn_issue_date = fields.Date('PPSN Issue Date')
    effective_date = fields.Date('Effective Date', compute='compute_rpn_values')
    end_date = fields.Date('end Date', compute='compute_rpn_values')
    usc_yearly_cut_off_1 = fields.Float('USC yearly cut off 1', compute='compute_rpn_values')
    usc_yearly_cut_off_2 = fields.Float('USC yearly cut off 2', compute='compute_rpn_values')
    usc_yearly_cut_off_3 = fields.Float('USC yearly cut off 3', compute='compute_rpn_values')
    usc_yearly_cut_off_4 = fields.Float('USC yearly cut off 4', compute='compute_rpn_values')
    usc_yearly_rate_1 = fields.Float('USC Yearly Rate 1', compute='compute_rpn_values')
    usc_yearly_rate_2 = fields.Float('USC Yearly Rate 2', compute='compute_rpn_values')
    usc_yearly_rate_3 = fields.Float('USC Yearly Rate 3', compute='compute_rpn_values')
    usc_yearly_rate_4 = fields.Float('USC Yearly Rate 4', compute='compute_rpn_values')
    yearly_standard_tax = fields.Float('Standard Tax Rate', compute='compute_rpn_values')
    yearly_top_tax = fields.Float('Top Tax Rate', compute='compute_rpn_values')
    prsi_exempt = fields.Float('PRSI Exempt', compute='compute_rpn_values')
    yearly_tax_credits = fields.Float('Yearly Tax Credits', compute='compute_rpn_values')
    yearly_rate_cut_off = fields.Float('Yearly Rate Cut Off', compute='compute_rpn_values')
    prsi_class = fields.Char('PRSI Class', compute='compute_rpn_values')
    rpn_ids = fields.One2many('hr.employee.rpn', 'employee_id', string='RPN')

    def compute_rpn_values(self):
        for emp in self:
            rpn_id = emp.rpn_ids[0] if emp.rpn_ids else False
            if rpn_id:
                emp.effective_date = rpn_id.effective_date
                emp.end_date = rpn_id.end_date
                emp.usc_yearly_cut_off_1 = rpn_id.usc_yearly_cut_off_1
                emp.usc_yearly_cut_off_2 = rpn_id.usc_yearly_cut_off_2
                emp.usc_yearly_cut_off_3 = rpn_id.usc_yearly_cut_off_3
                emp.usc_yearly_cut_off_4 = rpn_id.usc_yearly_cut_off_4
                emp.usc_yearly_rate_1 = rpn_id.usc_yearly_rate_1
                emp.usc_yearly_rate_2 = rpn_id.usc_yearly_rate_2
                emp.usc_yearly_rate_3 = rpn_id.usc_yearly_rate_3
                emp.usc_yearly_rate_4 = rpn_id.usc_yearly_rate_4
                emp.yearly_standard_tax = rpn_id.yearly_standard_tax
                emp.yearly_top_tax = rpn_id.yearly_top_tax
                emp.prsi_exempt = rpn_id.prsi_exempt
                emp.yearly_tax_credits = rpn_id.yearly_tax_credits
                emp.yearly_rate_cut_off = rpn_id.yearly_rate_cut_off
                emp.prsi_class = rpn_id.prsi_class
            else:
                emp.effective_date = False
                emp.end_date = False
                emp.usc_yearly_cut_off_1 = ''
                emp.usc_yearly_cut_off_2 = ''
                emp.usc_yearly_cut_off_3 = ''
                emp.usc_yearly_cut_off_4 = ''
                emp.usc_yearly_rate_1 = ''
                emp.usc_yearly_rate_2 = ''
                emp.usc_yearly_rate_3 = ''
                emp.usc_yearly_rate_4 = ''
                emp.yearly_standard_tax = ''
                emp.yearly_top_tax = ''
                emp.prsi_exempt = ''
                emp.yearly_tax_credits = ''
                emp.yearly_rate_cut_off = ''
                emp.prsi_class = ''



class HrEmployeeRPN(models.Model):
    _name = 'hr.employee.rpn'
    _order = 'id desc'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    effective_date = fields.Date('Effective Date')
    end_date = fields.Date('end Date')
    usc_yearly_cut_off_1 = fields.Float('USC yearly cut off 1')
    usc_yearly_cut_off_2 = fields.Float('USC yearly cut off 2')
    usc_yearly_cut_off_3 = fields.Float('USC yearly cut off 3')
    usc_yearly_cut_off_4 = fields.Float('USC yearly cut off 4')
    usc_yearly_rate_1 = fields.Float('USC Yearly Rate 1')
    usc_yearly_rate_2 = fields.Float('USC Yearly Rate 2')
    usc_yearly_rate_3 = fields.Float('USC Yearly Rate 3')
    usc_yearly_rate_4 = fields.Float('USC Yearly Rate 4')
    yearly_standard_tax = fields.Float('Standard Tax Rate')
    yearly_top_tax = fields.Float('Top Tax Rate')
    prsi_exempt = fields.Float('PRSI Exempt')
    yearly_tax_credits = fields.Float('Yearly Tax Credits')
    yearly_rate_cut_off = fields.Float('Yearly Rate Cut Off')
    prsi_class = fields.Char('PRSI Class')