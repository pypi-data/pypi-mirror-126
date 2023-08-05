import json
import os
import sys
import time
from functools import reduce
from operator import add
from typing import List, Union

import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Kline, Line

sys.path.append(os.path.dirname(__file__) + os.sep + '../')
try:
    from ..data.Stock import StockData
    from ..log.log import hide, progress_bar, show, slog, sprint
except:
    from data.Stock import StockData
    from log.log import hide, progress_bar, show, slog, sprint


def calculate_ma(day_count: int, data):
    result: List[Union[float, str]] = []
    for i in range(len(data["values"])):
        if i < day_count:
            result.append("-")
            continue
        sum_total = 0.0
        for j in range(day_count):
            sum_total += float(data["values"][i - j][1])
        result.append(abs(float("%.2f" % (sum_total / day_count))))
    return result


class SyntheticIndex(object):

    def __init__(self, weights={'贵州茅台': 0.5,
                                '隆基股份': 0.2,
                                '五粮液': 0.3},
                 ):
        self.names = list(weights.keys())
        self.weights = list(weights.values())
        self.lens = len(self.names)

    def stock_weights(self):
        return dict(zip(self.names, [i/sum(self.weights) for i in self.weights]))

    def stock_data(self):
        global StockData
        StockData = StockData(names=self.names)
        StockData.start_date = sorted([i['ipoDate'] for i in StockData.stocks_info().values()])[-1]
        StockData.end_date = time.strftime("%Y-%m-%d", time.localtime())        
        return StockData.stocks_data()[['name', 'date', 'open', 'close', 'low', 'high', 'volume']]

    def split_data(self, data):
        category_data = []
        values = []
        volumes = []
        for i, tick in enumerate(data):
            category_data.append(tick[0])
            values.append(tick)
            volumes.append([i, tick[4], 1 if tick[1] > tick[2] else -1])
        return {"categoryData": category_data, "values": values, "volumes": volumes}

    def get_data(self):
        data = self.stock_data()
        data['weight'] = data['name'].map(self.stock_weights())
        data['real_weight'] = data.weight/data.open
        date = data.date.unique()
        x = [list(data[data.date == i].real_weight /
                  data[data.date == i].real_weight.sum()) for i in date]
        data = data.sort_values(by=['date', 'name'])
        data['z_weight'] = reduce(add, tuple(x))
        data.date = data.date.astype(str)
        data.open = (data.open*data.z_weight).map(lambda x: round(x, 2))
        data.close = (data.close*data.z_weight).map(lambda x: round(x, 2))
        data.low = (data.low*data.z_weight).map(lambda x: round(x, 2))
        data.high = (data.high*data.z_weight).map(lambda x: round(x, 2))
        data.volume = (data.volume*data.z_weight).map(lambda x: round(x, 0))
        data = data.groupby('date').sum()
        data['date'] = data.index
        json_data = data[['date', 'open', 'close',
                          'low', 'high', 'volume']].values.tolist()
        return self.split_data(data=json_data)

    def draw_charts(self):
        chart_data = self.get_data()
        kline_data = [data[1:-1] for data in chart_data["values"]]
        kline = (
            Kline()
            .add_xaxis(xaxis_data=chart_data["categoryData"])
            .add_yaxis(
                series_name="portfolio index",
                y_axis=kline_data,
                itemstyle_opts=opts.ItemStyleOpts(
                    color="#ec0000", color0="#00da3c"),
            )
            .set_global_opts(
                legend_opts=opts.LegendOpts(
                    is_show=False, pos_bottom=10, pos_left="center"
                ),
                datazoom_opts=[
                    opts.DataZoomOpts(
                        is_show=False,
                        type_="inside",
                        xaxis_index=[0, 1],
                        range_start=98,
                        range_end=100,
                    ),
                    opts.DataZoomOpts(
                        is_show=True,
                        xaxis_index=[0, 1],
                        type_="slider",
                        pos_top="85%",
                        range_start=98,
                        range_end=100,
                    ),
                ],
                yaxis_opts=opts.AxisOpts(
                    is_scale=True,
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                ),
                tooltip_opts=opts.TooltipOpts(
                    trigger="axis",
                    axis_pointer_type="cross",
                    background_color="rgba(245, 245, 245, 0.8)",
                    border_width=1,
                    border_color="#ccc",
                    textstyle_opts=opts.TextStyleOpts(color="#000"),
                ),
                visualmap_opts=opts.VisualMapOpts(
                    is_show=False,
                    dimension=2,
                    series_index=5,
                    is_piecewise=True,
                    pieces=[
                        {"value": 1, "color": "#00da3c"},
                        {"value": -1, "color": "#ec0000"},
                    ],
                ),
                axispointer_opts=opts.AxisPointerOpts(
                    is_show=True,
                    link=[{"xAxisIndex": "all"}],
                    label=opts.LabelOpts(background_color="#777"),
                ),
                brush_opts=opts.BrushOpts(
                    x_axis_index="all",
                    brush_link="all",
                    out_of_brush={"colorAlpha": 0.1},
                    brush_type="lineX",
                ),
            )
        )

        line = (
            Line()
            .add_xaxis(xaxis_data=chart_data["categoryData"])
            .add_yaxis(
                series_name="MA5",
                y_axis=calculate_ma(day_count=5, data=chart_data),
                is_smooth=True,
                is_hover_animation=False,
                linestyle_opts=opts.LineStyleOpts(width=3, opacity=0.5),
                label_opts=opts.LabelOpts(is_show=False),
            )
            .add_yaxis(
                series_name="MA10",
                y_axis=calculate_ma(day_count=10, data=chart_data),
                is_smooth=True,
                is_hover_animation=False,
                linestyle_opts=opts.LineStyleOpts(width=3, opacity=0.5),
                label_opts=opts.LabelOpts(is_show=False),
            )
            .add_yaxis(
                series_name="MA20",
                y_axis=calculate_ma(day_count=20, data=chart_data),
                is_smooth=True,
                is_hover_animation=False,
                linestyle_opts=opts.LineStyleOpts(width=3, opacity=0.5),
                label_opts=opts.LabelOpts(is_show=False),
            )
            .add_yaxis(
                series_name="MA30",
                y_axis=calculate_ma(day_count=30, data=chart_data),
                is_smooth=True,
                is_hover_animation=False,
                linestyle_opts=opts.LineStyleOpts(width=3, opacity=0.5),
                label_opts=opts.LabelOpts(is_show=False),
            )
            .set_global_opts(xaxis_opts=opts.AxisOpts(type_="category"))
        )

        bar = (
            Bar()
            .add_xaxis(xaxis_data=chart_data["categoryData"])
            .add_yaxis(
                series_name="Volume",
                y_axis=chart_data["volumes"],
                xaxis_index=1,
                yaxis_index=1,
                label_opts=opts.LabelOpts(is_show=False),
            )
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    is_scale=True,
                    grid_index=1,
                    boundary_gap=False,
                    axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                    axistick_opts=opts.AxisTickOpts(is_show=False),
                    splitline_opts=opts.SplitLineOpts(is_show=False),
                    axislabel_opts=opts.LabelOpts(is_show=False),
                    split_number=20,
                    min_="dataMin",
                    max_="dataMax",
                ),
                yaxis_opts=opts.AxisOpts(
                    grid_index=1,
                    is_scale=True,
                    split_number=2,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                    axisline_opts=opts.AxisLineOpts(is_show=False),
                    axistick_opts=opts.AxisTickOpts(is_show=False),
                    splitline_opts=opts.SplitLineOpts(is_show=False),
                ),
                legend_opts=opts.LegendOpts(is_show=False),
            )
        )

        # Kline And Line
        overlap_kline_line = kline.overlap(line)

        # Grid Overlap + Bar
        grid_chart = Grid(
            init_opts=opts.InitOpts(
                width="1000px",
                height="800px",
                animation_opts=opts.AnimationOpts(animation=False),
            )
        )
        grid_chart.add(
            overlap_kline_line,
            grid_opts=opts.GridOpts(
                pos_left="10%", pos_right="8%", height="50%"),
        )
        grid_chart.add(
            bar,
            grid_opts=opts.GridOpts(
                pos_left="10%", pos_right="8%", pos_top="63%", height="16%"
            ),
        )

        grid_chart.render(f"kline_{str(self.names)}_index.html")


if __name__ == "__main__":
    si = SyntheticIndex()
    si.draw_charts()
