import webapp2

from server.controllers import customer_controller, order_controller

APP = webapp2.WSGIApplication([
    ('/customers', customer_controller.All),
    ('/customers/create', customer_controller.Create),
    ('/orders/(\d+)', order_controller.All),
    ('/orders/(\d+)/create', order_controller.Create),
], debug=True)
