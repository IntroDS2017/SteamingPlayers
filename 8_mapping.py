import geopandas         as gpd
import matplotlib.pyplot as plt
import pandas            as pd

from shapely.geometry import Point
from geopandas        import GeoDataFrame


def read_em():
    city = gpd.read_file('./stadi/kaupunginosat.dxf')
    moottori = gpd.read_file('./stadi/klinj_moottorivayla.dxf')
    alu_kok = gpd.read_file('./stadi/klinj_alu_kokoojakatu.dxf')
    kokooja = gpd.read_file('./stadi/klinj_paik_kokoojakatu.dxf')
    paa = gpd.read_file('./stadi/klinj_paakadut.dxf')
    asunto = gpd.read_file('./stadi/klinj_asuntokatu.dxf')

    return {'city': city, 'moottori': moottori, 'alu_kok': alu_kok, 'kokooja': kokooja, 'paa': paa, 'asunto': asunto}


added = []


def plot_em(gpd_dict):
    base = gpd_dict['city'].plot(color='gray', edgecolor='white')
    gpd_dict['moottori'].plot(ax=base, color='black')
    gpd_dict['alu_kok'].plot(ax=base, color='cyan')
    gpd_dict['kokooja'].plot(ax=base, color='orange')
    gpd_dict['paa'].plot(ax=base, color='blue')
    gpd_dict['asunto'].plot(ax=base, color='yellow')

    points = gpd_dict['points']
    point_ax = points.plot(ax=base, color='red', marker='*', zorder=2)

    gpd_dict['points'].apply(lambda x: annotate_point(x, point_ax), axis=1)
    added.clear()


def annotate_point(row, ax):
    if row.nimi not in added:
        ax.annotate(row.nimi, xy=(row.geometry.x, row.geometry.y), ha='center')
        added.append(row.nimi)
        

def usage_df_to_gpd(path):
    df = pd.read_csv(path)

    coord = df[['piste','x_gk25', 'y_gk25', 'aika', 'vuosi', 'nimi']]

    geometry = [Point(xy) for xy in zip(coord.x_gk25, coord.y_gk25)]
    coord.drop(['x_gk25', 'y_gk25'], axis=1)
    crs = {'init': 'epsg:3879'}

    return GeoDataFrame(coord, crs=crs, geometry=geometry)


if __name__ == '__main__':
    usage_load_path = './data/4_road_usages.csv'

    gpd_dict = read_em()
    gpd_dict['points'] = usage_df_to_gpd(usage_load_path)

    plot_em(gpd_dict)
    plt.show()




