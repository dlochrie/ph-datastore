"""Order Controller"""
import json

from server.models import order_model
from server.controllers import base_controller as base


class All(base.BaseController):
    """All (Find All) handler."""

    def get(self, customer_id):
        """Gets a list of all items for this resource."""
        self.send_json(order_model.all(customer_id))


class Create(base.BaseController):
    """Create handler."""

    def post(self, customer_id):
        """Attempts to create an item."""
        request_body = json.loads(self.request.body)
        order = order_model.create(request_body, customer_id)
        self.send_json(order)
