import logging
import traceback


logging.basicConfig(filename = 'log.log', level = logging.DEBUG, filemode = 'w',
                    format = '%(asctime)s %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p')


def return_errors_as_empty_string(func):
    logger = logging.getLogger('logger')

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            error_to_log = ' ERROR:\n'

            formatted_traceback = traceback.format_exc().splitlines()
            for trace in formatted_traceback[3:]:
                error_to_log += trace + '\n'

            logger.error(error_to_log)
            return ''

    return wrapper
