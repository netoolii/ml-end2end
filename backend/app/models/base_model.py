class BaseModel():

    def to_json(self):
        attributes = vars(self)
        if attributes.get('password') is not None:
            attributes.pop('password')
        if attributes.get('_sa_instance_state') is not None:
            attributes.pop('_sa_instance_state')
        if attributes.get('created_at') is not None:
            attributes.pop('created_at')

        return attributes
