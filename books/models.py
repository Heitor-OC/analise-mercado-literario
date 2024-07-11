from mongoengine import Document, StringField, FloatField, URLField, ReferenceField, CASCADE

class Category(Document):
    name = StringField(max_length=100, required=True)

    def __str__(self):
        return self.name

class Book(Document):
    category = ReferenceField(Category, reverse_delete_rule=CASCADE)
    title = StringField(max_length=200, required=True)
    old_price = FloatField(null=True, blank=True)
    new_price = FloatField(required=True)
    image_url = URLField(null=True, blank=True)

    def __str__(self):
        return self.title
