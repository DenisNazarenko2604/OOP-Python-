import logging
from datetime import date

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s: %(message)s')

logger = logging.getLogger(__name__)
today_str = date.today().strftime('%Y-%m-%d')
logger.info(f"Поточна дата: {today_str}")