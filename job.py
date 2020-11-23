# Job: A process or task that has a priority.
# Your implementation should pass the tests in test_job.py.
# ERIN OCONNELL

class Job:

    def __init__(self, priority = None, message = None):
       self.priority = priority
       self.message = message      

    def __eq__(self, other):
        if self.priority == other.priority:
            return True
        else: 
            return False    

    def __lt__(self, other):
        return self.priority <= other.priority

    def __gt__(self, other):
        return self.priority > other.priority    
                    

