from kmy.xml_storage.common.attribute.str_attribute import StrAttribute
from kmy.xml_storage.common.container import Container
from kmy.xml_storage.common.entity import Entity
from kmy.xml_storage.report.account_group import AccountGroupContainer
from kmy.xml_storage.report.dates import DatesContainer


class Report(Entity):
    entity_name = "REPORT"

    include_moving_average: StrAttribute = StrAttribute("includesmovingaverage")
    include_schedules: StrAttribute = StrAttribute("includeschedules")
    row_type: StrAttribute = StrAttribute("rowtype")
    detail: StrAttribute = StrAttribute("detail")
    include_unused: StrAttribute = StrAttribute("includeunused")
    neg_expenses: StrAttribute = StrAttribute("negexpenses")
    investments: StrAttribute = StrAttribute("investments")
    id: StrAttribute = StrAttribute("id")
    data_major_tick: StrAttribute = StrAttribute("dataMajorTick")
    column_type: StrAttribute = StrAttribute("columntype")
    include_transfers: StrAttribute = StrAttribute("includestransfers")
    y_labels_precision: StrAttribute = StrAttribute("yLabelsPrecision")
    show_row_totals: StrAttribute = StrAttribute("showrowtotals")
    log_y_axis: StrAttribute = StrAttribute("logYaxis")
    mixed_time: StrAttribute = StrAttribute("mixedtime")
    include_average_price: StrAttribute = StrAttribute("includesaverageprice")
    include_actuals: StrAttribute = StrAttribute("includesactuals")
    chart_line_width: StrAttribute = StrAttribute("chartlinewidth")
    data_minor_tick: StrAttribute = StrAttribute("dataMinorTick")
    chart_by_default: StrAttribute = StrAttribute("chartbydefault")
    data_range_start: StrAttribute = StrAttribute("dataRangeStart")
    include_price: StrAttribute = StrAttribute("includesprice")
    group: StrAttribute = StrAttribute("group")
    date_lock: StrAttribute = StrAttribute("datelock")
    chart_data_labels: StrAttribute = StrAttribute("chartdatalabels")
    chart_palette: StrAttribute = StrAttribute("chartpalette")
    chart_type: StrAttribute = StrAttribute("charttype")
    data_lock: StrAttribute = StrAttribute("datalock")
    columns_are_days: StrAttribute = StrAttribute("columnsaredays")
    include_forecast: StrAttribute = StrAttribute("includesforecast")
    comment: StrAttribute = StrAttribute("comment")
    show_column_totals: StrAttribute = StrAttribute("showcolumntotals")
    charts_v_grid_lines: StrAttribute = StrAttribute("chartsvgridlines")
    type: StrAttribute = StrAttribute("type")
    favorite: StrAttribute = StrAttribute("favorite")
    convert_currency: StrAttribute = StrAttribute("convertcurrency")
    skip_zero: StrAttribute = StrAttribute("skipZero")
    name: StrAttribute = StrAttribute("name")
    chart_ch_grid_lines: StrAttribute = StrAttribute("chartchgridlines")
    data_range_end: StrAttribute = StrAttribute("dataRangeEnd")

    account_groups: AccountGroupContainer
    dates = DatesContainer

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id!r})"


class ReportContainer(Container[Report]):
    entity_name = "REPORTS"
    entity_class = Report

    include_if_empty = True
