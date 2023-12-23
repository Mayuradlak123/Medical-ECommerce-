from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, FloatProperty, IntegerProperty, UniqueIdProperty, BooleanProperty

class MedCatNode(StructuredNode):
    name = StringProperty(unique_index=True)

class MedicineNode(StructuredNode):
    name = StringProperty()
    price = FloatProperty()
    quantity = IntegerProperty()
    thumbnail = StringProperty()
    thumb_content_type = StringProperty(default='image/png')
    description = StringProperty()
    slug = StringProperty(unique_index=True)
    created_at = StringProperty()
    updated_at = StringProperty()
    is_active = BooleanProperty(default=True)

    # Define relationships
    belongs_to = RelationshipTo(MedCatNode, 'BELONGS_TO')
    owned_by = RelationshipFrom('UserNode', 'OWNS')

    def as_json(self):
        owner = 'Medstore'
        if self.owned_by.is_connected():
            owner = self.owned_by.single().store_name

        return {
            'id': self.id,
            'name': self.name,
            'category': self.belongs_to.single().name,
            'price': self.price,
            'quantity': self.quantity,
            'description': self.description,
            'owner': owner,
            'slug': self.slug,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'is_active': self.is_active
        }
