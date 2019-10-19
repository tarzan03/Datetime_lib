from datetime import tzinfo, timedelta, datetime
import pytz

class dtdtail():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def locltm():
        tm = datetime.now()
        return print(tm)
    
    def utctm():
        tn = datetime.utcnow()
        return print(tn)
        
    def crntdy(self):
        cd = datetime.today()
        return cd
        
    def day(self):
        dt = datetime(self.x,self.y,self.z)
        print('{}-{}-{} \nDay-{}'.format(dt.strftime('%b'), dt.strftime('%d'),dt.strftime('%Y'), dt.strftime('%a')))
        
    
    def leap(self):
        if self.x%4 == 0 and self.x%100 == 0:
            if self.x%400 == 0:
                print('{} is a leap year.'.format(self.x))
                
        elif self.x%4 == 0 and self.x%100 != 0:
            print('{} is a leap year.'.format(self.x))
    
        else:
            print('{} is not a leap year.'.format(self.x))
            
            
    def is_dst(self, dt=None, timezone="UTC"):
        if dt is None:
            dt = datetime.utcnow()
        timezone = pytz.timezone(timezone)
        timezone_aware_date = timezone.localize(dt, is_dst=None)
        return timezone_aware_date.tzinfo._dst.seconds != 0
            
   
