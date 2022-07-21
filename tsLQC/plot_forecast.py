import seaborn as sns
import matplotlib.pyplot as plt


def plot_forecast(timeseries_input_df, forecast_df, plot_company):
    df = timeseries_input_df[timeseries_input_df['CompanyName'] == plot_company]
    historical_data = df.set_index('Date')['Value']

    df = forecast_df[forecast_df['CompanyName'] == plot_company]
    point_forecast = df.set_index('Date')['PointForecast'].iloc[0:48]
    upper_forecast = df.set_index('Date')['UpperForecast'].iloc[0:48]
    lower_forecast = df.set_index('Date')['LowerForecast'].iloc[0:48]

    sns.set_style("whitegrid")

    fig, ax1 = plt.subplots(1, 1, sharex=True, figsize=(13, 8))
    ax1.plot(historical_data, label='Historical Data', linestyle='dashed', c='k', marker='o')
    ax1.plot(point_forecast, label='Forecast', c='#0343DF')
    ax1.fill_between(point_forecast.index, lower_forecast, upper_forecast, alpha=0.2)
    ax1.set_xlim([historical_data.index[0], point_forecast.index[-1]])
    ax1.set_ylabel('Revenue in USD')
    ax1.set_xlabel('Date', )
    ax1.set_title('Forecast for ' + plot_company)
    plt.show()

    return
