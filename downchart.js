$(function () {
    Highcharts.chart('container', {
        chart: {
            type: 'bar'
        },
        title: {
            text: '跌势与舆论'
        },
        subtitle: {
            text: '来源：雪球'
        },
        xAxis: {
            categories: ['N如通', '云南城投', '麦迪科技', '卧龙地产', '华安证券', '海天精工', '蓝光发展', '神力股份', '三江购物', '三维股份'],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: '',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        tooltip: {
            valueSuffix: ''
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            x: -40,
            y: 80,
            floating: true,
            borderWidth: 1,
            backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
            shadow: true
        },
        credits: {
            enabled: false
        },
        series: [{
            name: '讨论-时间排序',
            data: [-0.32, -0.65, 0.52, -0.53, 0.81, -0.59, 0.04, 0.7, 0.01, -0.35]
        }, {
            name: '讨论-热度排序',
            data: [-0.63, 0.52, -0.52, -1.05, 0.07, 0.05, 1.47, 0.49, 0.98, 0.56]
        }, {
            name: '全部-时间排序',
            data: [-0.32, -0.65, 0.52, -0.52, 0.81, -0.59, -0.24, 1.16, -0.04, -0.35]
        }, {
            name: '全部-热度排序',
            data: [-0.22, 1.27, -0.38, -1.79, 0.62, 1.0, 0.08, 1.87, 0.99, 0.68]
        }]
    });
});
