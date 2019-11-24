from WEDWorker import WEDWorkerTemplate
import sys,random,time,keys

class t_reserve_hotel(WEDWorkerTemplate):
    
    #trname and dbs variables are static in order to conform with the definition of wed_trans()    
    trname = 't_reserve_hotel'
    dbs = 'user={name} dbname={name} application_name=t_reserve_hotel'.format(name = keys.dict['wed-flow-name'])
    wakeup_interval = 5
    
    def __init__(self):
        super().__init__(self.trname, self.dbs, self.wakeup_interval)
    
    # Compute the WED-transition and return a string as the new WED-state, using the SQL SET clause syntax 
    # Return None to abort transaction
    def wed_trans(self, wed_state, wid):
        print("\033[33m> Reserving hotel (Id = %d)\033[0m" % wid)
        print ("\033[33m> WED-state: %s\033[0m" % wed_state)
        
        #business logic goes here 
        #time.sleep(300)
        return "hotel_status = 'Reserved'"
        
w = t_reserve_hotel()

try:
    w.run()
except KeyboardInterrupt:
    print()
    sys.exit(0)

