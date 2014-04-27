from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=100, unique='True')

    def __unicode__(self):
        return self.country_name

class State(models.Model):
    state_name = models.CharField(max_length=100, unique='True')
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.state_name

class District(models.Model):
    district_name = models.CharField(max_length=100, unique='True')
    state = models.ForeignKey(State)

    def __unicode__(self):
        return self.district_name

class Block(models.Model):
    block_name = models.CharField(max_length=100, unique='True')
    district = models.ForeignKey(District)
    
    def __unicode__(self):
        return self.block_name

class Sublocation(models.Model):
    sublocation_name = models.CharField(max_length=100)
    block = models.ForeignKey(Block)
    class Meta:
        unique_together = ("sublocation_name","block")


class Village(models.Model):
    village_name = models.CharField(max_length=100)
    sublocation = models.ForeignKey(Sublocation)
    
    class Meta:
        unique_together = ("village_name","sublocation")

class Person(models.Model):
    person_name = models.CharField(max_length=100)
    spouse_name = models.CharField(max_length=100)
    job_card_number = models.CharField(max_length=100, blank=True)
    village = models.ForeignKey(Village)
    no_of_adults = models.IntegerField()
    no_of_children = models.IntegerField()
    house_hold_per_capita_income = models.IntegerField()
    date_of_entry = models.DateField()
    phone_no = models.CharField(max_length=100, blank=True)
    
    class Meta:
        unique_together = ("person_name", "spouse_name", "village")
        
### For SHG Level Data Capture

class Cluster(models.Model):
    cluster_name = models.CharField(max_length=100)
    village = models.ForeignKey(Village)
    
    class Meta:
        unique_together = ("cluster_name","village")


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    cluster = models.ForeignKey(Cluster)
    date_of_formation = models.DateField()
    share_holder_company_1 = models.CharField(max_length=100, blank = True)
    num_of_shares_company_1 = models.IntegerField(blank = True)
    share_value_company_1 = models.IntegerField(blank = True)
    share_holder_company_2 = models.CharField(max_length=100, blank = True)
    num_of_shares_company_1 = models.IntegerField(blank = True)
    share_value_company_1 = models.IntegerField(blank = True)
    share_holder_company_3 = models.CharField(max_length=100, blank = True)
    num_of_shares_company_3 = models.IntegerField(blank = True)
    share_value_company_3 = models.IntegerField(blank = True)
    
    class Meta:
        unique_together = ("group_name","cluster")

class SHGProgram(models.Model):
    person = models.ForeignKey(Person)
    loan_from_money_lenders = models.IntegerField()
    loan_from_kcc_or_mfis = models.IntegerField()
    
    
    
class AgricultureProgram(models.Model):
    person = models.ForeignKey(Person)
    total_land = models.IntegerField()
    irrigated_land = models.IntegerField()
    rainfed_land = models.IntegerField()
    fallow_land = models.IntegerField()
    IRRIGATION_CHOICES = (
                ('FarmPond','FarmPond'),
                ('BoreWell','Tuesday'),
                ('Well','Well'),
                ('River/CanalStream','River/CanalStream'),
                ('EarthenDam','EarthenDam'),
                  )
    irrigation_sources = models.CharField(max_length=50,choices=IRRIGATION_CHOICES)
    share_holder_company_1 = models.CharField(max_length=100, blank = True)
    num_of_shares_company_1 = models.IntegerField(blank = True)
    share_value_company_1 = models.IntegerField(blank = True)
    share_holder_company_2 = models.CharField(max_length=100, blank = True)
    num_of_shares_company_1 = models.IntegerField(blank = True)
    share_value_company_1 = models.IntegerField(blank = True)
    share_holder_company_3 = models.CharField(max_length=100, blank = True)
    num_of_shares_company_3 = models.IntegerField(blank = True)
    share_value_company_3 = models.IntegerField(blank = True)
    