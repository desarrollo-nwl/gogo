//radar chart data
var radarData = {
	labels : ["Eating","Drinking","Sleeping","Designing","Coding","Partying","Running"],
	datasets : [
		{
			 fillColor: "rgba(102,45,145,.1)",
			 strokeColor: "rgba(102,45,145,1)",
			pointColor : "rgba(220,220,220,1)",
			pointStrokeColor : "#fff",
			data : [65,59,90,81,56,55,40]
		},
		{
	        fillColor: "rgba(63,169,245,.1)",
            strokeColor: "rgba(63,169,245,1)",
			pointColor : "rgba(151,187,205,1)",
			pointStrokeColor : "#fff",
			data : [28,48,40,19,96,27,100]
		}
	]
}

//Create Radar chart
var ctx2 = document.getElementById("radarChart").getContext("2d");
var myNewChart = new Chart(ctx2).Radar(radarData);

new Chart(ctx2).Radar(radarData,options);