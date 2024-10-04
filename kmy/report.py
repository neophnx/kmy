from xml.etree.ElementTree import Element

from .account_group import AccountGroup
from .dates import Dates
from .entity import Entity
from .container import Container


class Report(Entity):
    entity_name = "REPORT"

    def __init__(self) -> None:
        self.include_moving_average: str = ""
        self.include_schedules: str = ""
        self.row_type: str = ""
        self.detail: str = ""
        self.include_unused: str = ""
        self.neg_expenses: str = ""
        self.investments: str = ""
        self.id: str = ""
        self.data_major_tick: str = ""
        self.column_type: str = ""
        self.include_transfers: str = ""
        self.y_labels_precision: str = ""
        self.show_row_totals: str = ""
        self.log_y_axis: str = ""
        self.mixed_time: str = ""
        self.include_average_price: str = ""
        self.include_actuals: str = ""
        self.chart_line_width: str = ""
        self.data_minor_tick: str = ""
        self.chart_by_default: str = ""
        self.data_range_start: str = ""
        self.include_price: str = ""
        self.group: str = ""
        self.date_lock: str = ""
        self.chart_data_labels: str = ""
        self.chart_palette: str = ""
        self.chart_type: str = ""
        self.data_lock: str = ""
        self.columns_are_days: str = ""
        self.include_forecast: str = ""
        self.comment: str = ""
        self.show_column_totals: str = ""
        self.charts_v_grid_lines: str = ""
        self.type: str = ""
        self.favorite: str = ""
        self.convert_currency: str = ""
        self.skip_eero: str = ""
        self.name: str = ""
        self.chart_ch_grid_lines: str = ""
        self.data_range_end: str = ""

        self.account_groups: list[AccountGroup] = []
        self.dates: list[Dates] = []

    def init_from_xml(self, node: Element) -> None:
        self.include_moving_average = node.attrib.get("includesmovingaverage", "")
        self.include_schedules = node.attrib.get("includeschedules", "")
        self.row_type = node.attrib.get("", "")
        self.detail = node.attrib.get("", "")
        self.include_unused = node.attrib.get("", "")
        self.neg_expenses = node.attrib.get("", "")
        self.investments = node.attrib.get("", "")
        self.id = node.attrib.get("", "")
        self.data_major_tick = node.attrib.get("", "")
        self.column_type = node.attrib.get("", "")
        self.include_transfers = node.attrib.get("", "")
        self.y_labels_precision = node.attrib.get("", "")
        self.show_row_totals = node.attrib.get("", "")
        self.log_y_axis = node.attrib.get("", "")
        self.mixed_time = node.attrib.get("", "")
        self.include_average_price = node.attrib.get("", "")
        self.include_actuals = node.attrib.get("", "")
        self.chart_line_width = node.attrib.get("", "")
        self.data_minor_tick = node.attrib.get("", "")
        self.chart_by_default = node.attrib.get("", "")
        self.data_range_start = node.attrib.get("", "")
        self.include_price = node.attrib.get("", "")
        self.group = node.attrib.get("", "")
        self.date_lock = node.attrib.get("", "")
        self.chart_data_labels = node.attrib.get("", "")
        self.chart_palette = node.attrib.get("", "")
        self.chart_type = node.attrib.get("", "")
        self.data_lock = node.attrib.get("", "")
        self.columns_are_days = node.attrib.get("", "")
        self.include_forecast = node.attrib.get("", "")
        self.comment = node.attrib.get("", "")
        self.show_column_totals = node.attrib.get("", "")
        self.charts_v_grid_lines = node.attrib.get("", "")
        self.type = node.attrib.get("", "")
        self.favorite = node.attrib.get("", "")
        self.convert_currency = node.attrib.get("", "")
        self.skip_eero = node.attrib.get("", "")
        self.name = node.attrib.get("", "")
        self.chart_ch_grid_lines = node.attrib.get("", "")
        self.data_range_end = node.attrib.get("", "")

        for sub_node in node.findall(AccountGroup.entity_name):
            self.account_groups.append(AccountGroup.from_xml(sub_node))
        for sub_node in node.findall(Dates.entity_name):
            self.dates.append(Dates.from_xml(sub_node))

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.attrib["includesmovingaverage"] = self.include_moving_average
        node.attrib["includeschedules"] = self.include_schedules
        node.attrib["rowtype"] = self.row_type
        node.attrib["detail"] = self.detail
        node.attrib["includeunused"] = self.include_unused
        node.attrib["negexpenses"] = self.neg_expenses
        node.attrib["investments"] = self.investments
        node.attrib["id"] = self.id
        node.attrib["dataMajorTick"] = self.data_major_tick
        node.attrib["columntype"] = self.column_type
        node.attrib["includestransfers"] = self.include_transfers
        node.attrib["yLabelsPrecision"] = self.y_labels_precision
        node.attrib["showrowtotals"] = self.show_row_totals
        node.attrib["logYaxis"] = self.log_y_axis
        node.attrib["mixedtime"] = self.mixed_time
        node.attrib["includesaverageprice"] = self.include_average_price
        node.attrib["includesactuals"] = self.include_actuals
        node.attrib["chartlinewidth"] = self.chart_line_width
        node.attrib["dataMinorTick"] = self.data_minor_tick
        node.attrib["chartbydefault"] = self.chart_by_default
        node.attrib["dataRangeStart"] = self.data_range_start
        node.attrib["includesprice"] = self.include_price
        node.attrib["group"] = self.group
        node.attrib["datelock"] = self.date_lock
        node.attrib["chartdatalabels"] = self.chart_data_labels
        node.attrib["charttype"] = self.chart_type
        node.attrib["datalock"] = self.data_lock
        node.attrib["columnsaredays"] = self.columns_are_days
        node.attrib["includesforecast"] = self.include_forecast
        node.attrib["comment"] = self.comment
        node.attrib["showcolumntotals"] = self.show_column_totals
        node.attrib["chartsvgridlines"] = self.charts_v_grid_lines
        node.attrib["type"] = self.type
        node.attrib["favorite"] = self.favorite
        node.attrib["convertcurrency"] = self.convert_currency
        node.attrib["skipZero"] = self.skip_eero
        node.attrib["name"] = self.name
        node.attrib["chartbydefault"] = self.chart_by_default
        node.attrib["dataRangeEnd"] = self.data_range_end
        for account_group in self.account_groups:
            node.append(account_group.to_xml())
        for dates in self.dates:
            node.append(dates.to_xml())
        return node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id!r})"


class ReportContainer(Container[Report]):
    entity_name = "REPORTS"
    entity_class = Report
