var app = angular.module('Turnos', []);
app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });
