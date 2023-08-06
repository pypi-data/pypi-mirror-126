from typing import Optional
from urllib.parse import urlencode
from .output.dataset_version_output import DatasetVersionOutput
from .output.paged_response import PagedResponse

from vectice.api.dataset import DatasetApi
from vectice.entity import DatasetVersion
from .json_object import JsonObject
from .Page import Page


class DatasetVersionApi(DatasetApi):
    def __init__(self, project_token: str, dataset_id: int, _token: Optional[str] = None):
        super().__init__(project_token=project_token, _token=_token)
        self._dataset_id = dataset_id
        self._dataset_version_path = super().api_base_path + "/" + str(dataset_id) + "/version"

    @property
    def dataset_id(self) -> int:
        return self._dataset_id

    @property
    def api_base_path(self) -> str:
        return self._dataset_version_path

    def list_dataset_versions(self, page_index=Page.index, page_size=Page.size) -> PagedResponse[DatasetVersionOutput]:
        queries = {"index": page_index, "size": page_size}
        dataset_versions = self._get(self.api_base_path + "?" + urlencode(queries))
        return PagedResponse(
            item_cls=DatasetVersionOutput,
            total=dataset_versions["total"],
            page=dataset_versions["page"],
            items=dataset_versions["items"],
        )

    def create_dataset_version(self, dataset_version: JsonObject) -> DatasetVersion:
        return DatasetVersion(self._post(self.api_base_path, dataset_version))

    def update_dataset_version(self, dataset_id: int, dataset_version) -> DatasetVersion:
        return DatasetVersion(self._put(self.api_base_path + "/" + str(dataset_id), dataset_version))
