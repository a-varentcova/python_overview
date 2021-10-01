import logging

def main():

    FORMAT = '%(asctime)s:%(name)s:%(levelname)s - %(message)s'
    LOGLEVEL = logging.DEBUG

    # 0
    # configure default root logger:
    logging.basicConfig(
        filename = 'progress_root.log',
        level=LOGLEVEL,       # everything above this level will be logged
        format=FORMAT,             # formats the log message
        filemode='w',              # rewrite every time as the program runs
        )


    # five default levels:
    logging.debug("This is a debug message")
    logging.info("This is a info message")  
    logging.warning("This is a warning message")  
    logging.error("This is a error message")  
    logging.critical("This is a critical message")  


    # 1
    # using specific logger is more flexible:
    logger = logging.getLogger(__name__)  # will get a name of the module where it's defined

    # configuring logger:

    # set level:
    logger.setLevel(logging.INFO)

    # set log file:
    # file_handler = logging.FileHandler('separate.log', mode='a')
    file_handler = logging.FileHandler('separate.log', mode='w')

    # set format:
    FORMAT = '%(asctime)s:%(name)s:inside %(funcName)s function:%(levelname)s - %(message)s'
    formatter = logging.Formatter(FORMAT)
    file_handler.setFormatter(formatter)

    # relate it to logger:
    logger.addHandler(file_handler)

    logger.debug("This is a debug message")
    logger.info("This is a info message")  
    logger.warning("This is a warning message")  
    logger.error("This is a error message")  
    logger.critical("This is a critical message") 



if __name__ == "__main__":
    main()
