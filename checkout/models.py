from neomodel import StructuredNode, StringProperty, IntegerProperty, RelationshipTo

class UserNode(StructuredNode):
    # Assuming your User model is also converted to Neo4j
    # Add the necessary properties for the User model here
    pass

class BillingAddressNode(StructuredNode):
    user = RelationshipTo(UserNode, 'BELONGS_TO')
    address = StringProperty()
    pincode = IntegerProperty()
    city = StringProperty()
    landmark = StringProperty(null=True)

    def __str__(self):
        return f"{self.user.username} Billing Address"

    @property
    def as_json(self):
        return dict(address=self.address, pincode=self.pincode, city=self.city, landmark=self.landmark)
