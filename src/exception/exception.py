import sys

class customexception(Exception):

    def __init__(self, error_message, error_details:sys):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()
        print(exc_tb)

        self.lineno=exc_tb.tb_lineno
        self.filename=exc_tb.tb_frame.f_code.co_filename


    def __str__(self) -> str:
        self.filename, self.lineno, self.error_message
        return "Error occured in python script name [{0}] line number [{1}] error message[{2}]."
    
if __name__ == "__main__":
    try:
        raise customexception()
    except customexception as e:
        print(e)
