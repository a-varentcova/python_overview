import logging

def main():

    FORMAT = '%(asctime)s:%(levelname)s - %(message)s'

    logging.basicConfig(
        filename = 'progress.log',
        level=logging.DEBUG,       # everythong above this level will be logged
        format=FORMAT,             # formats the log message
        filemode='w',              # rewrite every time as the program runs
        )

    # five default levels of logs:
    logging.debug("This is a debug message")
    logging.info("This is a info message")  
    logging.warning("This is a warning message")  
    logging.error("This is a error message")  
    logging.critical("This is a critical message")  

  
if __name__ == "__main__":
    main()
