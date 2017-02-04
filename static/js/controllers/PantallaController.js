app.controller('pantalla', function(PantallaService, $scope, $interval) {


    $scope.init = function() {
    	console.log("intervalo");
    	PantallaService.post().then(function(d){
    		$scope.data = d;
    	});
    	PantallaService.logica().then(function(d){
    		$scope.Turnos = d;
    	});
    };
	setInterval(function(){$scope.init();},2000});
    
});