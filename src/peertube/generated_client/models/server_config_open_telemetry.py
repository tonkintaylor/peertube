from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.server_config_open_telemetry_metrics import ServerConfigOpenTelemetryMetrics





T = TypeVar("T", bound="ServerConfigOpenTelemetry")



@_attrs_define
class ServerConfigOpenTelemetry:
    """ PeerTube >= 6.1

        Attributes:
            metrics (Union[Unset, ServerConfigOpenTelemetryMetrics]):
     """

    metrics: Union[Unset, 'ServerConfigOpenTelemetryMetrics'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_config_open_telemetry_metrics import ServerConfigOpenTelemetryMetrics
        metrics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_config_open_telemetry_metrics import ServerConfigOpenTelemetryMetrics
        d = dict(src_dict)
        _metrics = d.pop("metrics", UNSET)
        metrics: Union[Unset, ServerConfigOpenTelemetryMetrics]
        if isinstance(_metrics,  Unset):
            metrics = UNSET
        else:
            metrics = ServerConfigOpenTelemetryMetrics.from_dict(_metrics)




        server_config_open_telemetry = cls(
            metrics=metrics,
        )


        server_config_open_telemetry.additional_properties = d
        return server_config_open_telemetry

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
