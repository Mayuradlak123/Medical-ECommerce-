from neomodel import StructuredNode, StringProperty, RelationshipTo, PositiveIntegerProperty, RelationshipFrom
from django.conf import settings

class UserNode(StructuredNode):
    username = StringProperty(unique_index=True)
    first_name = StringProperty()
    last_name = StringProperty()

class UserProfileNode(StructuredNode):
    gender = StringProperty(choices=["Male", "Female", "Prefer not to say"], required=False)
    phone = PositiveIntegerProperty(verbose_name="Mobile Number", required=False)

    # Define relationships
    user = RelationshipTo(UserNode, 'HAS_PROFILE')

    def __str__(self):
        return f"{self.user.username} Profile"

    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

class SellerProfileNode(StructuredNode):
    store_name = StringProperty()
    address = StringProperty(max_length=40, required=False)
    pincode = PositiveIntegerProperty()

    # Define relationships
    user = RelationshipTo(UserNode, 'HAS_SELLER_PROFILE')

    def __str__(self):
        return f"Seller {self.user.username} Profile"
