app.controller('pantalla', function(PantallaService, $scope) {

    var init = function() {
    	console.log("intervalo");
    	PantallaService.post().then(function(d){
    		$scope.data = d;
    	});
    	PantallaService.logica().then(function(d){
    		$scope.Turnos = d;
    		console.log(d);
    	});
    	$scope.$apply();
    };
	setInterval(init,2000);

});