from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from Richmond_Library_App.models import Book, Genre

book_index = Index('books')

@registry.register_document
class BookDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'books'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}
        
    class Django:
        model = Book # The model associated with this Document
        
        title = fields.TextField()
        author = fields.TextField()
        # isbn = fields.LongField()
        year = fields.Integer()
        publisher = fields.TextField()
        copies = fields.Integer()
        available = fields.Integer()
        
        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'title',
            'author',
            'publisher',
            'copies',
            'available',
        ]
        


@registry.register_document
class GenreDocument(Document):
    class Index:
        name = 'genre'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}
        
    class Django:
        model = Genre
        fields = [
            'genre_name',
            
        ]