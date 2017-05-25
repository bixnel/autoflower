google.charts.load('current', {packages: ['corechart']});
google.charts.setOnLoadCallback(drawBasic1);
google.charts.setOnLoadCallback(drawBasic2);
google.charts.setOnLoadCallback(drawBasic3);



function drawBasic1(e) {

	var data = new google.visualization.DataTable();
	data.addColumn('string', 'Example');
	data.addColumn('number', 't');


	data.addRows(e);

	data.deleteRow

	var options = {
	hAxis: {
	  title: 'Время'
	},
	vAxis: {
	  title: 'Температура'
	}
	};

	var chart = new google.visualization.LineChart(document.getElementById('temp_div'));

	chart.draw(data, options);
}


function drawBasic2(e) {

	var data = new google.visualization.DataTable();
	data.addColumn('string', 'Example');
	data.addColumn('number', 'Освещенность');


	data.addRows(e);


	var options = {
	hAxis: {
	  title: 'Время'
	},
	vAxis: {
	  title: 'Люксы'
	}
	};

	var chart = new google.visualization.LineChart(document.getElementById('light_div'));

	chart.draw(data, options);
}


function drawBasic3(e) {

	var data = new google.visualization.DataTable();
	data.addColumn('string', 'Example');
	data.addColumn('number', 'Влажность');


	data.addRows(e);

	data.deleteRow

	var options = {
	hAxis: {
	  title: 'Время'
	},
	vAxis: {
	  title: ''
	}
	};

	var chart = new google.visualization.LineChart(document.getElementById('water_div'));

	chart.draw(data, options);
}

