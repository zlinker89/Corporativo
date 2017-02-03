app.controller('ticket', function(TicketService, $scope) {
	_ini();
    $scope.Impresion = false;
    $scope.Turno = "";

    $scope.Volver = function() {
        $scope.Impresion = false;
    };

    $scope.printDiv = function(divName) {
	  	var printContents = '<div style="font-size: 8em;text-align: center"><strong>' + $scope.Turno +'</strong></div>'+
						'<br>'+
						'<div style="text-align: center">'+
							'<strong>{$Empresa.Nombre$}</strong><br>'+
							'<strong>{$Empresa.Direccion$}</strong><br>'+
							'<strong>{$Empresa.Telefono$}</strong><br>'+
							'<strong>{$Empresa.Url$}</strong>'+
						'</div>'
	  	
	  	var mywindow = window.open('', 'PRINT', 'height=400,width=600');
        window.focus();
	  	mywindow.blur();

        mywindow.document.write(printContents);

        //mywindow.document.close(); // necessary for IE >= 10
        // mywindow.focus(); // necessary for IE >= 10*/

        mywindow.print();
        
		setTimeout(function(){mywindow.close();},1000);
	}; 

    $scope.GenerarTicket = function(obj) {
    	TicketService.post(obj.pk).then(function(d){
    		console.log(d);
    		$scope.Turno = d;
    		$scope.Impresion = true;
    		$scope.printDiv("printable");
	    });
    };

    function _ini() {
    	TicketService.get().then(function(d){
	    	$scope.data = d;
	    });
    }

    
});