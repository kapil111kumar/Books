from tortoise import fields, models

class Book(models.Model):
    id = fields.IntField(primary_key=True)
    title = fields.CharField(max_length=255, unique=True)
    description = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.title
