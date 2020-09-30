# (generated with --quick)

from typing import Any, NoReturn

GenericAPIView: Any
HttpResponse: Any
JsonResponse: Any
ParseError: Any
Report: Any
Response: Any
detail_route: Any
models: Any
projects: Any
regions: Any
reports: Any
scenarios: Any
viewsets: Any

class AttributeGroupViewset(Any):
    queryset: Any
    serializer_class: Any

class DeterministicTransitionViewset(Any):
    queryset: Any
    serializer_class: Any

class GenerateCSVReportView(ReportViewBase):
    def _response(self, report) -> Any: ...

class InitialConditionsNonSpatialDistributionViewset(Any):
    queryset: Any
    serializer_class: Any

class InitialConditionsNonSpatialViewset(Any):
    queryset: Any
    serializer_class: Any

class InitialConditionsSpatialViewset(Any):
    queryset: Any
    serializer_class: Any

class LibraryViewset(Any):
    queryset: Any
    serializer_class: Any

class ProjectViewset(Any):
    definitions: Any
    queryset: Any
    scenarios: Any
    serializer_class: Any

class RegionViewset(Any):
    queryset: Any
    reporting_units: Any
    serializer_class: Any

class ReportViewBase(Any):
    serializer_class: Any
    def _response(self, report) -> NoReturn: ...
    def post(self, request, *args, **kwargs) -> NoReturn: ...

class ReportingUnitViewset(Any):
    queryset: Any
    serializer_class: Any

class RequestPDFReportView(ReportViewBase):
    def _response(self, report) -> Any: ...

class RequestSpatialDataView(ReportViewBase):
    def _response(self, report) -> Any: ...

class ScenarioViewset(Any):
    config: Any
    library: Any
    project: Any
    queryset: Any
    reports: Any
    serializer_class: Any
    def get_queryset(self) -> Any: ...

class SecondaryStratumViewset(Any):
    queryset: Any
    serializer_class: Any

class StateAttributeSummaryReportViewset(Any):
    queryset: Any
    serializer_class: Any

class StateAttributeTypeViewset(Any):
    queryset: Any
    serializer_class: Any

class StateAttributeValueViewset(Any):
    queryset: Any
    serializer_class: Any

class StateClassSummaryReportViewset(Any):
    queryset: Any
    serializer_class: Any

class StateClassViewset(Any):
    queryset: Any
    serializer_class: Any

class StratumViewset(Any):
    queryset: Any
    serializer_class: Any
    def get_queryset(self) -> Any: ...

class TransitionAttributeSummaryReportViewset(Any):
    queryset: Any
    serializer_class: Any

class TransitionAttributeTargetViewset(Any):
    queryset: Any
    serializer_class: Any

class TransitionAttributeTypeViewset(Any):
    queryset: Any
    serializer_class: Any

class TransitionAttributeValueViewset(Any):
    queryset: Any
    serializer_class: Any

class TransitionByStateClassSummaryReportViewset(Any):
    queryset: Any
    serializer_class: Any

class TransitionGroupViewset(Any):
    queryset: Any
    serializer_class: Any
    types: Any

class TransitionMultiplierTypeViewset(Any):
    queryset: Any
    serializer_class: Any

class TransitionMultiplierValueViewset(Any):
    queryset: Any
    serializer_class: Any

class TransitionSizeDistributionViewset(Any):
    queryset: Any
    serializer_class: Any

class TransitionSizePrioritizationViewset(Any):
    queryset: Any
    serializer_class: Any

class TransitionSpatialMultiplierViewset(Any):
    queryset: Any
    serializer_class: Any

class TransitionSummaryReportViewset(Any):
    queryset: Any
    serializer_class: Any

class TransitionTargetViewset(Any):
    queryset: Any
    serializer_class: Any

class TransitionTypeGroupViewset(Any):
    queryset: Any
    serializer_class: Any

class TransitionTypeViewset(Any):
    groups: Any
    queryset: Any
    serializer_class: Any

class TransitionViewset(Any):
    queryset: Any
    serializer_class: Any
