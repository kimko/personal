from tortoise import fields, models


class Resume(models.Model):
    title = fields.TextField()
    shortDescription = fields.TextField()
    name = fields.TextField()
    email = fields.TextField()
    phone = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url
