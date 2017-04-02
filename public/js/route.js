(function(){
    "use strict";

    angular.module('myApp').config(['$routeProvider', '$locationProvider', routing]);

    function routing($routeProvider, $locationProvider) {
        $routeProvider
        .when("/", {
            templateUrl : "/views/home.html"
        })
        .when("/category/:category/page/:page", {
            controller: 'postsCtrl',
            controllerAs:"category",
            templateUrl : "/views/category.html"
        })
        .otherwise({
          redirectTo: '/'
        });

        $locationProvider.hashPrefix('');
        $locationProvider.html5Mode(true);
    }
})();
