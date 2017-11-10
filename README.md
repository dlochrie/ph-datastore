# PH Datastore Proof of Concept

Basic app using Google App Engine and Google Datastore.

## Install

Install the Google Cloud SDK and the dependencies for the Python App Engine.
See [here](https://cloud.google.com/appengine/docs/standard/python/download) for
docs.

When you have the required Cloud components, you can do:

```
pip install -r server/requirements.txt -t lib
```

~OR~

```
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r server/requirements.txt -t lib
```

## Running

1. Start the local GAE server: `dev_appserver.py app.yaml`

The app server runs at localhost:8080.

| Request Type | Request URL | Sample Body |
| ------------ | ----------- | ----------- |
| Get all customers | GET localhost:8080/customers | N/A |
| Add a new customer | POST localhost:8080/customers/create | See `Sample Customer` below. |
| Get all orders for a customer | GET localhost:8080/orders/:customerID | N/A |
| Add a new order for a customer | POST localhost:8080/orders/:customerID/create | See `Sample Order` below. |

Sample Customer:

    {
      "first_name": "Daniel",
      "last_name": "Lochrie",
      "email": "daniel.lochrie@yum.com",
      "phone": "888.222.2525"
    }

Sample Order:

    {
      "order_status": "RECEIVED",
      "order_source": "OrderSource",
      "estimated_time": "20",
      "promo_ser_code": "PromoSerCode",
      "promo_ser_code_s": "PromoSerCodeS",
      "occasion": "1"
    }
