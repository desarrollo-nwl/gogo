google.load("visualization", "1", {
	packages : ["corechart"]
});
google.setOnLoadCallback(drawChart);
function drawChart() {
	var data = google.visualization.arrayToDataTable([['Nombre', 'Respuestas'], ['SAMIR FAMADAS', 1], ['SUFIAN DE TOLEDO', 1], ['LAILA MALAGUILLA', 2], ['SALMA GASQUET', 3], ['FARIDA RUJANO', 3], ['MINA AUZA', 2], ['ERHIMO ANCIZAR', 2], ['DUNIA PERALIAS', 4], ['HAMED BARJACOBA', 1], ['HABIBA VILLAFUERTES', 3], ['DINA BOHER', 2], ['YUSEF DANUS', 3], ['FÁTIMA SOHORA CALLON', 2], ['NABIL ESTOPAÑAN', 2], ['ADAM MASERES', 3], ['SOHORA DELEITO', 5], ['SORAYA ERGUETA', 3], ['MIMOUNT SASTRIQUES', 2], ['SAMIRA CARROMERO', 4], ['ABDESELAM COMERAS', 3], ['FARAH TELLES', 2], ['MARÍA ÁFRICA ESTARRIAGA', 3], ['RAHMA PEÑAMARIA', 2], ['MIMOUN SABARICH', 2], ['KARIMA CARAFI', 2], ['MARIAM ROQUEÑI', 3], ['NORA SANDI', 2], ['YAMINA BONAVILA', 3], ['MARÍA FUENCISLA ARNALOT', 4], ['RACHIDA MELENDRERAS', 5], ['NAIMA DEVAL', 3], ['ALÍ EVIA', 1], ['OMAR MARABE', 2], ['FADMA ALFARA', 2], ['KARIM MUSOLES', 2], ['NADIA RUIZ DE AGUIRRE', 3], ['RACHID GIRAUT', 2], ['SONSOLES HENAR', 3], ['SAID JARIEGO', 3], ['NATIVIDAD RETAMINO', 2], ['ÁFRICA BASTAROS', 2], ['YASMINA JARTIN', 3], ['AICHA ONDARZA', 2], ['BILAL PARET', 2], ['ABDELKADER SANTAYA', 2], ['LUIS ANGEL ANTELA', 1], ['HASSAN LIBOREIRO', 3], ['MARÍA SONSOLES PASION', 3], ['BLANCA GRABULEDA', 2], ['MALIKA FERNANDINO', 2]]);

	var options = {
		legend : {
			position : 'top','alignment':'center'
		},
	};

	var chart = new google.visualization.Histogram(document.getElementById('histograma'));
	chart.draw(data, options);
};

$(document).ready(function() {
	$(window).resize(function() {
		drawChart();
	});
});
