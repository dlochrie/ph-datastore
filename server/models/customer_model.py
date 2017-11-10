"""Customer Model"""
from google.appengine.ext import ndb

from server.common.util import parse_id, populate
from server.models.order_model import Order

NAMESPACE = 'staging'

# We set a parent key on each record to ensure that they are all
# in the same entity group. Queries across the single entity group
# will be consistent. However, the write rate should be limited to
# ~1/second.


def get_ancestor_key(namespace=NAMESPACE):
    """Constructs a Datastore key for a top-level entity.
    We use `namespace` as the key, it can be anything.
    """
    return ndb.Key('Namespace', namespace)


class Customer(ndb.Model):
    """The Customer Model definition."""
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
    phone = ndb.StringProperty()

    def as_dict(self, orders=[]):
        """Converts the datastore reponse into a JSON parsable dictionary."""
        return {
            'id': self.key.id(),
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'orders': orders
        }

    @property
    def orders(self):
        return Order.query(ancestor=self.key)


def all():
    """Gets all the items for a resource."""
    customers = Customer.query(ancestor=get_ancestor_key())

    # Loop through each customer. For each customer, fetch their orders.
    results = []
    for i, customer in enumerate(customers):
        orders = list(customer.orders.fetch())
        orders_dict = [order.as_dict() for order in orders]
        results.append(customer.as_dict(orders_dict))

    return results


def create(body):
    """Creates a new record for the resource."""
    customer = Customer(parent=get_ancestor_key())
    customer = populate(Customer, customer, body)
    customer.put()
    return customer.as_dict()
