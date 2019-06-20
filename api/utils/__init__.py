from api.utils.models import (UserDetails, MovieDetails, MovieCategory, 
                              FavouriteMovies, db)
from api.utils.cache import set_result_in_cache, get_data_from_cache
from api.utils.schemas import reg_schema, login_schema
from api.utils.auth import token_required
