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
import sys
import traceback

class CustomException(Exception):
    """
    Custom exception class that captures and formats exception details including
    the filename, line number, and error message.
    """

    def __init__(self, error_message):
        """
        Initialize the custom exception with an error message and automatically capture
        the current exception traceback information.
        """
        self.error_message = error_message
        
        # Capture the current exception's traceback details
        exc_type, exc_value, exc_tb = sys.exc_info()
        
        # Extract the last traceback object if it exists
        if exc_tb:
            self.lineno = exc_tb.tb_lineno
            self.filename = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = None
            self.filename = "Unknown"
        
        # Clean up the traceback to avoid circular references
        del exc_tb

    def __str__(self):
        """
        Format the string representation of the exception to provide detailed error info.
        """
        return f"Error occurred in Python script: [{self.filename}] at line number [{self.lineno}] with error message [{self.error_message}]."
