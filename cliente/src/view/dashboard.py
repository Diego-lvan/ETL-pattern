##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: dashboard.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define los elementos visuales de la pantalla
#   del tablero
#
#-------------------------------------------------------------------------
from src.controller.dashboard_controller import DashboardController
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dcc, html
from dash.dependencies import Output, Input
from datetime import datetime

class Dashboard:

    def __init__(self):
        pass

    def document(self):
        return dbc.Container(
            fluid = True,
            children = [
                html.Br(),
                self._header_title("Sales Report"),
                html.Div(html.Hr()),
                self._header_subtitle("Sales summary financial report", "subtitle"),
                html.Br(),
                self._highlights_cards(),
                html.Div(html.Hr()),
                self._header_subtitle("Sales summary financial report filtered", "filtered-financial-report"),
                html.Br(),
                self._filtered_financial_report(),
                html.Br(),
                html.Div(html.Hr()),
                self._header_subtitle("Sold products by range time", "sold-products-report"),
                html.Br(),
                self._sold_products_report(),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._bar_chart_providers_by_location(),
                                    width=12
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._highlights_cards_4(),
                                    width=12
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._bar_chart_orders_per_location(),
                                    width=12
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._panel_best_sellers(),
                                    width=6
                                ),
                                dbc.Col(
                                    self._panel_worst_sales(),
                                    width=6
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._panel_most_selled_products(),
                                    width=12
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),



                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._panel_most_selled_products_2(),
                                    width=12
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),



            ]
        )
    


  






    def _header_title(self, title):
        return dbc.Row(
            [
                dbc.Col(html.H2(title, className="display-4"))
            ]
        )

    def _header_subtitle(self, subtitle, id):
        return html.Div(
            [
                html.P(
                    subtitle,
                    className="lead",
                ),
            ],
            id=id,
        )

    def _card_value(self, label, value, id):
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H2(value, className="card-title", id=id),
                    ]
                ),
                dbc.CardFooter(label),
            ]
        )

    def _highlights_cards(self):
        products = DashboardController.load_products()
        orders = DashboardController.load_orders()
        providers = DashboardController.load_providers()
        locations = DashboardController.load_locations()
        sales = DashboardController.load_sales()
        return html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            self._card_value("Products", products["products"], "products-value-full")
                        ),
                        dbc.Col(
                            self._card_value("Orders", orders["orders"], "orders-value-full")
                        ),
                        dbc.Col(
                            self._card_value("Providers", providers["providers"], "providers-value-full")
                        ),
                        dbc.Col(
                            self._card_value("Locations", locations["locations"], "locations-value-full")
                        ),
                        dbc.Col(
                            self._card_value("Sales", "$ {:,.2f}".format(float(sales['sales'])), "sales-value-full")
                        ),
                    ]
                ),
            ]
        )
    
    def _filtered_financial_report(self):
        products = DashboardController.load_products()
        orders = DashboardController.load_orders()
        providers = DashboardController.load_providers()
        locations = DashboardController.load_locations()
        sales = DashboardController.load_sales()
        return html.Div(
            [
                dbc.Row(
                    [
                        self._range_date_picker('start-date', '2024-04-01', datetime.now().strftime('%Y-%m-%d')),
                        
                    ]  
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            self._card_value("Products", products["products"], "products-value")
                        ),
                        dbc.Col(
                            self._card_value("Orders", orders["orders"], "orders-value")
                        ),
                        dbc.Col(
                            self._card_value("Providers", providers["providers"], "providers-value")
                        ),
                        dbc.Col(
                            self._card_value("Locations", locations["locations"], "locations-value")
                        ),
                        dbc.Col(
                            self._card_value("Sales", "$ {:,.2f}".format(float(sales['sales'])), "sales-value")
                        ),
                    ]
                ),
            ]
        )
        
    def _sold_products_report(self):
        products = DashboardController.load_products()
        return html.Div(
            [
                dbc.Row(
                    [
                        self._range_date_picker('sold-products-start-date', '2024-04-01', datetime.now().strftime('%Y-%m-%d')),
                    ]  
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            self._card_value("Products", products["products"], "sold-products-value")
                        )
                    ]
                ),
            ]
        )

    def _bar_chart_providers_by_location(self):
        data = DashboardController.load_providers_per_location()
        bar_char_fig = px.bar(data, x="location", y="providers")
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H3("Providers per location", className="card-title"),
                        dcc.Graph(
                            id='providers-per-location',
                            figure=bar_char_fig
                        ),
                    ]
                ),
            ]
        )
    
    def _highlights_cards_4(self):
        start_date = '2024-04-01'
        end_date = datetime.now().strftime('%Y-%m-%d')
        sales_locations = DashboardController.load_sales_per_location_by_period(start_date, end_date)
        locations = DashboardController.load_locations()
        sales = DashboardController.load_sales()
        ##id = 'start-date-2'
        
        ##date_picker = self._range_date_picker(id, start_date, end_date)
        bar_chart_sales_per_location = self._bar_chart_sales_per_location(start_date=start_date, end_date=end_date)
        return html.Div(
            [
                dbc.Row(
                    [
                        
                        bar_chart_sales_per_location,
                        ##date_picker,
                    ]
                ),

            ]
        )
    
    def _range_date_picker(self, id, start_date, end_date):
        return dbc.Form(
            [
                dbc.Label("Select a range time", style={"margin-right":"10px"}),
                dcc.DatePickerRange(
                    id=id,
                    start_date=start_date,
                    end_date=end_date,
                    display_format='YYYY-MM-DD'
                ),
            ]
        )
    

    def _bar_chart_sales_per_location(self, start_date, end_date):
        data = DashboardController.load_sales_per_location_by_period(start_date, end_date)
        id = 'start-date-2'
        date_picker = self._range_date_picker(id, start_date, end_date)
        bar_char_fig = px.bar(data, x="location", y="sales")
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H3("Sales per location", className="card-title"),
                        date_picker,
                        dcc.Graph(
                            id='sales-per-location-value',
                            figure=bar_char_fig
                        ),
                    ]
                ),
            ]
        )

    def _bar_chart_orders_per_location(self):
        data = DashboardController.load_orders_per_location()
        bar_char_fig = px.bar(data, x="location", y="orders")
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H3("Orders per location", className="card-title"),
                        dcc.Graph(
                            id='orders-per-location',
                            figure=bar_char_fig
                        ),
                    ]
                ),
            ]
        )

    def _panel_best_sellers(self):
        best_sellers = DashboardController.load_best_sellers()
        return html.Div(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H3("Best sellers", className="card-title"),
                                html.Br(),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                dbc.Row(
                                                    [
                                                        html.H5(f"- [{sale['invoice']}] $ {sale['total']:,.2f}", style={"font-weight":"bold"}),
                                                    ]
                                                ),
                                            ]
                                        )

                                        for sale in best_sellers
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def _panel_worst_sales(self):
        worst_sales = DashboardController.load_worst_sales()
        return html.Div(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H3("Worst sales", className="card-title"),
                                html.Br(),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                dbc.Row(
                                                    [
                                                        html.H5(f"- [{sale['invoice']}] $ {sale['total']:,.2f}", style={"font-weight":"bold"}),
                                                    ]
                                                ),
                                            ]
                                        )

                                        for sale in worst_sales
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def _panel_most_selled_products(self):
        most_selled = DashboardController.load_most_selled_products()
        return html.Div(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H3("Most selled", className="card-title"),
                                html.Br(),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                dbc.Row(
                                                    [
                                                        html.H5(f"- {product['product']} [{product['times']} time(s) sold]", style={"font-weight":"bold"}),
                                                    ]
                                                ),
                                            ]
                                        )

                                        for product in most_selled
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    

    def _panel_most_selled_products_2(self):
        return html.Div(
            [   
                dbc.Row(
                    [
                        dbc.Form(
                            [
                                dbc.Label("Start Date"),
                                dcc.DatePickerRange(
                                    id='start-date-3',
                                    start_date='2024-04-01',
                                    end_date=datetime.now().strftime('%Y-%m-%d'),
                                    display_format='YYYY-MM-DD'
                                ),
                            ]
                        ),
                        
                    ]  
                ),
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H3("Most selled", className="card-title"),
                                html.Br(),
                                html.Div(id="most_selled")
                            ]
                        )
                    ]
                )
            ]
        )