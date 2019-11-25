from WEDWorker import WEDWorkerTemplate
import sys,random

class t_extract_materials(WEDWorkerTemplate):
    
    #trname and dbs variables are static in order to conform with the definition of wed_trans()    
    trname = 't_extract_materials'
    dbs = 'user=organ_donation dbname=organ_donation application_name=t_extract_materials'
    wakeup_interval = 5
    
    def __init__(self):
        super().__init__(self.trname, self.dbs, self.wakeup_interval)
    
    # Compute the WED-transition and return a string as the new WED-state, using the SQL SET clause syntax 
    # Return None to abort transaction
    def wed_trans(self, wed_state, wid):
        print("\033[33m> Extractiong materials from body (Id = %d)\033[0m" % wid)
        print ("\033[33m> WED-state: %s\033[0m" % wed_state)
        
        #business logic goes here 
        
        return "material_extraction_status = 'Finalized'"
        
w = t_extract_materials()

try:
    w.run()
except KeyboardInterrupt:
    print()
    sys.exit(0)

