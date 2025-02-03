import pytest
import json
from kundo_movies.routers.details import details
from fastapi.responses import JSONResponse


@pytest.mark.asyncio
async def test_detailed_query():
    """
    Testing to make a detailed query search
    :return:
    """
    response = await details("Memento")  # type: JSONResponse
    assert response.status_code == 200
    assert response.content == "test"
