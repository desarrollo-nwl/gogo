google.load("visualization", "1", {
    packages: ["corechart"]
});
google.setOnLoadCallback(drawChart);

function drawChart() {
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Task');
    data.addColumn('number', 'Hours per Day');
    data.addRows([
        ['Sin Contestar', 4],
        ['Contestadas', 20]
        ]);
    var options = {
        legend: {position: 'top', maxLines: 1,'alignment':'center'},
        pieHole: 0.4,
        animation: {duration:800,easing:'in'}
    };
    var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
    chart.draw(data, options);
}
   