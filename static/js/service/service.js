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
    },
    getEntidades: function() {
      var promise = $http.post('/entidad/').then(function (response) {
        return response.data;
      });
      return promise;
    }
  };
  return myService;
});


app.factory('CajaService', function($http) {
  var myService = {
    TurnoEspera: function() {
      var promise = $http.get('/turnosespera/').then(function (response) {
        return response.data;
      });
      return promise;
    },
    TurnoActivo: function() {
      var promise = $http.get('/turnoactivo/').then(function (response) {
        return response.data;
      });
      return promise;
    },
    Llamar: function(pk) {
      var promise = $http.get('/llamar/' + pk).then(function (response) {
        return response.data;
      });
      return promise;
    },
    Finalizar: function(pk) {
      var promise = $http.get('/finalizar/' + pk).then(function (response) {
        return response.data;
      });
      return promise;
    }
  };
  return myService;
});