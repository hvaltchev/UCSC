#!/usr/bin/env python3
"""Provides a FileLogger(file_name) context manager class, that logs the opening and closing of the file_name.
"""     

#!/usr/bin/env python
"""Provides FileLogger(file_name) context manager class.
"""
import context, datetime

class FileLogger(context.OpenClose):
    log_file_name = "file.log"
    
    def __enter__(self):
        self.logger_object = open(FileLogger.log_file_name, 'a')
        self.logger_object.write(f"""Opening "{self.file_name}" in mode '{self.mode}' on {datetime.datetime.now()}\n""")
        return context.OpenClose.__enter__(self)

    def __exit__(self,*args):
        self.logger_object.write(f'Closing "{self.file_name}" on {datetime.datetime.now()}\n\n')
        self.logger_object.close()
        context.OpenClose.__exit__(self, *args)    

def main():
    for loop in range(3):
        with FileLogger("words.txt", "a") as file_obj:
            file_obj.write("Writing some words at {}.\n".format(
                datetime.datetime.now()))
    print("words.text:")
    print(open("words.txt").read())
    print(FileLogger.log_file_name + ":")
    print(open(FileLogger.log_file_name).read())

main()                            
