from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.server_config_views_views import ServerConfigViewsViews





T = TypeVar("T", bound="ServerConfigViews")



@_attrs_define
class ServerConfigViews:
    """ PeerTube >= 6.1

        Attributes:
            views (Union[Unset, ServerConfigViewsViews]):
     """

    views: Union[Unset, 'ServerConfigViewsViews'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_config_views_views import ServerConfigViewsViews
        views: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.views, Unset):
            views = self.views.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if views is not UNSET:
            field_dict["views"] = views

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_config_views_views import ServerConfigViewsViews
        d = dict(src_dict)
        _views = d.pop("views", UNSET)
        views: Union[Unset, ServerConfigViewsViews]
        if isinstance(_views,  Unset):
            views = UNSET
        else:
            views = ServerConfigViewsViews.from_dict(_views)




        server_config_views = cls(
            views=views,
        )


        server_config_views.additional_properties = d
        return server_config_views

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
