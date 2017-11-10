def parse_id(data):
    """Parses the ID from the RESTFul URL string."""
    try:
        # IDs that come from REST might be strings, so they are coerced
        # into integers (which the model requires).
        parse_id = int(data['id'])
    except ValueError:
        parse_id = None

    return parse_id


def populate(model, instance, data):
    """
    Validate each attribute, checking if the model has that attribute
    (we don't want to populate user-defined attributes that the model does
    not have).
    Also validate if there is data for a particular attribute.
    NOTE: We do NOT populate the "id", since this is a special NDB attribute.
    """
    for attr in data:
        if hasattr(model, attr) and data[attr] and attr != 'id':
            setattr(instance, attr, data[attr])

    return instance
