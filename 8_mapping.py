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


def plot_em(gpd_dict, show_names=False):
    base = gpd_dict['city'].plot(color='gray', edgecolor='white', linewidth=1.0, zorder=0)
    gpd_dict['moottori'].plot(ax=base, color='black', linewidth=1.0, markersize=1, zorder=1)
    gpd_dict['alu_kok'].plot(ax=base, color='cyan', linewidth=0.5, markersize=0.5, zorder=1)
    gpd_dict['kokooja'].plot(ax=base, color='orange', linewidth=0.9, markersize=0.9, zorder=1)
    gpd_dict['paa'].plot(ax=base, color='blue', linewidth=0.6, markersize=0.6, zorder=1)
    gpd_dict['asunto'].plot(ax=base, color='yellow', linewidth=0.2, markersize=0.2, zorder=1)

    points = gpd_dict['points']
    point_ax = points.plot(ax=base, color='red', marker='*', zorder=2, markersize=1.5)

    x1, x2, y1, y2 = plt.axis()

    point_ax.set_xlim([x1, x2])
    point_ax.set_ylim([6670000, 6687500])

    point_ax.set_axis_off()

    if show_names:
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

    plt.savefig('./data/figures/4_measurement_points.png', format='png', bbox_inches='tight', dpi=500)
    plt.show()





