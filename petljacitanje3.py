import sys
import time
import traceback
import nfc

clf = nfc.ContactlessFrontend()
clf.open('ttyAMA0')

try:
    # Should be defined in Python 3
    x = TimeoutError
except:
    # For Python 2
    class TimeoutError(Exception):
        def __init__(self, value="Timeout"):
            self.value = value

        def __str__(self):
            return repr(self.value)

class ExpectTimeout(object):
    def __init__(self, seconds, print_traceback=True, mute=False):
        self.seconds_before_timeout = seconds
        self.original_trace_function = None
        self.end_time = None
        self.print_traceback = print_traceback
        self.mute = mute

    # Tracing function
    def check_time(self, frame, event, arg):
        if self.original_trace_function is not None:
            self.original_trace_function(frame, event, arg)

        current_time = time.time()
        if current_time >= self.end_time:
            raise TimeoutError

        return self.check_time

    # Begin of `with` block
    def __enter__(self):
        start_time = time.time()
        self.end_time = start_time + self.seconds_before_timeout

        self.original_trace_function = sys.gettrace()
        sys.settrace(self.check_time)
        return self

    # End of `with` block
    def __exit__(self, exc_type, exc_value, tb):
        self.cancel()

        if exc_type is None:
            return

        # An exception occurred
        if self.print_traceback:
            lines = ''.join(
                traceback.format_exception(
                    exc_type,
                    exc_value,
                    tb)).strip()
        else:
            lines = traceback.format_exception_only(
                exc_type, exc_value)[-1].strip()

        if not self.mute:
            print("(expected)")
        return True  # Ignore it

    def cancel(self):
        sys.settrace(self.original_trace_function)

def main():
    try:
        while True:
            unos = ''
            print("Zelite pokusati citati? 1 - DA 3 - NE")
            
            while unos != 1 and unos != 3:

                unos = input()

                if unos == 1:
                    print("citanje")
                    userID = ''

                    with ExpectTimeout(5, print_traceback=False):
                        try:
                            userID = clf.connect(rdwr={'on-connect': lambda tag: False})
                            print(userID)
                            pass
                        except:
                            print("Nesto ne valja!")
                    break
                elif unos == 3:
                    print("nema citanja")
                    break
                else:
                    print("neispravan unos!")
                    pass
                pass
            pass
        pass
    except KeyboardInterrupt:
        print("Kraj rograma!")
        clf.close()
        pass

if __name__ == '__main__':
    main()