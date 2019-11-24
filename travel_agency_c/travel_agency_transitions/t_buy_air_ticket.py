from WEDWorker import WEDWorkerTemplate
import sys,random,keys

class t_buy_air_ticket(WEDWorkerTemplate):
    
    #trname and dbs variables are static in order to conform with the definition of wed_trans()    
    trname = 't_buy_air_ticket'
    dbs = 'user={name} dbname={name} application_name=t_buy_air_ticket'.format(name = keys.dict['wed-flow-name'])
    wakeup_interval = 5
    
    def __init__(self):
        super().__init__(self.trname, self.dbs, self.wakeup_interval)
    
    # Compute the WED-transition and return a string as the new WED-state, using the SQL SET clause syntax 
    # Return None to abort transaction
    def wed_trans(self, wed_state, wid):
        print("\033[33m> Requesting air ticket (Id = %d)\033[0m" % wid)
        print ("\033[33m> WED-state: %s\033[0m" % wed_state)
        
        #business logic goes here 
        
        return "air_ticket_status = 'Purchased'"
        
w = t_buy_air_ticket()

try:
    w.run()
except KeyboardInterrupt:
    print()
    sys.exit(0)

