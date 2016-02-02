class Sample:
    def __init__(self, msg):
        self.msg = msg
    def __enter__(self):
        return self
    def __exit__(self,type ,value ,tb):
        print type,"_",value,"_",tb
        print "Sayonara"
        print "done with context"


class Context_test:
    def sample_testing(self):
        try:
            with Sample('Hello') as sam:
                raise Exception
                print sam.msg
        except Exception as err:
            pass


Context_test().sample_testing()
