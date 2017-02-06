app.controller('CajaAtencion', function(CajaService, $scope) {
	CajaService.TurnoEspera().then(function(d){
    	$scope.TurnosEspera = d;
    });
    CajaService.TurnoActivo().then(function(d){
    	if (d.length > 0) {
    		d[0].fields.Llamados -= 1;
    	}
    	$scope.TurnoActivo = d;
    });
	var init = function() {
    	console.log("intervalo");
    	CajaService.TurnoEspera().then(function(d){
	    	$scope.TurnosEspera = d;
	    });
	    
    	$scope.$apply();
    };
	setInterval(init,10000);
    
    $scope.Llamar = function(pk) {
    	CajaService.Llamar(pk).then(function(){
	    	CajaService.TurnoActivo().then(function(d){
	    		if (d.length > 0) {
		    		d[0].fields.Llamados -= 1;
		    	}
		    	$scope.TurnoActivo = d;
		    });
	    });
    };

    $scope.Finalizar = function(pk) {
    	CajaService.Finalizar(pk).then(function(){
		    	$scope.TurnoActivo = [];
	    });
    };
});

