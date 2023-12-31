from odoo import http
from odoo.http import request
import base64


class HomePageController(http.Controller):

    @http.route('/', type="http", auth='public', website=True)
    def user_authentication_form(self, **kw):
        return request.render('support_sys.homepage', {})

class ExpenseController(http.Controller):
    @http.route('/employee_expense', type="http", auth='public', website=True)
    def user_authentication_form(self, **kw):
        return request.render('support_sys.employee_expense', {})

    @http.route('/employee_history', type="http", auth='public', website=True)
    def list_tickets(self, **kwargs):
        expenses = request.env["employee.expense"].sudo().search([])

        data = []
        for expense in expenses:
            photo = expense.photo.decode('utf-8') if expense.photo else None
            data.append({
                'nepalidatepicker': expense.nepalidatepicker,
                'starting_location': expense.starting_location,
                'ending_location': expense.ending_location,
                'expense_category': expense.expense_category,
                'amount': expense.amount,
                'hotel_name': expense.hotel_name,
                'hotel_address': expense.hotel_address,
                'hotel_phone': expense.hotel_phone,
                'description': expense.description,
                'photo': photo,
            })
        return http.request.render(
            "support_sys.employee_history",
            {"records": data}
        )

    @http.route('/expense_form', type='http', auth='public', website=True)
    def authenticate_user(self, **post):
        nepalidatepicker = post.get('nepalidatepicker')
        starting_location = post.get('starting_location')
        ending_location = post.get('ending_location')
        expense_category = post.get('expense_category')
        amount = post.get('amount')
        photo = post.get('photo')
        description = post.get('description')
        hotel_name=post.get('hotel_name')
        hotel_address = post.get('hotel_address')
        hotel_phone = post.get('hotel_phone')

        if photo:
            # If a photo is uploaded, convert it to base64
            photo_base64 = base64.b64encode(photo.read())
        else:
            photo_base64 = None

        expense = request.env['employee.expense'].sudo().create({
            'nepalidatepicker': nepalidatepicker,
            'starting_location': starting_location,
            'ending_location': ending_location,
            'amount': amount,
            'photo': photo_base64,
            'expense_category': expense_category,
            'hotel_name': hotel_name,
            'hotel_address': hotel_address,
            'hotel_phone': hotel_phone,
            'description': description,

        })



        return request.redirect('/employee_history')
class EmployeeHistoryController(http.Controller):
    @http.route('/employee_history', type="http", auth='public', website=True)
    def user_authentication_form(self, **kw):
        return request.render('support_sys.employee_history', {})


class TicketController(http.Controller):
    @http.route('/ticket_history', type="http", auth='public', website=True)
    def list_tickets(self, **kwargs):
        tickets = request.env["ticket.raise"].sudo().search([])

        data = []
        for ticket in tickets:
            photo = ticket.photo.decode('utf-8') if ticket.photo else None
            data.append({
                'ticket_id': ticket.ticket_id,
                'ticket_type': ticket.ticket_type,
                'product': ticket.product,
                'priority': ticket.priority,
                'message': ticket.message,
                'nepalidatepicker': ticket.nepalidatepicker,
                'photo': photo,
            })
        return http.request.render(
            "support_sys.ticket_history",
            {"records": data}
        )

    @http.route('/ticket_raise', type='http', auth='public', website=True)
    def authenticate_user(self, **post):
        ticket_type = post.get('ticket_type')
        product = post.get('product')
        priority = post.get('priority')
        message = post.get('message')
        client_email = post.get('client_email')
        nepalidatepicker = post.get('nepalidatepicker')
        photo = post.get('photo')

        if photo:
            # If a photo is uploaded, convert it to base64
            photo_base64 = base64.b64encode(photo.read())
        else:
            photo_base64 = None

        ticket = request.env['ticket.raise'].sudo().create({
            'ticket_type': ticket_type,
            'product': product,
            'priority': priority,
            'message': message,
            'photo': photo_base64,
            'nepalidatepicker': nepalidatepicker,
            'client_email': client_email,  # Assign the client's email to the model's email field
        })

        # Send an email to the client
        if ticket:
            template = request.env.ref('support_sys.email_template_ticket_raise')
            if template:
                template.with_context(object=ticket).send_mail(ticket.id, force_send=True)

        # Redirect to the ticket view
        return request.redirect('/ticket_history')


class NewTicketController(http.Controller):
    @http.route('/new_ticket', type="http", auth='public', website=True)
    def user_authentication_form(self, **kw):
        return request.render('support_sys.new_ticket', {})
