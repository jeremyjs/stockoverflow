$(function () {
  $.get('/simulate/TSLA.json', function (response_string) {
    var res = JSON.parse(response_string);
    var prices =
    console.log(res);
    var chart = c3.generate({
      bindto: '.simulation.chart',
      data: {
        columns: [
          ['data1', 30, 200, 100, 400, 150, 250],
          ['data2', 50, 20, 10, 40, 15, 25]
        ]
      }
    });
  })
});
