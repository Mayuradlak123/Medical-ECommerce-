from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, IntegerProperty, DateTimeProperty, BooleanProperty, FloatProperty, JSONProperty
from medicines.models import Medicine
from users.models import User  # Import User model from your app

class MedicineNode(StructuredNode):
    name = StringProperty()
    price = FloatProperty()
    # Add other properties as needed

class UserNode(StructuredNode):
    # Define properties for your UserNode
    pass

class CartItemNode(StructuredNode):
    quantity = IntegerProperty(default=1)
    created = DateTimeProperty(default_now=True)
    purchased = BooleanProperty(default=False)

    # Define relationships
    user = RelationshipFrom(UserNode, 'HAS_CART_ITEM')
    item = RelationshipTo(MedicineNode, 'HAS_MEDICINE')

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def total_amount(self):
        return float(self.quantity * self.item.price)

    @property
    def as_json(self):
        return {'id': self.id, 'quantity': self.quantity, 'total': self.total_amount()}

class OrderNode(StructuredNode):
    items = RelationshipTo(CartItemNode, 'HAS_CART_ITEM')
    user = RelationshipFrom(UserNode, 'HAS_ORDER')
    ordered = BooleanProperty(default=False)
    created = DateTimeProperty(default_now=True)
    orderID = StringProperty(null=True)
    paymentID = StringProperty(null=True)
    orderDate = DateTimeProperty(null=True, default_now=True)
    total = FloatProperty(default=0)
    postOrder = JSONProperty(null=True)

    def __str__(self):
        return f"Order of {self.order_total} by {self.user.username}"

    @property
    def order_total(self):
        if not self.ordered:
            return sum([item.total_amount() for item in self.items.all()])
        return self.total

    @property
    def as_json(self):
        if not self.ordered:
            return {item.item.name: item.as_json for item in self.items.all()}
        return json.loads(self.postOrder)

    def order_now(self):
        items = [item.as_json for item in self.items.all()]
        self.postOrder = json.dumps(items)
        self.total = sum([item.total_amount() for item in self.items.all()])
        self.save()
