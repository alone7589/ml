import random,datetime

class DynamicPricing:
    def __init__(self,base):
        self.base=base

    def price(self,demand,supply,competitor):
        hour=datetime.datetime.now().hour

        demand_f=0.5*demand
        supply_f=0.4*supply
        time_f=0.2 if 18<=hour<=22 else 0.05

        price=self.base*(1+demand_f-supply_f+time_f)

        if price>competitor*1.05:
            price=competitor*1.05

        return round(price,2)

system=DynamicPricing(1000)

d=random.random()
s=random.random()
c=random.uniform(900,1200)

print(system.price(d,s,c))