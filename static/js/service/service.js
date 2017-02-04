app.factory('PantallaService', function($http) {
  var myService = {
    post: function() {
      var promise = $http.post('/cajas/').then(function (response) {
        return response.data;
      });
      return promise;
    },
    logica: function() {
      var promise = $http.get('/logica/').then(function (response) {
        return response.data;
      });
      return promise;
    }
  };
  return myService;
});


app.factory('TicketService', function($http) {
  var myService = {
    get: function() {
      var promise = $http.get('/Ticket/').then(function (response) {
        return response.data;
      });
      return promise;
    },
    post: function(pk) {
      var promise = $http.post('/Ticket/', pk).then(function (response) {
        return response.data;
      });
      return promise;
    }
  };
  return myService;
});