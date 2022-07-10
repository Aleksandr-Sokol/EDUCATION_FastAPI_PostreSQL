from crud.base import CRUDBase
from database.models import Data


class DataCRUD(CRUDBase):
    model = Data
