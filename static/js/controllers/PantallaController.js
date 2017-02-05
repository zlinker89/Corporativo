app.controller('pantalla', function(PantallaService, $scope) {
	$scope.data = [];
	$scope.Turnos = [];

    var init = function() {
    	console.log("intervalo");
    	PantallaService.post().then(function(d){
    		$scope.data = d;
    	});
    	PantallaService.logica().then(function(d){
    		if ($scope.Turnos.length > 0) {
    			HasCambios($scope.Turnos, d);
    		}
    		$scope.Turnos = d;
    	});
    	$scope.$apply();
    };
	setInterval(init,2000);

	function HasCambios(list, Newlst) {
		console.log(list);
			for(var i in list){
				if(list[i]){
					if (list.length == Newlst.length) {
						if (list[i].fields.CodigoTurno != Newlst[i].fields.CodigoTurno || list[i].fields.Llamados != Newlst[i].fields.Llamados) {
								console.log("hubo un cambio " + list[i].fields.CodigoTurno + " ----- " + Newlst[i].fields.CodigoTurno);
								document.getElementById('player').play();
								var caja = "caja" + list[i].fields.Caja;
								ChangeColor(caja);
						}
					}
				}else{
					document.getElementById('player').play();
					var caja = "caja" + list[i].fields.Caja;
					ChangeColor(caja);
				}
			}
	};

	function ChangeColor(caja) {
		document.getElementById(caja).style.background = "#f2f2f2";
		setTimeout(function(){document.getElementById(caja).style.background = "white";}, 2500);
	}
});