import logging

logging.basicConfig(
    level=logging.INFO,
    filename="simulation.log",
    filemode="w",
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)

# Декоратор логування помилок
def log_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Помилка у функції {func.__name__}: {type(e).__name__} – {e}")
            print(f"⚠ Помилка: {type(e).__name__}: {e}")
    return wrapper
