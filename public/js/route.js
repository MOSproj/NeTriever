(function(){
    "use strict";

    angular.module('myApp').config(['$routeProvider', '$locationProvider', routing]);

    function routing($routeProvider, $locationProvider) {
        $routeProvider
        .when("/", {
            templateUrl : "/views/home.html"
        })
        .when("/categories/:category", {
            controller: 'postsCtrl',
            controllerAs:"category",
            templateUrl : "/views/categories.html"
        })
        .otherwise({
          redirectTo: '/'
        });

        $locationProvider.hashPrefix('');
        $locationProvider.html5Mode(true);
    }
})();
