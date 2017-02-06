app.controller('ticket', function(TicketService, $scope) {
	_ini();
    $scope.Impresion = false;
    $scope.Turno = "";
    $scope.Entidad = "";
    $scope.Volver = function() {
        $scope.Impresion = false;
    };
function Print()
         {
          if (document.all) 
             {
               WebBrowser1.ExecWB(6, 6) //use 6, 1 to prompt the print dialog or 6, 6 to omit it; 
                WebBrowser1.outerHTML = "";
             }
         else
            {
             window.print();
             }
         }

    $scope.printDiv = function(divName) {
	 //  	var printContents = '<div style="font-size: 8em;text-align: center"><strong>' + $scope.Turno +'</strong></div>'+
		// 				'<br>'+
		// 				'<div style="text-align: center">'+
		// 					'<strong>' + $scope.Entidad.fields.Nombre + '</strong><br>'+
		// 					'<strong>' + $scope.Entidad.fields.Direccion + '</strong><br>'+
		// 					'<strong>' + $scope.Entidad.fields.Telefono + '</strong><br>'+
		// 					'<strong>' + $scope.Entidad.fields.Url + '</strong>'+
		// 				'</div>'
	  	
	 //  	var mywindow = window.open('', 'PRINT', 'height=400,width=600');
  //       window.focus();
	 //  	mywindow.blur();

  //       mywindow.document.write(printContents);

  //       //mywindow.document.close(); // necessary for IE >= 10
  //       // mywindow.focus(); // necessary for IE >= 10*/

  //       mywindow.print();
        
		setTimeout(function(){$.print("#printable");},100);
        
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
        TicketService.getEntidades().then(function(d) {
            if (d.length > 0) {
                $scope.Entidad = d[0];
            }
        });
    }

    
});