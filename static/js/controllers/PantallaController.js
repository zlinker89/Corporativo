app.controller('pantalla', function(PantallaService, $scope) {

    PantallaService.post().then(function(d){
    	$scope.data = d;
    });
});