"""Base Controller"""
import json
import webapp2
import google.auth.transport.requests
import google.oauth2.id_token
import requests_toolbelt.adapters.appengine

requests_toolbelt.adapters.appengine.monkeypatch()
HTTP_REQUEST = google.auth.transport.requests.Request()

HOSTS_ALLOWED = [
    'http://localhost:3000',
    'http://localhost:8080',
]


class BaseController(webapp2.RequestHandler):
    """The base controller for which all API controller's inherit."""

    def __init__(self, request, response):
        # See: http://webapp2.readthedocs.io/en/latest/guide/handlers.html#overriding-init
        # Set self.request, self.response and self.app.
        self.initialize(request, response)

        # Decorate headers for all requests except OPTIONS.
        self.decorate_headers()

    def decorate_headers(self):
        """Decorates the headers for a request."""
        # Prevent non-authorized apps from making requests to this server.
        headers = self.request.headers
        origin = headers.get('Origin')
        if origin in HOSTS_ALLOWED:
            self.response.headers.add_header(
                'Access-Control-Allow-Origin', origin)

        # Override the rest of the headers.
        self.response.headers.add_header(
            'Access-Control-Allow-Headers',
            'Origin, X-Requested-With, Content-Type, Accept, Authorization')
        self.response.headers.add_header(
            'Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')

    def dispatch(self):
        """Middleware for all the routes."""
        # Add any middleware here...
        super(BaseController, self).dispatch()

    def options(self, *args, **kwarg):
        """
        Send an OPTIONs response for pre-flight requests.
        Our __init__ method will decorate OPTIONS with the correct headers, so
        this method just needs to exist, and isn't required to do anything.
        """
        return True

    def send_json(self, data):
        """Respond with a JSON payload."""
        self.response.headers['content-type'] = 'text/plain'
        self.response.write(json.dumps(data))

    def send_not_found(self):
        """Respond with 404 (Not Found)."""
        self.response.set_status(404)

    def send_ok(self):
        """Respond with 200 (OK)."""
        self.response.set_status(200)
        self.response.write('Ok')

    def send_unauthorized(self):
        """Responnd with 401 (Unauthorized)."""
        self.response.set_status(401)
        self.response.write('Unauthorized')
