app.controller('Logica', function(PantallaService, $scope) {

    PantallaService.logica().then(function(d){
    	$scope.data = d;
    });
});

