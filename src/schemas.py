from litestar.plugins.sqlalchemy import SQLAlchemyDTO, SQLAlchemyDTOConfig


class ExcludeIdDTO(SQLAlchemyDTO):
    config = SQLAlchemyDTOConfig(exclude={'id'})


class ExcludeIdAndTimestampsDTO(SQLAlchemyDTO):
    config = SQLAlchemyDTOConfig(exclude={'id', 'created_at', 'updated_at'})
