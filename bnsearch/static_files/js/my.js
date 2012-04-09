$.ajaxSetup({ traditional: true });

$(document).ready(function() {
//    $("#submit").remove();
    $("#searchform").append('<input type="button" value="Искать Ajax\'ом" id="search"></input>');
});

$(document).ready(addClickHandlers);

function populateResults(data) {
    if(data[1].length > 0) {
	var table = '<table border="1"><tr><th>';
	table = table.concat(data[0].join("</th><th>"));
	table = table.concat("</th></tr>");
	
	
	for (var i=0, l=data[1].length; i<l;i++) {
	    html_line = "<tr><td>";
	    html_line = html_line.concat(data[1][i].join('</td><td>'));
	    html_line = html_line.concat("</td></tr>");
	    table = table.concat(html_line);
	}
	table = table.concat('</table>');
    
	$('#results').html(table);
    } else {
	$('#results').html('Ничего не найдено Ajax\'ом');

    }
    $("#spinner").removeClass('visible');
    $("#spinner").addClass('invisible');
}

function addClickHandlers() {
    $("#search").click(function() {

	$("#results").html('')

        var postdata = {
            'price_to': $("#id_price_to").val(),
            'price_from': $("#id_price_from").val(),
            'rooms_to': $("#id_rooms_to").val(),
            'rooms_from': $("#id_rooms_from").val(),
	    'fmt': 'json',
	    'metro_stations': [],
            'csrfmiddlewaretoken': $token
        }

	$(":checked").each(function() {
	    postdata['metro_stations'].push($(this).val());
	});


        $("#spinner").removeClass('invisible');
        $("#spinner").addClass('visible');

        $.post('/', postdata, populateResults);
    });
}

