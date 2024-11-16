from litestar import Response, get, status_codes


@get('/health/')
async def health() -> Response:
    return Response(content={}, status_code=status_codes.HTTP_200_OK)


routes = [health]
