import matplotlib as mpl
from scipy import stats
mpl.use('Agg')
import matplotlib.pyplot as plt; plt
import seaborn as sns
import decimal

def simplify_borders(ax):
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.tick_params(direction='out')
delta = r'$\Delta$'
ylabel_dict = {}; ylim_dict = {}
ylabel_dict['mean_ratio_time_peak_to_dicrotic'] = '%ssec systolic peak / %ssec diastolic peak' % (
        delta, delta) 
ylabel_dict['mean_sec_start_to_peak'] = 'systolic peak onset (%ssec)' % (delta) 
ylabel_dict['systolic_to_diastolic'] = 'systolic to diastolic peak onset (%ssec)' % (delta) 
ylabel_dict['mean_sec_start_to_dicrotic'] = '%ssec diastolic peak onset' % (delta) 
ylabel_dict['std_ratio_amp_dicrotic'] = 'stdev %smmHg diastolic peak / %smmHg systolic peak' % (
        delta, delta) 
ylabel_dict['mean_width'] = 'mean pulse width (sec)'
ylim_dict['mean_ratio_time_peak_to_dicrotic'] = [0, 1]
#ylim_dict['mean_sec_start_to_dicrotic'] = [0, .4]
ylim_dict['mean_sec_start_to_peak'] = [0, .3]


def boxplot_by_category(full_df, category, variable, palette, output_path):

    plt.figure()
    ax = sns.boxplot(x=category, y=variable, data=full_df, width=.55, palette=palette)
    simplify_borders(ax)

    if category == 'age_category':
        ax.set(xticklabels=['Young', 'Old'])
    elif category == 'gender_binary':
        ax.set(xticklabels=['Female', 'Male'])

    set_axis_and_lim(ax, variable)

    ax.set_xlabel('')
    ax.set_xlim([-.5, 1.5])
    plt.tight_layout()
    plt.savefig(output_path + '%s_boxplot.png' % (variable), bbox_inches='tight')
    plt.close()

def set_axis_and_lim(ax, variable):
    try:
        ax.set_ylabel(ylabel_dict[variable], fontsize=15)
    except:
        pass

    try:
        ax.set_ylim(ylim_dict[variable])
    except:
        pass


def plot_linreg_for_age(properties_df, variable,  output_path, disease_category='all'):
    if disease_category is not "all":
        properties_df = properties_df[(properties_df.disease_category==disease_category)]
    x = properties_df['age_at_admission']
    plt.figure()
    y = properties_df[variable]
    ax = plt.subplot(111)
    ax.set_xlim([0, 80])
    sns.regplot(ax=ax, y=y, x=x, fit_reg=True, color=sns.xkcd_rgb['dark blue'], 
            scatter_kws={'alpha':0.5})
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    ax.set_title("r=%.2f, p=%.1e" % (r_value, decimal.Decimal(p_value)))
    ax.set_xlabel("Age at admission")
    simplify_borders(ax)
    set_axis_and_lim(ax, variable)
    plt.savefig(output_path + 'regressions/' + variable + '_' + disease_category)
    plt.close()
