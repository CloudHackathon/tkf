$(function () {
    Highcharts.chart('container', {
        chart: {
            type: 'bar'
        },
        title: {
            text: '涨势与舆论'
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
            data: [2.2, 0.44, 1.61, 0.55, 0.79, 0.4, 0.08, 1.26, -0.93, 1.2]
        }, {
            name: '讨论-热度排序',
            data: [1.89, 1.2, 1.44, 1.45, 1.15, 1.93, -0.36, 0.96, -2.21, 0.87]
        }, {
            name: '全部-时间排序',
            data: [1.75, 0.44, 1.23, 0.55, 1.02, 0.13, 0.25, 1.35, -0.93, 1.2], 'user.time': [2.2, 0.44, 1.61, 0.55, 0.79, 0.4, 0.08, 1.26, -0.93, 1.2]
        }, {
            name: '全部-热度排序',
            data: [2.4, -0.17, 1.62, 0.41, 0.98, 0.32, 1.19, 0.85, -0.76, 1.62]
        }]
    });
});
