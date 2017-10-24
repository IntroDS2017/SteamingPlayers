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
    points.plot(ax=base, color='red', marker='*', zorder=3, markersize=1.5)

    points.apply(lambda x: draw_point(x, base), axis=1)

    x1, x2, y1, y2 = plt.axis()

    # whole map
    base.set_xlim([x1, x2])
    base.set_ylim([6670000, 6687500])

    # central
    # base.set_xlim([5000+2.549e7, 8000+2.549e7])
    # base.set_ylim([6671000, 6674000])

    base.set_axis_off()

    if show_names:
        points.apply(lambda x: annotate_point(x, base), axis=1)

    added.clear()


def draw_point(row, ax):
    marker_size = row['Accidents per Traffic sum'] * 10000
    ax.plot(row.geometry.x, row.geometry.y, 'o', markersize=marker_size, markerfacecolor=(1, 1, 0, 0.5))


def annotate_point(row, ax):
    if row.nimi not in added:
        ax.annotate(row.nimi, xy=(row.geometry.x, row.geometry.y))
        added.append(row.nimi)
        

def usage_df_to_gpd(path):
    df = pd.read_csv(path)

    coord = df[['piste', 'x_gk25', 'y_gk25', 'nimi']].drop_duplicates().reset_index()

    geometry = [Point(xy) for xy in zip(coord.x_gk25, coord.y_gk25)]
    coord.drop(['x_gk25', 'y_gk25'], axis=1)
    crs = {'init': 'epsg:3879'}

    return GeoDataFrame(coord, crs=crs, geometry=geometry)


def get_accident_ratio(path):
    df = pd.read_csv(path)
    return df[['piste', 'Accidents per Traffic']]


def combine_ratio_and_usage(usage_path, accident_ratio_path):
    usage_gdp = usage_df_to_gpd(usage_path)
    accident_ratio_df = get_accident_ratio(accident_ratio_path)
    accident_ratio_sum_df = accident_ratio_df.groupby('piste')\
        .agg({'Accidents per Traffic': 'sum'})\
        .reset_index()\
        .rename(columns={'Accidents per Traffic': 'Accidents per Traffic sum'})\

    combined_gdp = usage_gdp.merge(accident_ratio_sum_df, on='piste')

    return combined_gdp.sort_values('Accidents per Traffic sum', ascending=False)


def main():
    usage_load_path = './data/4_road_usages.csv'
    accident_ratio_path = './data/8_accident_ratio.csv'

    points_and_accident_ratio_sum = combine_ratio_and_usage(usage_load_path, accident_ratio_path)

    gpd_dict = read_em()
    gpd_dict['points'] = points_and_accident_ratio_sum

    plot_em(gpd_dict)

    # plt.savefig('./data/figures/5_measurement_points.png'
    #             , format='png', bbox_inches='tight', dpi=500)
    plt.show()

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())






