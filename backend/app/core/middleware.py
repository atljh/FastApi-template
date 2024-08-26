from functools import wraps
from dependency_injector.wiring import inject as di_inject
from loguru import logger
from app.services.base_service import BaseService

def inject(func):
    @di_inject
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        injected_services = [arg for arg in kwargs.values() if isinstance(arg, BaseService)]
        if len(injected_services) == 0:
            return result
        else:
            try:
                service = injected_services[-1]
                if hasattr(service, 'close_scoped_session'):
                    service.close_scoped_session()
                else:
                    logger.warning(f"Service {service} does not have 'close_scoped_session' method")
            except Exception as e:
                logger.error(e)
        return result

    return wrapper
