app.controller('ticket', function(TicketService, $scope) {
	_ini();
    
    $scope.GenerarTicket = function(obj) {
    	console.log(obj);
    };

    function _ini() {
    	TicketService.post().then(function(d){
	    	$scope.data = d;
	    });
    }
});