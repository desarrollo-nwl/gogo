$(function() {

    Morris.Area({
        element: 'morris-area-chart',
        data: [{
            period: '2010 Q1',
            ventas: 3.6,
            logistica: null,
            finanzas: 4.2
        }, {
            period: '2010 Q2',
            ventas: 3.8,
            logistica: 4.2,
            finanzas: 4.1
        }, {
            period: '2010 Q3',
            ventas: 3.5,
            logistica: 3.8,
            finanzas: 4.1
        }, {
            period: '2010 Q4',
            ventas: 4.2,
            logistica: 3.6,
            finanzas: 4.5
        }, {
            period: '2011 Q1',
            ventas: 3.9,
            logistica: 4.2,
            finanzas: 4.0
        }, {
            period: '2011 Q2',
            ventas: 4.5,
            logistica: 4.2,
            finanzas: 2.8
        }, {
            period: '2011 Q3',
            ventas: 4.8,
            logistica: 3.7,
            finanzas: 4.2
        }, {
            period: '2011 Q4',
            ventas: 3.8,
            logistica: 3.9,
            finanzas: 4.1
        }, {
            period: '2012 Q1',
            ventas: 4.2,
            logistica: 4.4,
            finanzas: 3.4
        }, {
            period: '2012 Q2',
            ventas: 3.8,
            logistica: 3.9,
            finanzas: 4.5
        }],
        xkey: 'period',
        ykeys: ['ventas', 'logistica', 'finanzas'],
        labels: ['ventas', 'logistica', 'finanzas'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true
    });

    

});
