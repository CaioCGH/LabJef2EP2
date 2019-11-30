from WEDWorker import WEDWorkerTemplate
import sys,random

class t_validate_projects(WEDWorkerTemplate):
    
    #trname and dbs variables are static in order to conform with the definition of wed_trans()    
    trname = 't_validate_projects'
    dbs = 'user=organ_donation dbname=organ_donation application_name=t_validate_projects'
    wakeup_interval = 5
    
    def __init__(self):
        super().__init__(self.trname, self.dbs, self.wakeup_interval)
    
    # Compute the WED-transition and return a string as the new WED-state, using the SQL SET clause syntax 
    # Return None to abort transaction
    def wed_trans(self, wed_state, wid):
        print("\033[33m> Validating projects (Id = %d)\033[0m" % wid)
        print ("\033[33m> WED-state: %s\033[0m" % wed_state)
        
        #business logic goes here 
        
        return "validation_status = 'Validated'"
        
w = t_validate_projects()

try:
    w.run()
except KeyboardInterrupt:
    print()
    sys.exit(0)

