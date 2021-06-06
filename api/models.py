from django.db.models import Model, IntegerField, DateTimeField, BigIntegerField

# Create your models here.


class WateringSettings(Model):
    guild_id = BigIntegerField()
    interval = IntegerField(null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        db_table = 'watering_settings'
