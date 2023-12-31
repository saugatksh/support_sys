from odoo import models, fields, api
from datetime import datetime


class support_sys(models.Model):
    _name = 'support_sys.support_sys'
    _description = 'support_sys.support_sys'

    c_id = fields.Integer(string='ID')
    name = fields.Char(string='Client Name')
    image = fields.Binary("Client Image")
    # message = fields.Text(string='Message', required=True)
    issue_description = fields.Char(string='Issued Description')
    support_type = fields.Selection([
        ('ordinary', 'Ordinary'),
        ('vip', 'VIP')
    ], string='Support Type', default='ordinary', help='Select the support type')
    assigned_employee = fields.Char(string='Name of Employee')
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ], string='Status', default='new')
    month_field = fields.Date(
        string='Date',
        widget='Date',
        help='Select a month',
        default=datetime.now().date()
    )


class Ticket(models.Model):
    _name = 'ticket.raise'
    _description = 'ticket'

    # name = fields.Char(string='Name')
    ticket_id = fields.Char(string='Ticket ID', required=True)
    ticket_type = fields.Selection(
        [('complain', 'Complain'), ('feedback', 'Feedback'), ('request', 'Request'), ('query', 'Query')],
        string='Choose a Ticket')
    product = fields.Selection([('Internet', 'Internet'), ('Software', 'Software'), ('Website', 'Website')
                                ],
                                string='Choose an Employer')
    priority = fields.Selection([('urgent', 'Urgent'), ('high', 'High'), ('medium','Medium'),('low', 'Low')], string='Choose a Priority')
    message = fields.Text(string='Message', required=True)
    client_email=fields.Char(string='Client Email', required=True)
    photo = fields.Binary(string='Photo')
    nepalidatepicker = fields.Date(string='Requested date', required=True)
    # attachment_filename = fields.Char(string='Attachment Filename')

    @api.model
    def create(self, vals):
        print("Sequence", vals)
        vals['ticket_id'] = self.env['ir.sequence'].next_by_code("ticket.raise")
        return super(Ticket, self).create(vals)



class Employee(models.Model):
    _name = 'employee.details'
    _description = 'Employee Details'

    name = fields.Char(string='Name')


    # employee_id = fields.Char(string='Employee ID', required=True, copy=False, readonly=True, index=True,
    #                           default=lambda self: self.env['ir.sequence'].next_by_code(
    #                               'support_sys.employee_sequence'))
    employee_id = fields.Char(string='Sequence Number')
    employee_name = fields.Char()
    contact = fields.Char()
    address = fields.Char()
    department = fields.Char()
    position = fields.Char()
    salary = fields.Integer()
    date_joined = fields.Date()




    _sql_constraints = [
        ('employee_id_uniq', 'unique(employee_id)', 'Employee ID must be unique!'),
    ]

    @api.model
    def create(self, vals):
        print("Sequence", vals)
        vals['employee_id'] = self.env['ir.sequence'].next_by_code("employee.details")
        return super(Employee, self).create(vals)

class Expense(models.Model):
    _name = 'employee.expense'
    _description = 'Expense'
    nepalidatepicker = fields.Date(string='Expense Date', default=fields.Date.today())
    amount = fields.Float(string='Amount')
    description = fields.Text(string='Description')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft')
    expense_category = fields.Selection([
        ('meals', 'Meals'),
        ('travel', 'Travel'),
        ('accommodation', 'Accommodation'),
        ('other', 'Other'),
    ], string='Expense Category')

    starting_location = fields.Char(string='Starting Location')
    ending_location = fields.Char(string='Ending Location')
    photo = fields.Binary("Bill Image")
    hotel_name = fields.Char("Hotel Name")
    hotel_address = fields.Char("Hotel")
    hotel_phone = fields.Char("Hotel")

    def submit_ticket(self):
        # Add logic to handle ticket submission
        # You can process the form data and perform any necessary actions here
        return {'type': 'ir.actions.act_window_close'}

