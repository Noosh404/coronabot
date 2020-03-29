from pymodm import MongoModel, fields


class Corona(MongoModel):
    county = fields.CharField(primary_key=True)
    country = fields.CharField()
    date = fields.CharField(default=' ')
    infected = fields.IntegerField()
    deaths = fields.IntegerField()
    recovered = fields.IntegerField()

    def to_dict(self):
        corona_dict = self.to_son().to_dict()
        corona_dict['id'] = corona_dict['_id']
        del corona_dict['_id']
        del corona_dict['_cls']
        return corona_dict
