from gymhero.crud.base import CRUDRepository
from gymhero.log import get_logger
from gymhero.models.exercise import Exercise

log = get_logger(__name__)


exercise_crud = CRUDRepository(model=Exercise)
