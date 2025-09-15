from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.server_config_custom_import_videos_torrent import ServerConfigCustomImportVideosTorrent
  from ..models.server_config_custom_import_videos_http import ServerConfigCustomImportVideosHttp





T = TypeVar("T", bound="ServerConfigCustomImportVideos")



@_attrs_define
class ServerConfigCustomImportVideos:
    """ 
        Attributes:
            http (Union[Unset, ServerConfigCustomImportVideosHttp]):
            torrent (Union[Unset, ServerConfigCustomImportVideosTorrent]):
     """

    http: Union[Unset, 'ServerConfigCustomImportVideosHttp'] = UNSET
    torrent: Union[Unset, 'ServerConfigCustomImportVideosTorrent'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_config_custom_import_videos_torrent import ServerConfigCustomImportVideosTorrent
        from ..models.server_config_custom_import_videos_http import ServerConfigCustomImportVideosHttp
        http: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.http, Unset):
            http = self.http.to_dict()

        torrent: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.torrent, Unset):
            torrent = self.torrent.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if http is not UNSET:
            field_dict["http"] = http
        if torrent is not UNSET:
            field_dict["torrent"] = torrent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_config_custom_import_videos_torrent import ServerConfigCustomImportVideosTorrent
        from ..models.server_config_custom_import_videos_http import ServerConfigCustomImportVideosHttp
        d = dict(src_dict)
        _http = d.pop("http", UNSET)
        http: Union[Unset, ServerConfigCustomImportVideosHttp]
        if isinstance(_http,  Unset):
            http = UNSET
        else:
            http = ServerConfigCustomImportVideosHttp.from_dict(_http)




        _torrent = d.pop("torrent", UNSET)
        torrent: Union[Unset, ServerConfigCustomImportVideosTorrent]
        if isinstance(_torrent,  Unset):
            torrent = UNSET
        else:
            torrent = ServerConfigCustomImportVideosTorrent.from_dict(_torrent)




        server_config_custom_import_videos = cls(
            http=http,
            torrent=torrent,
        )


        server_config_custom_import_videos.additional_properties = d
        return server_config_custom_import_videos

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
