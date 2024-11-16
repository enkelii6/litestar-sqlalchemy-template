import uvicorn
from litestar import Litestar
from litestar.plugins.sqlalchemy import SQLAlchemyAsyncConfig, SQLAlchemyInitPlugin

from src.config import settings
from src.routes import routes

db_config = SQLAlchemyAsyncConfig(connection_string=str(settings.database_url))

app = Litestar(
    route_handlers=routes,
    plugins=[SQLAlchemyInitPlugin(config=db_config)],
    debug=True,
)


if __name__ == '__main__':
    uvicorn.run('src.app:app', host='0.0.0.0', port=8000, reload=True)
