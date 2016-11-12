function momentFromUnix (uts) {
  return moment(uts, 'x');
}

function dateString (m) {
  return moment(m).format('YYYY-MM-DD');
}

function getPrice (daily) {
  return daily.price;
}

function getShares (daily) {
  return daily.shares;
}

function getCoh (daily) {
  return daily.cash_on_hand;
}

function getValue (daily) {
  var price = getPrice(daily);
  var shares = getShares(daily);
  var cash_on_hand = getCoh(daily);
  return cash_on_hand + shares * price;
}

$(function () {
  var symbol = $('#__template__').data('symbol'); // 'TSLA';
  console.log('symbol:', symbol);
  var simulation_url = '/simulate/' + symbol + '.json';
  $.get(simulation_url, function (response_string) {
    var res = JSON.parse(response_string);
    console.log(res);
    var dates = _.concat(['x'], _.keys(res.dailies).map(Number).map(momentFromUnix).map(dateString));
    console.log(dates);
    var prices = _.concat(['price'], _.values(res.dailies).map(getPrice));
    console.log(prices);
    var values = _.concat(['value'], _.values(res.dailies).map(getValue));
    console.log(values);
    var chart = c3.generate({
      bindto: '.simulation.chart',
      data: {
        x: 'x',
        columns: [
          dates,
          prices,
          values,
          // ['x', '2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04', '2016-01-05', '2016-01-06'],
          // ['data1', 30, 200, 100, 400, 150, 250],
          // ['data2', 50, 20, 10, 40, 15, 25],
        ],
        axes: {
          'price': 'y',
          'value': 'y2',
        }
      },
      axis: {
        x: {
          type: 'timeseries',
          tick: {
            format: '%Y-%m-%d',
          },
        },
        y2: {
          show: true
        }
      },
    });
  })
});
