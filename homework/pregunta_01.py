# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    if not os.path.exists('docs'):
        os.makedirs('docs')

    # se carga el archivo
    df = pd.read_csv('files/input/shipping-data.csv')

    visual_for_shipping_per_warehouse(df)
    visual_for_mode_of_shipment(df)
    visual_for_average_customer_rating(df)
    visual_for_weight_distribution(df)

    # se crea el archivo HTML

    with open('docs/index.html', 'w') as file:
        file.write(
            """
            <html>
            <head>
                <title>Shipping Dashboard</title>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css">
            </head>
            <body>
                <div class="container">
                    <div class="row">
                        <div class="col-6">
                            <img src="shipping_per_warehouse.png" class="img-fluid">
                        </div>
                        <div class="col-6">
                            <img src="mode_of_shipment.png" class="img-fluid">
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-6">
                            <img src="average_customer_rating.png" class="img-fluid">
                        </div>
                        <div class="col-6">
                            <img src="weight_distribution.png" class="img-fluid">
                        </div>
                    </div>
                </div>
            </body>
            </html>
            """
        )

    return None

def visual_for_shipping_per_warehouse(df):
    df = df.copy()
    df['Warehouse_block'].value_counts().plot(
        kind='bar',
        title = 'Shipping per Warehouse',
        xlabel = 'Warehouse Block',
        ylabel = 'Record count',
        color = 'tab:blue',
        fontsize = 8
    )
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    plt.savefig('docs/shipping_per_warehouse.png')
    return None


def visual_for_mode_of_shipment(df):
    df = df.copy()
    plt.figure()
    df['Mode_of_Shipment'].value_counts().plot.pie(
        title = 'Mode of Shipment',
        wedgeprops = dict(width=0.35),
        ylabel = '',
        colors = ['tab:blue', 'tab:orange', 'tab:green'],
    )
    plt.savefig('docs/mode_of_shipment.png')
    return None

def visual_for_average_customer_rating(df):
    df = df.copy()
    plt.figure()

    df = df[["Mode_of_Shipment",'Customer_rating']].groupby('Mode_of_Shipment').describe()
    df.columns = df.columns.droplevel()
    df = df[['mean', 'min', 'max']]

    plt.barh(
        y=df.index,
        width=df['max'].values - 1,
        left=df['min'].values,
        color='lightgreen',
        height=0.9,
        alpha=0.8, 
    )
    colors =[
        "tab:green" if value >= 3.0 else "tab:orange" for value in df['mean'].values
    ]
    plt.barh(
        y=df.index,
        width=df['mean'].values - 1,
        left=df['min'].values,
        color=colors,
        height=0.5,
        alpha=1.0,
    )

    plt.title('Average Customer Rating')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_color('gray')
    plt.gca().spines['bottom'].set_color('gray')

    plt.savefig('docs/average_customer_rating.png')
    return None

def visual_for_weight_distribution(df):
    df = df.copy()
    df['Weight_in_gms'].plot.hist(
        bins=20,
        title = 'Weight Distribution',
        xlabel = 'Weight (g)',
        ylabel = 'Record count',
        color = 'tab:orange',
        edgecolor = 'white',
    )
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig('docs/weight_distribution.png')
    return None

pregunta_01()
