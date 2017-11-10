"""Order Model"""
from google.appengine.ext import ndb

from server.common.util import get_ancestor_key, parse_id, populate
import customer_model


class Order(ndb.Model):
    """The Order Model definition."""
    order_status = ndb.StringProperty()
    order_source = ndb.StringProperty()
    estimated_time = ndb.StringProperty()
    promo_ser_code = ndb.StringProperty()
    promo_ser_code_s = ndb.StringProperty()
    occasion = ndb.StringProperty()

    def as_dict(self):
        """Converts the datastore reponse into a JSON parsable dictionary."""
        return {
            'id': self.key.id(),
            'order_status': self.order_status,
            'order_source': self.order_source,
            'estimated_time': self.estimated_time,
            'promo_ser_code': self.promo_ser_code,
            'promo_ser_code_s': self.promo_ser_code_s,
            'occasion': self.occasion
        }


def all(customer_id):
    """Gets all the items for a resource."""
    customers = Order.query(ancestor=Customer.get_by_id(customer_id))
    return [customer.as_dict() for customer in customers]


def create(body, customer_id):
    """Creates a new record for the resource."""
    # First, get the parent customer.
    parent_key = get_ancestor_key()
    customer = customer_model.Customer.get_by_id(
        int(customer_id), parent=parent_key)

    # Create the order with the Customer as the parent.
    order = Order(parent=customer.key)
    order = populate(Order, order, body)
    order.put()
    return order.as_dict()
