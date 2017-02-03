app.factory('PantallaService', function($http) {
  var myService = {
    post: function() {
      var promise = $http.post('/cajas/').then(function (response) {
        return response.data;
      });
      return promise;
    }
  };
  return myService;
});


app.factory('TicketService', function($http) {
  var myService = {
    post: function() {
      var promise = $http.post('/Ticket/').then(function (response) {
        return response.data;
      });
      return promise;
    }
  };
  return myService;
});