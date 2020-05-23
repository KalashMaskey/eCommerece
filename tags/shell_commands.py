>>> from tags.models import Tag
>>> Tag.objects.all()
<QuerySet [<Tag: black>, <Tag: brown>, <Tag: PC>, <Tag: red>, <Tag: hat>, <Tag: desktop>]>
>>> Tag.objects.first()
<Tag: black>
>>> black.title
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'black' is not defined
>>> black=Tag.objects.first()

>>> black.title
'black'
>>> black.slug
'black'
>>> black.products
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x000001A05BFD6E50>
>>> black.products.all()
<ProductQuerySet [<Product: Shoes>, <Product: Cap>, <Product: Gloves>]>
>>> black.products.all().first()
<Product: Shoes>
>>> exit()
<Product: Shoes>
>>> shoes.title
'Shoes'
>>> shoes.description
'Premium built synthetic shoes'
>>> shoes.tags
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Product' object has no attribute 'tags'
>>> shoes.tag_set
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRel
atedManager object at 0x0000020E602B6D00>
>>> shoes.tag_set.all()
<QuerySet [<Tag: black>, <Tag: brown>, <Tag: red>]>
>>> shoes.tag_set.filter(title__iexact='black')
<QuerySet [<Tag: black>]>
>>> shoes.tag
