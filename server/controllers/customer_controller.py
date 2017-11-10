"""User Controller"""
import json

from server.models import customer_model
from server.controllers import base_controller as base


class All(base.BaseController):
    """All (Find All) handler."""

    def get(self):
        """Gets a list of all items for this resource."""
        self.send_json(customer_model.all())


class Create(base.BaseController):
    """Create handler."""

    def post(self):
        """Attempts to create an item."""
        request_body = json.loads(self.request.body)
        customer = customer_model.create(request_body)
        self.send_json(customer)
