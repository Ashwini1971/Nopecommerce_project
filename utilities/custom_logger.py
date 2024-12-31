import logging

class LogMaker:

    @staticmethod
    def log_gen():
        logging.basicConfig(filename=r'C:\Users\User\PycharmProjects\POMbasedProject\logs\nopcommerce.log',
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger



